from django.shortcuts import render
from django.http import HttpResponse
from boards.models import *
# from boards.models import rand
import requests

# d = {'posts': Post.objects.all()}

def index(request):
    # return HttpResponse(f'<h1>{post.author} {post.time} {post.name} {post.content}</h1>')
    return render(request, 'index.html', {'posts': first_10_posts, 
        'userlist': user_list[:10],
        'user': user_list[0],
        'numbers': [num for num in range(1, 11)],
     
    })
   
def user(request):
    print(str(request).split('/'))
    posts = [post for post in Post.objects.all() if post.author == str(request).split('/')[-2]]
    return render(request, 'user.html', {'posts': posts})

def user1(request):
    print(str(request).split('/'))
    return render(request, 'user1.html', {'user': user_list[0],
    'user_list': user_list,
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




def user2(request):
    print(str(request).split('/'))
    return render(request, 'user2.html', {'user': user_list[1],
    'user_list': user_list,
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
    return render(request, 'user3.html', {'user': user_list[2],
    'user_list': user_list,
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

def user4(request):
    print(str(request).split('/'))
    return render(request, 'user4.html', {'user': user_list[3],
    'user_list': user_list,
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

def user5(request):
    print(str(request).split('/'))
    return render(request, 'user5.html', {'user': user_list[4],
    'user_list': user_list,
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

def user6(request):
    print(str(request).split('/'))
    return render(request, 'user6.html', {'user': user_list[5],
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

def user7(request):
    print(str(request).split('/'))
    return render(request, 'user7.html', {'user': user_list[6],
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

def tree(request):
    return render(request, 'tree.html', {'user': user_list[0]})

def user8(request):
    print(str(request).split('/'))
    return render(request, 'user8.html', {'user': user_list[7],
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

def user9(request):
    print(str(request).split('/'))
    return render(request, 'user9.html', {'user': user_list[8],
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

def user10(request):
    print(str(request).split('/'))
    return render(request, 'user10.html', {'user': user_list[9],
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


def one(request):
    return render(request, 'tree.html', {'user': user_list[0]})

def two(request):
    return render(request, 'tree.html', {'user': user_list[1]})

def three(request):
    return render(request, 'tree.html', {'user': user_list[2]})

def four(request):
    return render(request, 'tree.html', {'user': user_list[3]})

def five(request):
    return render(request, 'tree.html', {'user': user_list[4]})

def six(request):
    return render(request, 'tree.html', {'user': user_list[5]})

def seven(request):
    return render(request, 'tree.html', {'user': user_list[6]})

def eight(request):
    return render(request, 'tree.html', {'user': user_list[7]})

def nine(request):
    return render(request, 'tree.html', {'user':user_list[8] })

def ten(request):
    return render(request, 'tree.html', {'user': user_list[9]})

def eleven(request):
    return render(request, 'tree.html', {'user': user_list[10]})

def twelve(request):
    return render(request, 'tree.html', {'user': user_list[11]})

def thirteen(request):
    return render(request, 'tree.html', {'user': user_list[12]})

def fourteen(request):
    return render(request, 'tree.html', {'user': user_list[13]})

def fifteen(request):
    return render(request, 'tree.html', {'user': user_list[14]})

def sixteen(request):
    return render(request, 'tree.html', {'user': user_list[15]})

def seventeen(request):
    return render(request, 'tree.html', {'user': user_list[16]})

def eighteen(request):
    return render(request, 'tree.html', {'user': user_list[17]})

def nineteen(request):
    return render(request, 'tree.html', {'user': user_list[18]})

def twenty(request):
    return render(request, 'tree.html', {'user': user_list[19]})

def twenty_one(request):
    return render(request, 'tree.html', {'user': user_list[20]})

def twenty_two(request):
    return render(request, 'tree.html', {'user': user_list[21]})

def twenty_three(request):
    return render(request, 'tree.html', {'user': user_list[22]})

def twenty_four(request):
    return render(request, 'tree.html', {'user': user_list[23]})

def page1(request):
    url = str(request).split('/')

    return render(request, 'index.html', {'posts': Post.objects.all()[:10],
    'html': f'''
      
  <button class="btn btn-secondary dropdown-toggle" type="button" id="dropdownMenuButton" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
    Dropdown button
  </button>
  <div class="dropdown-menu" aria-labelledby="dropdownMenuButton">
    <a href="1/" href="#">Action</a>
    <a class="dropdown-item" href="#">Another action</a>
    <a class="dropdown-item" href="#">Something else here</a>
  </div>

    ''',
    'numbers': [1,2,3,4,5,6,7,8,9,10],
    'url': url
    
    })

def page2(request):
    url = str(request).split('/')

    return render(request, 'index.html', {'posts' : Post.objects.all()[10:20],
        'numbers': [1,2,3,4,5,6,7,8,9,10],
})

def page3(request):
    url = str(request).split('/')

    return render(request, 'index.html', {'posts' : Post.objects.all()[20:30],
        'numbers': [1,2,3,4,5,6,7,8,9,10],
})

def page4(request):
    url = str(request).split('/')

    return render(request, 'index.html', {'posts' : Post.objects.all()[30:40],
        'numbers': [1,2,3,4,5,6,7,8,9,10],
})

def page5(request):
    url = str(request).split('/')

    return render(request, 'index.html', {'posts' : Post.objects.all()[40:50],
        'numbers': [1,2,3,4,5,6,7,8,9,10],
})

def page6(request):
    url = str(request).split('/')

    return render(request, 'index.html', {'posts' : Post.objects.all()[50:60],
        'numbers': [1,2,3,4,5,6,7,8,9,10],
})

def page7(request):
    return render(request, 'index.html', {'posts' : Post.objects.all()[60:70],
        'numbers': [1,2,3,4,5,6,7,8,9,10],
})

def page8(request):
    url = str(request).split('/')

    return render(request, 'index.html', {'posts' : Post.objects.all()[70:80],
        'numbers': [1,2,3,4,5,6,7,8,9,10],
})

def page9(request):
    url = str(request).split('/')
    return render(request, 'index.html', {'posts' : Post.objects.all()[80:90],
        'numbers': [1,2,3,4,5,6,7,8,9,10],
})

def page10(request):
    url = str(request).split('/')
    return render(request, 'index.html', {'posts' : Post.objects.all()[90:100],
        'numbers': [1,2,3,4,5,6,7,8,9,10],
    })