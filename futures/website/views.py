from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse

from .models import Product
from .models import Contract
from .models import User


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
            return render(request, 'website/login.html', {"info": "Invalid username and password combination."})
    else:
        print('- get')
        return render(request, 'website/login.html', {"info": "Please login."})


def account(request):
    return render(request, 'website/account.html')


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

def buy_contract(request, contract_id):
    contract = Contract.objects.get(pk=contract_id)
    user = User.objects.get(pk=request.user.id)

    contract.price = contract.product.price

    if contract.seller:
        contract.buyer = user
    else:
        contract.seller = user

    contract.save()

    messages.add_message(request, messages.SUCCESS, 'Successfully Bought Contract!')

    return redirect('contract_list')



