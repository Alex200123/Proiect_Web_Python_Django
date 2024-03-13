from _decimal import Decimal
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from rest_framework import permissions
from rest_framework import viewsets

from .serializer import *


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAuthenticated]


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteSerializer
    permission_classes = [permissions.IsAuthenticated]


class PizzaViewSet(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    permission_classes = [permissions.IsAuthenticated]


class Pizza_ingredienteViewSet(viewsets.ModelViewSet):
    queryset = Pizza_ingrediente.objects.all()
    serializer_class = Pizza_ingredienteSerializer
    permission_classes = [permissions.IsAuthenticated]


class Lista_favoriteViewSet(viewsets.ModelViewSet):
    queryset = Lista_favorite.objects.all()
    serializer_class = Lista_favoriteSerializer
    permission_classes = [permissions.IsAuthenticated]


class Cos_cumparaturiViewSet(viewsets.ModelViewSet):
    queryset = Cos_cumparaturi.objects.all()
    serializer_class = Cos_cumparaturiSerializer
    permission_classes = [permissions.IsAuthenticated]


class Lista_comandaViewSet(viewsets.ModelViewSet):
    queryset = Lista_comanda.objects.all()
    serializer_class = Lista_comandaSerializer
    permission_classes = [permissions.IsAuthenticated]


class CategorieViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = CategorieSerializer
    permission_classes = [permissions.IsAuthenticated]


class Pizza_categorieViewSet(viewsets.ModelViewSet):
    queryset = Pizza_categorie.objects.all()
    serializer_class = Pizza_categorieSerializer
    permission_classes = [permissions.IsAuthenticated]


@login_required(login_url='login')
def shop(request, categorie_nume=None):
    categorie = Categorie.objects.order_by('-nume')
    ingredient = Ingrediente.objects.order_by('-nume')

    if categorie_nume:
        pizza_categorii = Pizza_categorie.objects.filter(Categorie__nume=categorie_nume)
        pizza_ids = [pc.Pizza.id for pc in pizza_categorii]
        pizza = Pizza.objects.filter(id__in=pizza_ids).order_by('nume')
    else:
        pizza = Pizza.objects.order_by('nume')

    if request.method == 'POST':
        pret = request.POST.get('fav_language')
        ingrediente_selectate = request.POST.getlist('ingredient')
        search_text = request.POST.get('search_text')

        if pret:
            if pret == "pret_15":
                pizza = pizza.filter(pret__lt=15)
            elif pret == "pret_25":
                pizza = pizza.filter(pret__lt=25)
            elif pret == "pret_35":
                pizza = pizza.filter(pret__lt=35)
        if ingrediente_selectate:
            filtered_pizzas = []
            for piz in pizza:
                contains_all_selected_ingredients = True
                for ingrediente in ingrediente_selectate:
                    if not piz.pizza_ingrediente_set.filter(Ingrediente__nume=ingrediente).exists():
                        contains_all_selected_ingredients = False
                        break

                if contains_all_selected_ingredients:
                    filtered_pizzas.append(piz)
            pizza = filtered_pizzas
        if search_text:
            pizza = pizza.filter(nume__icontains=search_text)
    context = {'pizzas': pizza,
               'categorii': categorie,
               'ingrediente': ingredient}
    return render(request, 'shop.html', context)


def user_login(request):
    if request.method == 'POST':
        if 'Login_button' in request.POST:
            username_login = request.POST['nume_login']
            password_login = request.POST['password_login']
            user_log = authenticate(username=username_login, password=password_login)
            if user_log is not None:
                if user_log.is_active:
                    login(request, user_log)
                    # Redirect to index page.
                    return HttpResponseRedirect("http://localhost:8000/")
                else:
                    # Return a 'disabled account' error message
                    return HttpResponse("You're account is disabled.")
        else:
            username_signup = request.POST['nume_signup']
            email_signup = request.POST['email_signup']
            password_signup = request.POST['password_signup']
            user_signup = User.objects.create_user(username=username_signup, email=email_signup,
                                                   password=password_signup)
            user_signup.is_active = True
            return HttpResponseRedirect("http://localhost:8000/")
    else:
        return render(request, 'login.html')


def index(request):
    return render(request, 'index.html')


@login_required(login_url='login')
def wishlist(request):
    user = request.user
    pizza = Pizza.objects.filter(lista_favorite__User=user)
    context = {'pizzas': pizza}
    return render(request, 'wishlist.html', context)


@login_required(login_url='login')
def checkout(request):
    user = request.user
    cos_cumparaturi = Cos_cumparaturi.objects.filter(User=user)
    subtotal = 0
    for cos in cos_cumparaturi:
        if cos.User.username == user.username:
            subtotal = cos.Pizza.pret * cos.nr_produse + subtotal

    suma = subtotal + 10
    context = {'user': user,
               'cos_cumparaturis': cos_cumparaturi,
               'suma': suma,
               'subtotal': subtotal}
    return render(request, 'checkout.html', context)


@login_required(login_url='login')
def cart(request):
    pizza = Pizza.objects.order_by('-nume')
    user = request.user
    cos_cumparaturi = Cos_cumparaturi.objects.filter(User=user)
    shipping = 10
    if request.method == 'POST':
        if 'Update' in request.POST:
            nr_produse_lista = []
            for cos in cos_cumparaturi:
                nume_input = cos.Pizza.nume
                cantita = request.POST.get(nume_input)
                cos.nr_produse = cantita
                if Decimal(cantita) <= 0:
                    Cos_cumparaturi.objects.filter(Pizza=cos.Pizza, User=cos.User).delete()
                else:
                    cos.save()
                    if cantita is not None:
                        nr_produse_lista.append(Decimal(cantita))
            cos_cumparaturi = Cos_cumparaturi.objects.filter(User=user)
            subtotal = 0
            iterator = 0
            for cos in cos_cumparaturi:
                if cos.User.username == user.username:
                    subtotal = cos.Pizza.pret * nr_produse_lista[iterator] + subtotal
                    iterator = iterator + 1

            suma = subtotal + shipping
            context = {'pizzas': pizza,
                       'user': user,
                       'cos_cumparaturis': cos_cumparaturi,
                       'suma': suma,
                       'subtotal': subtotal
                       }

            return render(request, 'cart.html', context)
    else:
        subtotal = 0
        for cos in cos_cumparaturi:
            if cos.User.username == user.username:
                subtotal = cos.Pizza.pret * cos.nr_produse + subtotal

        suma = subtotal + shipping 
        context = {'pizzas': pizza,
                   'user': user,
                   'cos_cumparaturis': cos_cumparaturi,
                   'suma': suma,
                   'subtotal': subtotal}

        return render(request, 'cart.html', context)


@login_required(login_url='login')
def add_to_wishlist(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    user = request.user

    if not Lista_favorite.objects.filter(User=user, Pizza=pizza).exists():
        Lista_favorite.objects.create(User=user, Pizza=pizza)
    return redirect('shop')


@login_required(login_url='login')
def add_to_cart(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    user = request.user
    cos, created = Cos_cumparaturi.objects.get_or_create(User=user, Pizza=pizza)

    if not created:
        cos.nr_produse += 1
        cos.save()
    return redirect('shop')


@login_required(login_url='login')
def remove_from_wishlist(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    user = request.user

    if Lista_favorite.objects.filter(User=user, Pizza=pizza).exists():
        entry = Lista_favorite.objects.get(User=user, Pizza=pizza)
        entry.delete()

    return redirect('wishlist')


@login_required(login_url='login')
def add_to_cart_wish(request, pizza_id):
    pizza = Pizza.objects.get(id=pizza_id)
    user = request.user
    cos, created = Cos_cumparaturi.objects.get_or_create(User=user, Pizza=pizza)

    if not created:
        cos.nr_produse += 1
        cos.save()
    return redirect('wishlist')


@login_required
def pay(request):
    user = request.user
    if request.method == 'POST':
        cos_cumparaturi = Cos_cumparaturi.objects.filter(User=user)

        if not cos_cumparaturi.exists():
            return redirect('fail')

        for cos in cos_cumparaturi:
            Lista_comanda.objects.create(
                Pizza=cos.Pizza,
                User=user,
                nr_produse=cos.nr_produse,
                adresa=request.POST.get('address', ''),  # obțineți adresa din formularul HTML
                nr_card=request.POST.get('card', ''),  # obțineți numărul cardului din formularul HTML
                data_expirare=request.POST.get('data', ''),  # obțineți data expirării din formularul HTML
                CVV=request.POST.get('cvv', ''),  # obțineți CVV din formularul HTML
                livrata=False  # setați opțiunea de livrare la False
            )
        cos_cumparaturi.delete()

        if not cos_cumparaturi.exists():
            return redirect('success')


@login_required
def success(request):
    return render(request, 'success.html')


@login_required
def fail(request):
    return render(request, 'fail.html')


@login_required
def istoric(request):
    pizza = Pizza.objects.order_by('-nume')
    user = request.user
    lista_comanda = Lista_comanda.objects.filter(User=user)

    context = {'pizzas': pizza,
               'user': user,
               'lista_comandas': lista_comanda}

    return render(request, 'istoric.html', context)