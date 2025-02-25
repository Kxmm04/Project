from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout


    
def login(requset):
    return render(requset, 'login.html')
def home(request):
    return render(request, 'base.html')
def home(request):
    return render(request, 'home.html')
