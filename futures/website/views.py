from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    if request.method == "POST":
        print('- post')
        username = request.POST["username"]
        password = request.POST["password"]
        print(f'-- username: {username}')
        print(f'-- password: {password}')
        return render(request, 'login.html',
                      {"item": "hello from django app",
                       "username": username})
    else:
        print('- get')
        return render(request, 'login.html',
                        {"item": "hello from django app"})
