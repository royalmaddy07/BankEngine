from django.shortcuts import render, redirect
from .models import Users, Transactions, Transactionstatus, Ledgerentries, Auditlog, Accounts
from django.contrib.auth.models import User
from django.utils import timezone # for storing time related fields
from django.db import transaction, IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# initialisation views : Login, Logout and Register
from django.db import IntegrityError

def register_user(request):
    if request.method == 'POST':
        details = request.POST
        name = details.get('name')
        email = details.get('email')
        password = details.get('password')
        cpassword = details.get('cpassword')
        phone = details.get('phone')

        # 1. Validation Logic (Catching errors before they hit the DB)
        if password != cpassword:
            return render(request, 'base/register.html', {'error': "Access Keys do not match."})
        
        if len(phone) != 10:
            return render(request, 'base/register.html', {'error': "Invalid Phone Format. 10 digits required."})

        try:
            with transaction.atomic():
                # 1. Create Digital Profile
                auth_user = User.objects.create_user(
                    username=email,
                    email=email,
                    password=password
                )

                # 2. Create Banking Profile (Using your custom 'Users' model)
                Users.objects.create(
                    auth_user=auth_user,
                    name=name,
                    email=email,
                    phone=phone,
                    status='ACTIVE',
                    createdate=timezone.now(),
                )

            messages.success(request, "Account created successfully!")
            return redirect('login')

        except IntegrityError:
            # Catch duplicate email/phone specifically
            return render(request, 'base/register.html', {'error': "Identity Conflict: Email or Phone already registered."})
        except Exception as e:
            # Catch-all for unexpected system issues
            return render(request, 'base/register.html', {'error': f"Engine Fault: {str(e)}"})
        
    return render(request, 'base/register.html')


def login_user(request):
    if request.method == 'POST':
        u = request.POST.get('username')
        p = request.POST.get('password')

        user = authenticate(request, username=u, password=p)

        if user is not None:
            login(request, user)
            messages.success(request, "Loggedin Successfully!")
            return redirect('home')
        else:
            return render(request, 'base/login.html', {'error': "Invalid AUTH_KEY or AUTH_ID."})
        
    return render(request, 'base/login.html')


def logout_user(request):
    logout(request)
    return redirect('login')


# base/home page view :
def home(request):
    
    return render(request, 'base/home.html', context)

# view for opening new account ->
def new_account(request):
    
    return render(request, 'base/new_account.html')
