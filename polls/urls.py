from django.urls import path
from . import views
from random import randint as ri

random_url = str(ri(1000000, 2000000))
underscore = '_'
urlpatterns = [path('', views.index, name='index'),
    path('wiki/', views.index, name='index2'),
    path("wiki/Philadelphia,_Pennsylvania", views.index3, name='index3'),
    path('wordle/', views.index4, name='index4'),
    path('5/', views.index5, name='index5'),
    # path(f'imdb/Kevin_Bacon/', views.index6, name='index6'),
    path(f'imdb/Apollo_13/', views.index7, name='index7'),
    path(f'imdb/Ed_Harris/', views.index8, name='index8'),
    path(f'jeffit/', views.index9, name='index9'),
    path('imdb/Kevin_Bacon/imdb/Apollo_13', views.index8, name="kevin-bacon-apollo-13"),
    path('imdb/Kevin_Bacon/imdb/Apollo_13/Ed_Harris', views.index10, name="kevin-bacon-apollo-13-ed-harris"),
    path('imdb/Kevin_Bacon/', views.kevin_bacon, name="kevin-bacon"),
    path('4chan/', views.chan4, name="4chan"),
    path('4chan/b/', views.chan4_b, name="4chanb"),
    path('4chan/biz/', views.chan4_biz, name="4chanbiz"),
    path('4chan/x/', views.chan4_x, name="4chanx"),
    path('4chan/sci/', views.chan4_sci, name="4chansci"),
    path('4chan/xs/', views.chan4_xs, name="4chanxs"),
    path('4chan/v/', views.chan4_v, name="4chanv"),
    path('4chan/vrpg/', views.chan4_vrpg, name="4chanvrpg"),
    path('shitposting/', views.shitposting, name="shitposting"),
    path('truth_social/', views.truth_social, name="truth_social"),

]
