from django.shortcuts import render
from django.http import HttpResponse
from boards.models import Post 
from boards.models import User
import requests
# d = {'posts': Post.objects.all()}

users = User.objects.all()
posts = Post.objects.all()
user = users[0]
user2 = users[1]
userposts = [user.posts for user in users]

def index(request):
    # return HttpResponse(f'<h1>{post.author} {post.time} {post.name} {post.content}</h1>')
    return render(request, 'index.html', {'numbers': [1,2,3,4,5,6,7,8,9,10],
    'html': requests.get('https://www.google.com').text,
    'colors': ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'],
    'response': HttpResponse('<h1>Hello, World!</h1>'),
    'users': users,
    'posts': posts,
    'user': user,
    'user2': user2,
    'userposts': userposts
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