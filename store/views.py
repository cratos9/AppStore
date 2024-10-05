from django.shortcuts import render, redirect
from .form import Post

def profile(request):
    return render(request,"store/profile.html")

def sell(request):
    if request.method == 'POST':
        form = Post(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']
            print(f'{title}, {desc}, {price}, {image}')
    else:
        form = Post()
    return render(request,"store/sell.html",{'form':form})