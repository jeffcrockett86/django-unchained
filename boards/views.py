from django.shortcuts import render
from django.http import HttpResponse
from boards.models import *
from boards.models import rand

# d = {'posts': Post.objects.all()}

def index(request):
    post = rand(Post.objects.all())
    # return HttpResponse(f'<h1>{post.author} {post.time} {post.name} {post.content}</h1>')
    return render(request, 'index.html', {'posts': Post.objects.all()[:25]})

def user(request):
    _user = User.objects.get(id=37)
    http_response = HttpResponse('I"m the HTTP response!"') 
    return render(request, 'user.html', {'user': _user, 
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

    
    '''

    })