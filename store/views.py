from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .form import PostForm
from app_auth.models import User
from .models import Post, Favorite

@login_required
def profile(request):
    favorite = Favorite.objects.filter(user = request.user).values_list('product', flat=True)
    product = Post.objects.filter(id__in=favorite)
    favorite_products_dict = {
    product.id: {
        'title': product.title,
        'price': product.price,
        'desc': product.desc,
        'image': product.image.url if product.image else '',
        'created_at': product.created_at,
        'author' : product.author
    }
    for product in product
    }
    context = {
    'favorite_products': favorite_products_dict
    }
    return render(request,"store/profile.html",context)

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

@login_required
def favorite(request, id):
    user = request.user
    product = get_object_or_404(Post, id = id)
    favorite = Favorite.objects.filter(user=user, product=product).first()

    if favorite:
        favorite.delete()
    else:
        Favorite.objects.create(user=user, product=product)
    return redirect('index')