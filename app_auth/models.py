from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    addres = models.CharField(max_length=255, null=True, blank=True)
    
    def _repr_(self):
        return f'<User: {self.user}>'