from django.urls import path
from . import views
from random import randint as ri

random_url = str(ri(1000000, 2000000))
underscore = '_'
urlpatterns = [path('', views.index, name='index'),
]