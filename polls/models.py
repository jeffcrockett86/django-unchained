from django.db import models
from django.utils import timezone 
# from . import four_chan

# class Page(models.Model):
#     html = models.TextField(max_length=10000000000)

# class Thread(models.Model):
#     pass

class Product(models.Model):
    title = models.TextField(default="title goes here")
    description = models.TextField("description goes here")
    price = models.TextField("price goes here")
    summary = models.TextField(default='summary goes here')

class Post(models.Model):
    number = models.IntegerField(default=69)
    content = models.TextField(default="post content goes here")
    time = models.DateTimeField(default=timezone.now())
    image = models.CharField(max_length=100, default="image link")

# class Word(models.Model):
#     name = models.CharField(max_length=5, default='stern',)
# Create your models here.

# class Page:
#     def __init__(self, html):
#         self.html = html


# p = Page(four_chan.html)
