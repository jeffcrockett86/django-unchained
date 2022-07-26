from django.shortcuts import render
from django.http import HttpResponse
from boards.models import Post 
from boards.models import User
import requests
# d = {'posts': Post.objects.all()}

def index(request):
    post = rand(Post.objects.all())
    # return HttpResponse(f'<h1>{post.author} {post.time} {post.name} {post.content}</h1>')
    return render(request, 'index.html', {'posts': Post.objects.all()})

def test(request):
    return render(request, 'test.html', {'numbers': [1,2,3,4,5,6,7,8,9,10],
    'html': requests.get('https://www.google.com').text},)