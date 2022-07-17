from django.db import models
from . import four_chan

class Word(models.Model):
    name = models.CharField(max_length=5, default='stern',)
# Create your models here.

class Page:
    def __init__(self, html):
        self.html = html


p = Page(four_chan.html)
