from django.db import models
from app_auth.models import User

class Post(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, editable=False, null=False, db_index=True)
    title = models.CharField(max_length=100, null=False)
    desc = models.TextField(max_length=300, null=False)
    price = models.FloatField(null=False, default=100)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    author = models.ForeignKey(to=User,on_delete=models.CASCADE, null=False)
    image = models.ImageField(upload_to='products/', default="Imagen")
    
    def _repr_(self):
        return f'<User: {self.title}>'