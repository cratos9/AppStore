from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.Register, name='register'),
    path('logout/', views.logout, name='logout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)