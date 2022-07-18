from . import css
from django.shortcuts import render
from django.http import HttpResponse
import requests
from . import reddit
from . import my_html
from . import wordle_alpha
from . import bootstrap
from . import four_chan
from . import stack_overflow
from . import models as M
import re
# from . import css
import sys
from . import ed_harris
from . import kevin_bacon_html

words = wordle_alpha.words

the_OA = []
# divs = re.findall('<div.\w*="\w*', pol.html)
underscore = '_'
def index(request):
    # html = requests.get(f'https://en.wikipedia.org/wiki/Kevin_Bacon').text
    # html = html.replace(html, reddit.my_html)
    # m = M.Page(html)
    # the_OA.append(m)
    return HttpResponse(kevin_bacon_html.html)

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

def chan4_news(request):
    return HttpResponse(requests.get('https://boards.4channel.org/news/').text)

def chan4_v(request):
    return HttpResponse(requests.get('https://boards.4channel.org/v/').text)

def chan4_vrpg(request):
    return HttpResponse(requests.get('https://boards.4channel.org/vrpg/').text)


def shitposting(request):
    return HttpResponse(requests.get('https://new.reddit.com/r/shitposting/comments/w1aghk/guys_pls_help/').text)

def truth_social(request):
    return HttpResponse(requests.get('https://truthsocial.com/').text)

def stack_overflow(request):
    return HttpResponse(stack_overflow_html.html)

def ph(request):
    return HttpResponse(requests.get('https://www.pornhub.com/').text)

def ph2(request):
    return HttpResponse(requests.get('https://www.pornhub.com/?utm_source=http://127.0.0.1:8000/polls/ph/&utm_medium=redirects&utm_campaign=hotlinkerredirects').text)

def askreddit(request):
    return HttpResponse(requests.get('https://www.reddit.com/r/AskReddit/comments/vjpkye/the_supreme_court_has_overturned_roe_v_wade_how/').text)


def chan4_v2(request):
    return HttpResponse(requests.get('https://boards.4channel.org/v/2').text)

def chan4_v3(request):
    return HttpResponse(requests.get('https://boards.4channel.org/v/3').text)

def chan4_v4(request):
    return HttpResponse(requests.get('https://boards.4channel.org/v/4').text)

def chan4_v5(request):
    return HttpResponse(requests.get('https://boards.4channel.org/v/5').text)

def chan4_v6(request):
    return HttpResponse(requests.get('https://boards.4channel.org/v/6').text)

def chan4_v7(request):
    return HttpResponse(requests.get('https://boards.4channel.org/v/7').text)

def chan4_v8(request):
    return HttpResponse(requests.get('https://boards.4channel.org/v/8').text)

def chan4_v9(request):
    return HttpResponse(requests.get('https://boards.4channel.org/v/9').text)

def movies(request):
    return HttpResponse(requests.get('https://en.wikipedia.org/Kevin_Bacon_filmography').text)

def tutorial(request):
    return HttpResponse(requests.get('https://www.youtube.com/watch?v=F5mRW0jo-U4').text)
