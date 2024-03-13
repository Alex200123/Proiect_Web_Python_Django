from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "email", "groups"]


class IngredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ["url", "nume"]


class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = ["url", "nume", "pret", "descriere"]


class Pizza_ingredienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza_ingrediente
        fields = ["url", "Pizza", "Ingrediente"]


class Lista_favoriteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lista_favorite
        fields = ["url", "User", "Pizza"]


class Cos_cumparaturiSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cos_cumparaturi
        fields = ["url", "User", "Pizza"]


class Lista_comandaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lista_comanda
        fields = ["url", "Pizza", "Cos_cumparaturi", "nr_produse", "livrata", "adresa", "nr_card",
                  "data_expirare", "CVV", "data_cumparare", "data_actualizare"]


class CategorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ["url", "nume"]


class Pizza_categorieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza_ingrediente
        fields = ["url", "Pizza", "Categorie"]


# def check_expiry_month(value):
#     if not 1 <= int(value) <= 12:
#         raise serializers.ValidationError("Invalid expiry month.")
#
#
# def check_expiry_year(value):
#     today = datetime.datetime.now()
#     if not int(value) >= today.year:
#         raise serializers.ValidationError("Invalid expiry year.")
#
#
# def check_cvc(value):
#     if not 3 <= len(value) <= 4:
#         raise serializers.ValidationError("Invalid cvc number.")
#
#
# def check_payment_method(value):
#     payment_method = value.lower()
#     if payment_method not in ["card"]:
#         raise serializers.ValidationError("Invalid payment_method.")
#
#
# class CardInformationSerializer(serializers.Serializer):
#     card_number =  serializers.CharField(
#         max_length=150, required=True
#     )
#     expiry_month = serializers.CharField(
#         max_length=150,
#         required=True,
#         validators=[check_expiry_month],
#     )
#     expiry_year = serializers.CharField(
#         max_length=150,
#         required=True,
#         validators=[check_expiry_year],
#     )
#     cvc = serializers.CharField(
#         max_length=150,
#         required=True,
#         validators=[check_cvc],
#     )
