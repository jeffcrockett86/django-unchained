from django.shortcuts import render
from django.http import HttpResponse
from boards.models import Post
from boards.models import rand

# d = {'posts': Post.objects.all()}

def index(request):
    post = rand(Post.objects.all())
    # return HttpResponse(f'<h1>{post.author} {post.time} {post.name} {post.content}</h1>')
    return render(request, 'index.html', {'posts': Post.objects.all()[:25]})
