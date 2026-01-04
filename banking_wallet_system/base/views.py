from django.shortcuts import render, redirect
from .models import Users, Transactions, Transactionstatus, Ledgerentries, Auditlog, Accounts
from django.contrib.auth.models import User
from django.utils import timezone # for storing time related fields
from django.db import transaction
from django.contrib.auth import authenticate, login, logout

# initialisation views : Login, Logout and Register
def register_user(request):
    if request.method == 'POST' :
        details = request.POST
        
        try:
            with transaction.atomic():
                # 1. object for digital profile
                auth_user = User.objects.create_user(
                    username = details.get('email'),
                    email = details.get('email'),
                    password = details.get('password')
                )

                # 2. object for Banking profile
                User.objects.create(
                    auth_user = auth_user,
                    name = details.get('name'),
                    email = details.get('email'),
                    phone = details.get('phone'),
                    status = 'ACTIVE',
                    createdate = timezone.now(),
                )

                return redirect('base/login.html')

        except Exception as e:
            return render(request, 'base/register.html', {'error': f"System error: {str(e)}"})
        
    return render(request,'base/register.html')

def login_user(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(request, username=u, password=p)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'base/login.html', {'error': "Invalid AUTH_KEY or AUTH_ID."})
        
    return render(request, 'base/login.html')

def logout_user(request):
    logout(request)
    return redirect('login')

# base/home page view :
def home(request):
    return render(request, 'base/home.html')
