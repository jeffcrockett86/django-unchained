from django.shortcuts import render
from django.http import HttpResponse
from boards.models import Post 
from boards.models import *
import requests
# d = {'posts': Post.objects.all()}

users = User.objects.all()
posts = Post.objects.all()
user = users[0]
user2 = users[1]
userposts = [user.posts for user in users]

"""
to do list:
make Comment class 
add 5 comments to each of the posts on index.html
make a user in the database other than numquam
add navbar to bottom of index.html
"""

def index(request):
    # return HttpResponse(f'<h1>{post.author} {post.time} {post.name} {post.content}</h1>')
    return render(request, 'index.html', {'numbers': [1,2,3,4,5,6,7,8,9,10],
    'html': requests.get('https://www.google.com').text,
    'colors': ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    'response': HttpResponse('<h1>Hello, World!</h1>'),
    'users': users,
    'posts': posts,
    'user': u,
    'user2': u2,
    'userposts': userposts,

    })

def test(request):
    # return HttpResponse(f'<h1>{post.author} {post.time} {post.name} {post.content}</h1>')
    return render(request, 'test.html', {'numbers': [1,2,3,4,5,6,7,8,9,10],
    'html': requests.get('https://www.google.com').text,
    'colors': ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    'response': HttpResponse('<h1>Hello, World!</h1>'),
    'users': users,
    'posts': posts,
    'user': user,
    'user2': user2,
    'userposts': userposts
    })