"""hr_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add file_backup import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add file_backup import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from hr import views
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'users', views.UserViewSet)
router.register(r'ingrediente', views.IngredienteViewSet)
router.register(r'pizza', views.PizzaViewSet)
router.register(r'pizza_ingrediente', views.Pizza_ingredienteViewSet)
router.register(r'lista_favorite', views.Lista_favoriteViewSet)
router.register(r'cos_cumparaturi', views.Cos_cumparaturiViewSet)
router.register(r'lista_comanda', views.Lista_comandaViewSet)
router.register(r'categorie', views.CategorieViewSet)
router.register(r'pizza_categorie', views.Pizza_categorieViewSet)
urlpatterns = [
    # path('index/', views.index),
    path('rest', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('shop/', views.shop, name='shop'),
    path('shop/<str:categorie_nume>/', views.shop, name='shop_by_categorie'),
    path('login', views.user_login),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('shop/', views.shop, name='shop'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('add_to_cart/<int:pizza_id>/', views.add_to_cart, name='add_to_cart'),
    path('add_to_cart_wish/<int:pizza_id>/', views.add_to_cart_wish, name='add_to_cart_wish'),
    path('add_to_wishlist/<int:pizza_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:pizza_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('pay', views.pay, name='pay'),
    path('success', views.success, name='success'),
    path('fail', views.fail, name='fail'),
    path('history', views.istoric, name='history'),
]

# path('sign_in/', views.user_login),
# path('trimitere_mail/', views.send_email),
# path('casuta_postala/', views.casutaPostala),
# path('orar/', views.other_time_table),
# path('arhiva/', views.arhiva),
# path('situatie_scolara/', views.situatie_scolara),
# path('date_personale/', views.date_personale),
# path('admin/', admin.site.urls),
# path('pagina_principala/', views.pagina_principala),