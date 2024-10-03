from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100, null=False)
    desc = models.TextField(max_length=300, null=False,)