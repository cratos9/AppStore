from django.shortcuts import render, redirect

def profile(request):
    return render(request,"store/profile.html")

def sell(request):
    return render(request,"store/sell.html")