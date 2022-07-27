from django.shortcuts import render
from django.http import HttpResponse
from boards.models import *
from boards.models import rand
import requests

# d = {'posts': Post.objects.all()}

def index(request):
    post = rand(Post.objects.all())
    # return HttpResponse(f'<h1>{post.author} {post.time} {post.name} {post.content}</h1>')
    return render(request, 'index.html', {'posts': first_25, 'numbers': [num for num in range(1, 11)]})

def user1(request):
    print(str(request).split('/'))
    return render(request, 'user1.html', {'user': u,
    'userposts': u.posts,
    'request': request,
    'numbers': [num for num in range(1,11)],
    'colors': ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    'spacer': '''
        
    ___________________________________________________________


    ''',
    'wiki': requests.get('https://en.wikipedia.org').text,
    'str_request': ' '.join(str(request).split('/')),
    'split_str_request': str(request).split('/')

    })



def test_a(request):
    return render(request, 'test.html', {'numbers': [1,2,3,4,5,6,7,8,9,10]})

def user2(request):
    print(str(request).split('/'))
    return render(request, 'user2.html', {'user': u2,
    'userposts': u2.posts,
    'request': request,
    'numbers': [num for num in range(1,11)],
    'colors': ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    'spacer': '''
        
    ___________________________________________________________


    ''',
    'kevin_bacon': requests.get('https://en.wikipedia.org').text,
    'str_request': ' '.join(str(request).split('/')),
    'split_str_request': str(request).split('/')

    })

def user3(request):
    print(str(request).split('/'))
    return render(request, 'user3.html', {'user': u3,
    'userposts': u3.posts,
    'request': request,
    'numbers': [num for num in range(1, 11)],
    'colors': ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    'spacer': '''
        
    ___________________________________________________________


    ''',
    'kevin_bacon': requests.get('https://en.wikipedia.org').text,
    'str_request': ' '.join(str(request).split('/')),
    'split_str_request': str(request).split('/')

    })

def do_something(request):
    return render(request, 'do_something.html', {})