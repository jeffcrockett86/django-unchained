from django.shortcuts import render
from django.http import HttpResponse
from boards.models import *
from boards.models import rand
import requests

# d = {'posts': Post.objects.all()}

def index(request):
    post = rand(Post.objects.all())
    # return HttpResponse(f'<h1>{post.author} {post.time} {post.name} {post.content}</h1>')
    return render(request, 'index.html', {'posts': Post.objects.all()[:25]})

def user(request):
    _user = User.objects.get(id=37)
    _user2 = User.objects.get(id=38)
    http_response = HttpResponse('I"m the HTTP response!"') 
    return render(request, 'user.html', {'user': _user,
    'user2': _user2, 
    'posttitles': [post.title for post in _user.posts],
    'postauthors': [post.author for post in _user.posts],
    'postcontents': [post.content for post in _user.posts],
    'request': request,
    'numbers': [num for num in range(100)],
    'colors': ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    'pictures': [],
    'alphanum': ALPHANUM,
    'numquam': u,
    'spacer': '''
    
    ___________________________________________________________


    ''',
    'kevin_bacon': requests.get('https://en.wikipedia.org').text,
    'str_request': ' '.join(str(request).split('/')),
    'split_str_request': str(request).split('/')

    })

def test_a(request):
    return render(request, 'test.html', {'numbers': [1,2,3,4,5,6,7,8,9,10]})

def user2(request):
    return render(request, 'user2.html', {'user': u,
    'request': request,
    'numbers': [num for num in range(100)],
    'colors': ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    'spacer': '''
        
    ___________________________________________________________


    ''',
    'kevin_bacon': requests.get('https://en.wikipedia.org').text,
    'str_request': ' '.join(str(request).split('/')),
    'split_str_request': str(request).split('/')

    })

