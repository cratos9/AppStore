from django.shortcuts import render
from .form import loginForm

def index(request):
    saludo={'clave':'valor'}
    return render(request,"auth/index.html", saludo)

def login(request):
    if request.method == 'POST':
        form = loginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
    else:
        form = loginForm()
    return render(request,"auth/login.html",{'form':form})