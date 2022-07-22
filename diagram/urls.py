from django.urls import path
from . import views
from random import randint as ri

random_url = str(ri(1000000, 2000000))
underscore = '_'
urlpatterns = [path('', views.p, name='p'),
path('p/', views.p, name="p"),
path('n/', views.n, name="n"),
path('v/', views.v, name="p"),
path('adj/', views.adj, name="adj"),
path('adv/', views.adv, name="adv"),




]