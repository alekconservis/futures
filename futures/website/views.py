from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            print('-- user authenticated')
            login(request, user)
            return redirect('home')
        else:
            print('-- not authenticated')
            return render(request, 'login.html',
                          {"info": "Invalid username and password combination."})
    else:
        print('- get')
        return render(request, 'login.html',
            {"info": "Please login."})


def home(request):
    return render(request, 'home.html',
                  {"info": "..."})