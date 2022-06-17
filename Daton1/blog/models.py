from cgitb import text
from turtle import title
from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=200)
    text=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    created_date=models.DateTimeField(auto_now_add=True)
    published_date=models.DateTimeField(auto_now_add=True)
