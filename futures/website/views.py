from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib import messages
from django.http import HttpResponse
from django.db.models import Q

from .models import Product
from .models import Contract
from .models import User


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            return render(request, 'website/login.html',
                        {"info": "Invalid username and password combination."})
    else:
        return render(request, 'website/login.html',
          {"info": "Please login."})


def account(request):
    user = User.objects.get(pk=request.user.id)
    userContractsBought = Contract.objects.filter(buyer_id=user.id)
    userContractsSold = Contract.objects.filter(seller_id=user.id)

    return render(request, 'website/account.html', {
        'boughtContracts': userContractsBought.count(),
        'soldContracts': userContractsSold.count()
    })


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def products(request):
    product_list = Product.objects.order_by('-name')
    for product in product_list:
        # randomize product prices
        product.fluctuate()
    context = {
        'product_list': product_list,
    }
    return render(request, 'website/products.html', context)


def contracts(request):
    if request.method == "POST":
        contract = Contract(
            # quantity = request.POST["quantity"],
            price = request.POST["price"],
            end_date = request.POST["expires_at"],
            product_id = request.POST["product_id"],
        )

        user = User.objects.get(id=request.user.id)
        if request.POST["type"] == "buy":
            contract.buyer = user
        else:
            contract.seller = user

        contract.save()
        return redirect("contract_list")

    else:
        contract_list = Contract.objects.exclude(seller__isnull=False, buyer__isnull=False).order_by('-end_date')
        context = {
            'contract_list': contract_list
        }
        return render(request, 'website/contracts.html', context)

def create_contract(request, id):
    product = Product.objects.get(pk=id)
    context = {
        'product': product,
    }
    return render(request, 'website/create_contract.html', context)

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



