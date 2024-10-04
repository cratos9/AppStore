from django.db import models

class User(models.Model):
    id = models.IntegerField(null=False, unique=True, primary_key=True, editable=False,db_index=True )
    user = models.CharField(null=False, editable=True, max_length=50)
    email = models.EmailField(null=False, editable=True, unique=True)
    password = models.CharField(null=False, editable=True, max_length=20)
    
    def _repr_(self):
        return f'<User: {self.user}>'