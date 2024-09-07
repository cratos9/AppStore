from django.shortcuts import render

def index(request):
    saludo={'clave':'valor'}
    return render(request,"auth/index.html", saludo)