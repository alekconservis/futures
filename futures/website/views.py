from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Product

def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")

def products(request):
  product_list = Product.objects.order_by('-expires_at')[:5]
  context = {
      'product_list': product_list,
  }
  return render(request, 'website/products.html', context)
