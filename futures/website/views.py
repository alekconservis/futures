from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from django.http import HttpResponse

from .models import Product
from .models import Contract


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
          print('-- user authenticated')
          login(request, user)
          return redirect('product_list')
        else:
          print('-- not authenticated')
          return render(request, 'website/login.html',
                        {"info": "Invalid username and password combination."})
    else:
        print('- get')
        return render(request, 'website/login.html',
          {"info": "Please login."})


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
        'contract_list': contract_list
    }
    return render(request, 'website/contracts.html', context)

