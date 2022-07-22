from django.shortcuts import render
from django.http import HttpResponse
import requests
from . import output_file as o 




def index(request):
    a = o.s.Article('the')
    return HttpResponse(f'<h1>Hello, World!</h1><h1>{a.spelling}</h1>')
