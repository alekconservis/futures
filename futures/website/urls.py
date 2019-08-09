
from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_view, name='login'),
    path('', views.index, name='index'),
    path('contracts', views.contracts, name='contract_list'),
    path('contracts/buy/<int:contract_id>/', views.buy_contract, name='buy_contract'),
    path('products', views.products, name='product_list'),
    path('account', views.account, name='account'),
    path('products/<int:id>/contracts/new', views.create_contract, name='create_contract'),
]
