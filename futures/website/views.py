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
            login(request, user)
            return redirect('product_list')
        else:
            return render(request, 'website/login.html',
                        {"info": "Invalid username and password combination."})
    else:
        return render(request, 'website/login.html',
          {"info": "Please login."})


def account(request):
    return render(request, 'website/account.html')


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
        contract_list = Contract.objects.order_by('-end_date')
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



