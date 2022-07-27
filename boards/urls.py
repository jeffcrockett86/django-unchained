from django.urls import path
from . import views
from random import randint as ri

urlpatterns = [path('', views.index, name='index'),
# path('user/', views.user2, name="user"),
path('user/', views.user1, name="user1"),
path('user/2', views.user2, name="user2"),
path('user/3', views.user3, name="user3"),
path('user/39', views.user3, name="user3"),
path('test/', views.test_a, name="test_a"),

]