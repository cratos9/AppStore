from django.shortcuts import render, redirect

def profile(request):
    request.session.flush()
    return render(request,"store/profile.html")