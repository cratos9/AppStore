from django.shortcuts import render
from .form import loginForm, RegisterForm
from .models import User

def index(request):
    return render(request,"auth/index.html")

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            password = form.cleaned_data['password']
    else:
        form = loginForm()
    return render(request,"auth/login.html",{'form':form})

def Register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            newUser = User(user = user, email = email, password = password)
            newUser.save()
    else:
        form = RegisterForm()
    return render(request,"auth/register.html",{'form':form})