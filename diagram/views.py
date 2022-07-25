from django.shortcuts import render
from django.http import HttpResponse
from random import randint as ri 
import requests
# from . import output_file as o
from . import diagram as the
from . import models as m

STACK_OVERFLOW_CSS = '''
.image {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 120px;
    height: 120px;
    margin:-60px 0 0 -60px;
    -webkit-animation:spin 4s linear infinite;
    -moz-animation:spin 4s linear infinite;
    animation:spin 4s linear infinite;
}
@-moz-keyframes spin { 
    100% { -moz-transform: rotate(360deg); } 
}
@-webkit-keyframes spin { 
    100% { -webkit-transform: rotate(360deg); } 
}
@keyframes spin { 
    100% { 
        -webkit-transform: rotate(360deg); 
        transform:rotate(360deg); 
    } 
}
'''

style = '''  <body style="text-align: center;
    color: aliceblue;
    font-family: monospace;
    text-align: center;
    color: aliceblue;
    font-family: monospace;
" >
  '''

spin_style = '''
position: absolute;
    top: 50%;
    left: 50%;
    width: 120px;
    height: 120px
px
;
    margin: -60px 0 0 -60px;
    -webkit-animation: spin 4s linear infinite;
    -moz-animation: spin 4s linear infinite;
    animation: spin 4s linear infinite;
'''

def index(request):
    return HttpResponse('<h1>Hello, World!</h1>')

def p(request):
    html = ''
    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for prep in m.d['prepositions'][:25]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]}; transform: rotate({ri(0, 180)})">' + m.rand(m.b)[0]
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
    for adj in m.d['adjectives'][:25]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]};">' + adj.spelling
        div_count += 1
    html += '</div>' * div_count
    return HttpResponse(style + html + '</body>')

def adv(request):
    html = ''
    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for adv in m.d['adverbs'][:25]:
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

def spin(request):
    html = f'<body style={spin_style}'
    div_count = 0
    colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
    for adv in m.d['adverbs'][:25]:
        html += f'<div style="background: {colors[ri(0, len(colors)-1)]};">' + adv.spelling
        div_count += 1
    html += '</div>' * div_count
    return HttpResponse(html + '</body>')