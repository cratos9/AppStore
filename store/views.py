from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .form import PostForm
from app_auth.models import User
from .models import Post

@login_required
def profile(request):
    return render(request,"store/profile.html")

@login_required
def sell(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data['title']
            desc = form.cleaned_data['desc']
            price = form.cleaned_data['price']
            photo = form.cleaned_data['photo']
            author = User.objects.get(user=request.session.get('user'))
            newPost = Post(title = title, desc = desc, price = price, author = author, image = photo)
            newPost.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request,"store/sell.html",{'form':form})