from django.urls import path
from . import views
from random import randint as ri

urlpatterns = [path('', views.index, name='index'),
# path('user/', views.user2, name="user"),
path('page/1', views.user1, name="user1"),
path('page/2', views.user2, name="user2"),
path('page/3', views.user3, name="user3"),
path('page/4', views.user4, name="user4"),
path('page/5', views.user5, name="user5"),
path('page/6', views.user6, name="user6"),
path('page/7', views.user7, name="user7"),
path('page/8', views.user8, name="user8"),
path('page/9', views.user9, name="user9"),
path('page/10', views.user10, name="user10"),

]