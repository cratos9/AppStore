#Django imports
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
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
def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email = email)
                if check_password(password, user.password):
                    request.session['user'] = user.user
                    request.session['email'] = user.email
                    request.session['id'] = user.id
                    return redirect('index')
                else:
                    messages.error(request, "El usuario o contrasenas son son incorrectas")
            except:
                messages.error(request, "El usuario o contrasenas son son incorrectas")
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
                    passwordSave = make_password(password)
                    newUser = User(user = user, email = email, password = passwordSave)
                    newUser.save()
                    return redirect("login")
            else:
                messages.error(request, "El usuario ya existe")
    else:
        form = RegisterForm()
    return render(request,"auth/register.html",{'form':form})

def logout(request):
    request.session.flush()
    return redirect('index')