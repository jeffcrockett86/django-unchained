from django.shortcuts import render
from django.http import HttpResponse
from random import randint as ri 
import requests
# from . import output_file as o
from . import diagram as the
from . import models as m



def p(request):
    html = ''
    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for prep in m.sorted_prepositions[:1000]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]}; transform: rotate({ri(0, 180)})">' + prep
        div_count += 1
    html += '</div>' * div_count
    return HttpResponse(html)
    # url = str(request).split('/')

def n(request):
    html = ''
    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for noun in m.sorted_nouns[:1000]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]};">' + noun
        div_count += 1
    html += '</div>' * div_count
    return HttpResponse(html)


def v(request):
    html = ''
    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for verb in m.sorted_verbs[:1000]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]};">' + verb
        div_count += 1
    html += '</div>' * div_count
    return HttpResponse(html)


def adj(request):
    html = ''
    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for adj in m.sorted_adjectives[:1000]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]};">' + adj
        div_count += 1
    html += '</div>' * div_count
    return HttpResponse(html)

def adv(request):
    html = ''
    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for adv in m.sorted_adverbs[:1000]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]};">' + adj
        div_count += 1
    html += '</div>' * div_count
    return HttpResponse(html)
    # url = str(request).split('/')
    # li= '<li>'
    # _li = '</li>'
    # h1 = '<h1>'
    # _h1 = '</h1>'
    # print('request url is', url)
    # return HttpResponse('<h1>' + models.Noun('DOG').spelling + '</h1>')
    # return HttpResponse(str([h1 + child + _h1 for child in the_big_dog.children]).replace(r't', '69'))
    # return HttpResponse(f'<h1>Hello, World!</h1><h1><ul>{str([li1 + child.spelling + li2 for child in a.children]).replace('asdf', '')}<ul></h1>')

# def without(request):
#     url = str(request).split('/')
#     if 'Not Found' in url:
#         return index(request, url)
