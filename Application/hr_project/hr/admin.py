from django.contrib import admin
from .models import *


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ["nume"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ["nume", "pret", "descriere"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Pizza_ingrediente)
class Pizza_ingredienteAdmin(admin.ModelAdmin):
    list_display = ["id_pizza", "id_ingrediente"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Lista_favorite)
class Lista_favoriteAdmin(admin.ModelAdmin):
    list_display = ["User", "id_pizza"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Cos_cumparaturi)
class Cos_cumparaturiAdmin(admin.ModelAdmin):
    list_display = ["User", "id_pizza"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Lista_comanda)
class ListaComandaAdmin(admin.ModelAdmin):
    list_display = ["id_pizza", "id_user", "nr_produse", "livrata", "adresa", "nr_card", "data_expirare",
                    "CVV", "data_cumparare", "data_actualizare"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ["nume"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset


@admin.register(Pizza_categorie)
class Pizza_CategorieAdmin(admin.ModelAdmin):
    list_display = ["id_pizza", "id_categorie"]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        user = request.user

        return queryset
