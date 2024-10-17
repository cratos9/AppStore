#Django imports
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#Personal imports
from .form import loginForm, RegisterForm
from .models import User
from store.models import Post

#index route
def index(request):
    products = Post.objects.all()
    return render(request,"auth/index.html", {'products':products})

#Login logic and route
def login_view(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username = email, password = password)
            if user is not None:
                login(request, user)
            else:
                messages.error(request, "La contrasena o usuario son incorrectos")
    else:
        form = loginForm()
    return render(request,"auth/login.html",{'form':form})

#register logic and route
def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            passwordConfirm = form.cleaned_data['passwordConfirm']
            userExist = User.objects.filter(email=email).exists()
            if userExist == False:
                if password != passwordConfirm:
                    messages.error(request, "La contrasena debe ser igual")
                elif password == passwordConfirm:
                    newUser = User.objects.create_user(username=user, email=email, password=password)
                    newUser.save()
                    return redirect("login")
            else:
                messages.error(request, "El usuario ya existe")
    else:
        form = RegisterForm()
    return render(request,"auth/register.html",{'form':form})

def logout_view(request):
    logout(request)
    return redirect('index')