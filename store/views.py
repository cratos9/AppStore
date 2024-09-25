from django.shortcuts import render

def index(requrst):
    return render(requrst,"store/index.html")