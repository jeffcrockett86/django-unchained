from django.shortcuts import render
from django.http import HttpResponse
import requests

def index(request):
    return HttpResponse(requests.get('https://en.wikipedia.org/wiki/Wikipedia').text)
# Create your views here.
