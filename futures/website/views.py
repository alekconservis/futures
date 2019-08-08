from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Product, Contract

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def products(request):
    product_list = Product.objects.order_by('-expires_at')[:5]
    context = {
        'product_list': product_list,
    }
    return render(request, 'website/products.html', context)


def contracts(request):
    contract_list = Contract.objects.order_by('-end_date')[:5]
    context = {
        'contracts': contract_list
    }
    return render(request, 'website/contracts.html', context)

