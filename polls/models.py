from django.db import models

class Word(models.Model):
    name = models.CharField(max_length=5, default='stern',)
# Create your models here.
