from django.urls import path
from . import views
from random import randint as ri

urlpatterns = [path('', views.index, name='index'),
path('user/', views.user, name="user"),
path('test/', views.test, name="test")

]