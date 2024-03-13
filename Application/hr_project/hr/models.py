from django.db import models
from django.conf import settings
from django.utils import timezone


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Ingrediente(MyModel):
    class Meta:
        db_table = 'ingrediente'
        verbose_name_plural = 'Ingrediente'

    def __str__(self):
        return self.nume

    nume = models.CharField(
        max_length=20,
        null=False
    )


class Pizza(MyModel):
    class Meta:
        db_table = 'pizza'
        verbose_name_plural = 'Pizza'

    def __str__(self):
        return self.nume

    nume = models.CharField(
        max_length=20,
        null=False
    )

    pret = models.DecimalField(
        decimal_places=1,
        max_digits=4,
        default=20,
        null=False
    )

    descriere = models.CharField(
        max_length=200,
        null=False
    )

    link = models.CharField(
        max_length=200,
        null=False
    )


class Pizza_ingrediente(MyModel):
    class Meta:
        db_table = 'pizza_ingrediente'
        verbose_name_plural = 'Pizza Ingrediente'

    def __str__(self):
        return f'{self.Pizza.nume} {self.Ingrediente.nume}'

    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def id_pizza(self):
        return self.Pizza.nume

    id_pizza.short_description = "Pizza"
    id_pizza.admin_order_field = "Pizza__id_pizza"

    Ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)

    def id_ingrediente(self):
        return self.Ingrediente.nume

    id_ingrediente.short_description = "Ingrediente"
    id_ingrediente.admin_order_field = "Ingrediente__id_ingrediente"


class Lista_favorite(MyModel):
    class Meta:
        db_table = 'lista_favorite'
        verbose_name_plural = 'Lista Favorite'

    def __str__(self):
        return f'{self.User.email} {self.Pizza.nume}'

    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def id_pizza(self):
        return self.Pizza.nume

    id_pizza.short_description = "Pizza"
    id_pizza.admin_order_field = "Pizza__id_pizza"

    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    def email(self):
        return self.User.email

    email.short_description = "Email"
    email.admin_order_field = "User__email"


class Cos_cumparaturi(MyModel):
    class Meta:
        db_table = 'cos_cumparaturi'
        verbose_name_plural = 'Cos Cumparaturi'

    def __str__(self):
        return f'{self.User.email} {self.Pizza.nume}'

    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, default="0")

    def id_pizza(self):
        return self.Pizza.nume

    id_pizza.short_description = "Pizza"
    id_pizza.admin_order_field = "Pizza__id_pizza"

    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default='0'
    )

    def email(self):
        return self.User.email

    email.short_description = "Email"
    email.admin_order_field = "User__email"

    nr_produse = models.DecimalField(
        decimal_places=0,
        max_digits=4,
        default=1,
        null=False
    )


class Lista_comanda(MyModel):
    class Meta:
        db_table = 'lista_comanda'
        verbose_name_plural = 'Lista Comenzi'

    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE, null=True)

    def id_pizza(self):
        return self.Pizza.nume

    User = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default='0'
    )

    def id_user(self):
        return self.User.id

    nr_produse = models.DecimalField(max_digits=2, decimal_places=0, null=True)

    livrata = models.BooleanField(default=False)

    adresa = models.CharField(
        max_length=40,
        null=False,
        default='XXXXXXXXXXXX'
    )

    nr_card = models.CharField(
        max_length=16,
        null=False,
        default='4242424242424242'
    )

    data_expirare = models.CharField(
        max_length=40,
        null=False,
        default='XX/XX'
    )

    CVV = models.CharField(
        max_length=40,
        null=False,
        default='XXX'
    )

    data_cumparare = models.DateTimeField(default=timezone.now)
    data_actualizare = models.DateTimeField(auto_now=True)


class Categorie(MyModel):
    class Meta:
        db_table = 'categorie'
        verbose_name_plural = 'Categorii'

    def __str__(self):
        return self.nume

    nume = models.CharField(
        max_length=20,
        null=False
    )


class Pizza_categorie(MyModel):
    class Meta:
        db_table = 'pizza_categorie'
        verbose_name_plural = 'Pizza Categorie'

    def __str__(self):
        return f'{self.Pizza.nume} {self.Categorie.nume}'

    Pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)

    def id_pizza(self):
        return self.Pizza.nume

    id_pizza.short_description = "Pizza"
    id_pizza.admin_order_field = "Pizza__id_pizza"

    Categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    def id_categorie(self):
        return self.Categorie.nume

    id_categorie.short_description = "Categorie"
    id_categorie.admin_order_field = "Categorie__id_categorie"
