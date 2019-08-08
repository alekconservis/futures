from django.contrib import admin
from django.urls import path
from .views import login_view, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login.html', login_view, name='login'),
    path('home.html', home, name='home'),
]
