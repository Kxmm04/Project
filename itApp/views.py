from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from itApp.models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')
def login(requset):
    return render(requset, 'login.html')

def user_login(request):#ฟังก์ชันล็อกอิน
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        username = request.POST['username']
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        messages.success(request, "Login success...")
        return redirect('home')
    else:
        messages.error(request, "Invalid username or password!!!")
        return redirect('user_login') # หรือ return redirect('home')

def user_logout(request):#ฟังก์ชันล็อกเอ้าท์
    logout(request)
    messages.info(request, "User logout...")
    return redirect('home')

def showMessages(request):
    return render(request, 'showMessages.html')

def computerList(request):
    computers = Computer.objects.all()  
    context = {'computers': computers}
    return render(request, 'computerList.html', context)

def computerOne(request,id):
    computers = Computer.objects.get(comid=id)
    context = {'computers': computers}
    return render(request, 'computerOne.html', context)

def accessoriesList(request):
    computers = Computer.objects.all()  
    context = {'computers': computers}
    return render(request, 'accessoriesList.html', context)

def storageList(request):
    storages = Storage.objects.all()  
    context = {'storages': storages}
    return render(request, 'storageList.html', context)

def storageOne(request,id):
    storages = Storage.objects.get(storageid=id)
    context = {'storages': storages}
    return render(request, 'storageOne.html', context)

