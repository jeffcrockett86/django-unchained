from django.shortcuts import render
from django.http import HttpResponse
import requests
from . import output_file as o 




def index(request):
    the_big_dog = o.ArtP(o.s.Article('the'), o.Adj('big'), o.N('dog'))
    url = str(request).split('/')
    li= '<li>'
    _li = '</li>'
    h1 = '<h1>'
    _h1 = '</h1>'
    print('request is', request)
    return HttpResponse(str([h1 + child.spelling + _h1 for child in the_big_dog.children]).replace(r't', '69'))
    # return HttpResponse(f'<h1>Hello, World!</h1><h1><ul>{str([li1 + child.spelling + li2 for child in a.children]).replace('asdf', '')}<ul></h1>')

# def without(request):
#     url = str(request).split('/')
#     if 'Not Found' in url:
#         return index(request, url)
