
from django.urls import path
from . import views

urlpatterns = [
    path('login.html', views.login_view, name='login'),
    path('home.html', views.home, name='home'),
    path('', views.index, name='index'),
    path('contracts', views.contracts, name='contract_list'),
    path('products', views.products, name='product_list'),
]
