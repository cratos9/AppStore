from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('sell/', views.sell, name='sell'),
    path('favorite/<int:id>', views.favorite, name='favorite')
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)