from django.shortcuts import render
from .models import Contract

# Create your views here.
def index(request):
  return HttpResponse("Hello, world. You're at the polls index.")

def contracts(request):
    contract_list = Contract.objects.order_by('-end_date')[:5]
    context = {
      'contracts': contract_list
    }
    return render(request, 'website/contracts.html', context)