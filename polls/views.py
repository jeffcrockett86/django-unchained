from . import css
from django.shortcuts import render
from django.http import HttpResponse
import requests
from . import reddit
from . import my_html
from . import wordle_alpha
from . import bootstrap
from . import four_chan
# import re
# from . import css
import sys
from . import ed_harris

words = wordle_alpha.words

underscore = '_'
def index(request):
    html = requests.get(f'https://en.wikipedia.org/wiki/Kevin_Bacon').text
    html = html.replace(html, reddit.my_html)
    return HttpResponse(html)

def index2(request):
    print(request)
    return HttpResponse(['<h1>' + word + '</h1>' for word in words])
# Create your views here.
t = requests.get(f'https://google.com').text

def index3(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def index4(request):
    html = requests.get('https://www.nytimes.com/games/wordle/index.html').text
    return HttpResponse(html)

def index5(request):
    html = requests.get('https://www.imdb.com/name/nm0000102/?ref_=fn_al_nm_1').text
    html = html.replace('Kevin Bacon', 'KEVIN_BACON')
    print(request)
    return HttpResponse(html)

def index6(request):
    html = requests.get('https://www.imdb.com/name/nm0000102/?ref_=fn_al_nm_1').text

    # html = html.replace('Kevin Hamm', 'Thank you for selecting Kevin Bacon! Did you know what he was in <a href="imdb/Apollo_13>Apollo 13?</a>')
    html = html.replace('<span class="itemprop">Kevin Bacon</span>', '<span class="itemprop">Thank you for choosing Kevin Bacon!</span>')
    html = html.replace('<span class="itemprop">Thank you for choosing Kevin Bacon!</span>', ' <span class="itemprop">Thank you for choosing Kevin Bacon!</span><br><br><a href="imdb/Apollo_13">Click here to continue.</a>'),
    return HttpResponse(html)

def index7(request):
    html = requests.get('https://www.imdb.com/title/tt0112384/?ref_=fn_al_tt_1').text
    return HttpResponse(html)

def index8(request):
    html = requests.get('https://www.imdb.com/name/nm0000438/?ref_=fn_al_nm_1').text

    html = html.replace('Ed Harris', 'Kevin Bacon was in Apollo 13 with Ed Harris')
    return HttpResponse(html)

def index9(request):
    html = requests.get('https://www.reddit.com').text
    html = html.replace('Reddit', 'Jeffit')
    return HttpResponse(html)

def index10(request):
    html = requests.get('https://www.imdb.com/name/nm0000438/?ref_=fn_al_nm_1').text
    html = html.replace('<a href="/title/tt0475784/">Westworld</a>', '<h1>TESTING</h1>' )
    return HttpResponse(html)

def kevin_bacon(request):
    html = requests.get('https://en.wikipedia.org/wiki/Kevin_Bacon').text
    html = html.replace(html, my_html.k)
    return HttpResponse(html)

def chan4(request):
    html = requests.get('https://boards.4channel.org/g/thread/87761950').text
    return HttpResponse(four_chan.html)

def chan4_b(request):
    return HttpResponse(four_chan.html)

def chan4_v(request):
    return HttpResponse(requests.get('https://boards.4channel.org/v/').text)

def chan4_biz(request):
    return HttpResponse(requests.get('https://boards.4channel.org/biz/').text)

def chan4_x(request):
    return HttpResponse(requests.get('https://boards.4channel.org/x/').text)

def chan4_sci(request):
    return HttpResponse(requests.get('https://boards.4channel.org/sci/').text)


def chan4_xs(request):
    return HttpResponse(requests.get('https://boards.4channel.org/xs/').text)
