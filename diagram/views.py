from django.shortcuts import render
from django.http import HttpResponse
from random import randint as ri 
import requests
# from . import output_file as o
from . import diagram as the
from . import models as m

style = '''  <body style="text-align: center;
    color: aliceblue;
    font-family: monospace;
    text-align: center;
    color: aliceblue;
    font-family: monospace;
" >
  '''

def p(request):
    html = ''
    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for prep in m.sorted_prepositions[:1000]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]}; transform: rotate({ri(0, 180)})">' + prep
        div_count += 1
    html += '</div>' * div_count
    return HttpResponse(style + html + '</body>')
    # url = str(request).split('/')

def n(request):
    html =  '' 

    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for noun in m.d['nouns'][:25]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]};" onclick="console.log(this)">' + noun.spelling
        div_count += 1
    html += '</div>' * div_count
    html += '</body>'
    return HttpResponse(style + html + '</body>')


def v(request):
    html = ''
    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for verb in m.d['verbs'][:25]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]};">' + verb.spelling
        div_count += 1
    html += '</div>' * div_count
    return HttpResponse(style + html + '</body>')


def adj(request):
    html = ''
    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for adj in m.d['adjectives'][:1000]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]};">' + adj.spelling
        div_count += 1
    html += '</div>' * div_count
    return HttpResponse(style + html + '</body>')

def adv(request):
    html = ''
    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for adv in m.d['adverbs'][:1000]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]};">' + adv.spelling
        div_count += 1
    html += '</div>' * div_count
    return HttpResponse(style + html + '</body>')

def b(request):
    return HttpResponse(f'<h1>{m.b[ri(0, len(m.b))]}</h1>')


def q(request):
    return HttpResponse(f'<h1> {m.q[ri(0, len(m.q))]}</h1>')

def s(request):
    return HttpResponse(f'<h1>{m.s.children[0].children[0].spelling}</h1>')
