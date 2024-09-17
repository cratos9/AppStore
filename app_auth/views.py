from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from .form import loginForm, RegisterForm
from .models import User

def index(request):
    return render(request,"auth/index.html")

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email = email)
                if check_password(password, user.password):
                    print("acceso permitido")
                else:
                    print("contrasena incorrecta")
            except:
                print("el usuario no existe")
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
            passwordSave = make_password(password)
            newUser = User(user = user, email = email, password = passwordSave)
            newUser.save()
    else:
        form = RegisterForm()
    return render(request,"auth/register.html",{'form':form})