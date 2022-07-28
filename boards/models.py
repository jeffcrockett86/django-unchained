from django.db import models
import datetime
import lorem #used to seed db with autogenerated content
from random import randint as ri

# kevin_bacon_movies = ['https://en.wikipedia.org/wiki/Animal_House', 'https://en.wikipedia.org/wiki/Starting_Over_(1979_film)', 
# 'https://en.wikipedia.org/wiki/Hero_at_Large', 'https://en.wikipedia.org/wiki/Friday_the_13th_(1980_film)', 
# 'https://en.wikipedia.org/wiki/Only_When_I_Laugh_(film)', 'https://en.wikipedia.org/wiki/Diner_(1982_film)', 
# 'https://en.wikipedia.org/wiki/Forty_Deuce', 'https://en.wikipedia.org/wiki/Enormous_Changes_at_the_Last_Minute', 
# 'https://en.wikipedia.org/wiki/Footloose_(1984_film)', 'https://en.wikipedia.org/wiki/Quicksilver_(film)', 
# 'https://en.wikipedia.org/wiki/White_Water_Summer', 'https://en.wikipedia.org/wiki/End_of_the_Line_(1987_film)', 
# 'https://en.wikipedia.org/wiki/Planes,_Trains_and_Automobiles', 
# 'https://en.wikipedia.org/wiki/She%27s_Having_a_Baby', 'https://en.wikipedia.org/wiki/Criminal_Law_(film)', 
# 'https://en.wikipedia.org/wiki/The_Big_Picture_(1989_film)', 'https://en.wikipedia.org/wiki/Tremors_(1990_film)', 
# 'https://en.wikipedia.org/wiki/Flatliners', 'https://en.wikipedia.org/wiki/Pyrates', 'https://en.wikipedia.org/wiki/Queens_Logic', 
# 'https://en.wikipedia.org/wiki/He_Said,_She_Said_(film)', 'https://en.wikipedia.org/wiki/JFK_(film)', 'https://en.wikipedia.org/wiki/A_Little_Vicious', 
# 'https://en.wikipedia.org/wiki/A_Few_Good_Men', 'https://en.wikipedia.org/wiki/The_Air_Up_There', 'https://en.wikipedia.org/wiki/The_River_Wild', 
# 'https://en.wikipedia.org/wiki/New_York_Skyride', 'https://en.wikipedia.org/wiki/Murder_in_the_First_(film)', 'https://en.wikipedia.org/wiki/Apollo_13_(film)', 
# 'https://en.wikipedia.org/wiki/Balto_(film)', 'https://en.wikipedia.org/wiki/Sleepers', 'https://en.wikipedia.org/wiki/Picture_Perfect_(1997_film)', 
# 'https://en.wikipedia.org/wiki/Destination_Anywhere_(film)', 'https://en.wikipedia.org/wiki/Digging_to_China', 'https://en.wikipedia.org/wiki/Telling_Lies_in_America', 
# 'https://en.wikipedia.org/wiki/Wild_Things_(film)', 'https://en.wikipedia.org/wiki/Stir_of_Echoes', 'https://en.wikipedia.org/wiki/My_Dog_Skip_(film)', 
# 'https://en.wikipedia.org/wiki/We_Married_Margo', 'https://en.wikipedia.org/wiki/Hollow_Man', 'https://en.wikipedia.org/wiki/Novocaine_(film)', 
# 'https://en.wikipedia.org/wiki/Trapped_(2002_film)', 'https://en.wikipedia.org/wiki/Mystic_River_(film)', 'https://en.wikipedia.org/wiki/In_the_Cut_(film)', 
# 'https://en.wikipedia.org/wiki/The_Woodsman_(2004_film)', 'https://en.wikipedia.org/wiki/Cavedweller_(film)', 
# 'https://en.wikipedia.org/wiki/Loverboy_(2005_film)', 'https://en.wikipedia.org/wiki/Beauty_Shop', 'https://en.wikipedia.org/wiki/Where_the_Truth_Lies', 
# 'https://en.wikipedia.org/wiki/Death_Sentence_(2007_film)', 'https://en.wikipedia.org/wiki/Rails_%26_Ties', 
# 'https://en.wikipedia.org/wiki/Saving_Angelo', 'https://en.wikipedia.org/wiki/The_Air_I_Breathe', 
# 'https://en.wikipedia.org/wiki/Frost/Nixon_(film)', 'https://en.wikipedia.org/wiki/New_York,_I_Love_You', 'https://en.wikipedia.org/wiki/My_One_and_Only_(film)', 
# 'https://en.wikipedia.org/wiki/Beyond_All_Boundaries', 'https://en.wikipedia.org/wiki/Super_(2010_American_film)', 'https://en.wikipedia.org/wiki/Elephant_White', 
# 'https://en.wikipedia.org/wiki/X-Men:_First_Class', 'https://en.wikipedia.org/wiki/Crazy,_Stupid,_Love', 'https://en.wikipedia.org/wiki/Jayne_Mansfield%27s_Car', 
# 'https://en.wikipedia.org/wiki/R.I.P.D.', 'https://en.wikipedia.org/wiki/Skum_Rocks!', 'https://en.wikipedia.org/wiki/Cop_Car_(film)', 'https://en.wikipedia.org/wiki/Black_Mass_(film)',
#  'https://en.wikipedia.org/wiki/The_Darkness_(film)', 'https://en.wikipedia.org/wiki/Patriots_Day_(film)', 'https://en.wikipedia.org/wiki/You_Should_Have_Left', 
#  'https://en.wikipedia.org/wiki/The_Toxic_Avenger_(2022_film)', 'https://en.wikipedia.org/wiki/They/Them', 'https://en.wikipedia.org/wiki/Leave_the_World_Behind_(film)', 'https://en.wikipedia.org/wiki/Search_for_Tomorrow', 
#  'https://en.wikipedia.org/wiki/The_Gift_(1979_film)', 'https://en.wikipedia.org/wiki/Guiding_Light', 'https://en.wikipedia.org/wiki/Mister_Roberts_(1984_film)', 
#  'https://en.wikipedia.org/wiki/American_Playhouse', 'https://en.wikipedia.org/wiki/Lemon_Sky', 'https://en.wikipedia.org/wiki/Saturday_Night_Live', 'https://en.wikipedia.org/wiki/Frasier', 
#  'https://en.wikipedia.org/wiki/God,_the_Devil_and_Bob', 'https://en.wikipedia.org/wiki/Will_%26_Grace', 'https://en.wikipedia.org/wiki/Taking_Chance', 'https://en.wikipedia.org/wiki/The_Magic_7', 
#  'https://en.wikipedia.org/wiki/Bored_to_Death', 'https://en.wikipedia.org/wiki/Robot_Chicken', 'https://en.wikipedia.org/wiki/The_Following', 'https://en.wikipedia.org/wiki/Comedy_Bang!_Bang!_(TV_series)', 
#  'https://en.wikipedia.org/wiki/I_Love_Dick_(TV_series)', 'https://en.wikipedia.org/wiki/Tour_de_Pharmacy', 'https://en.wikipedia.org/wiki/Story_of_a_Girl_(film)', 'https://en.wikipedia.org/wiki/SMILF', 
#  'https://en.wikipedia.org/wiki/City_on_a_Hill_(TV_series)', 'https://en.wikipedia.org/wiki/Live_in_Front_of_a_Studio_Audience', 'https://en.wikipedia.org/wiki/Losing_Chase', 'https://en.wikipedia.org/wiki/Loverboy_(2005_film)', 
#  'https://en.wikipedia.org/wiki/The_Closer', 'https://en.wikipedia.org/wiki/Losing_Chase', 'https://en.wikipedia.org/wiki/Loverboy_(2005_film)']
def rand(lst):
    return lst[ri(0, len(lst)-1)]

ALPHANUM = 'abcdefghijklmnopqrstuvwxyz0123456789'
name = ''

class Post(models.Model):
    author = models.CharField(max_length=25, default="Anonymous")
    title = models.CharField(max_length=144, default="Post Name")
    time = models.DateTimeField(auto_now_add=True, blank=True)
    content = models.CharField(max_length=10000, default="Post Content")
    comments = []

class User(models.Model):
    username = models.CharField(max_length=25, default="Anonymous")
    posts = []

class Comment(models.Model):
    username = None
    author = None
    content = models.CharField(max_length=10000, default="Comment")
    parent = None 
    comments = []


users = User.objects.all()
the_set = set([user.username for user in users])
posts = Post.objects.all()
# first_25 = Post.objects.all()[:25]
# first_10 = Post.objects.all()[:10]
first_10_posts = [Post(title=lorem.sentence(), author=lorem.sentence().split()[0]) for i in range(10)]
# for post in first_10:
#     post.comments = []
#     for i in range(5):
#         post.comments.append(Comment(content=lorem.sentence()))
#         post.comments[-1].parent = post
#         post.save()

# for post in first_10_posts:
#      post.comments = set(list(post.comments))
#      post.save()

user_list = []


for name in set([post.author for post in posts]):
    _u = User.objects.create(username=name)
    user_list.append(_u)
    _u.save()

for user in user_list:
    user.posts = [post for post in posts if post.author == user.username]
    user.save() 


for post in user.posts:
    post.comments = [Comment(content = lorem.sentence()) for i in range(5)]

for post in first_10_posts:
    post.comments = [Comment(content=lorem.sentence()) for i in range(5)]
    post.content = lorem.paragraph()
    post.save()

for post in Post.objects.all()[:200]:
    post.title = lorem.sentence()
    post.content = lorem.paragraph()
    post.comments = [Comment(content=lorem.sentence()) for i in range(5)]

count = 0
# for user in user_list:
#     for post in user.posts:
#         c = Comment(content=lorem.sentence())
#         c.comments.append(Comment(content=lorem.sentence()))
#         c.comments[-1].parent = c
#         c.parent = post
#         post.comments.append(c)
#         count += 1
#         if count==5:
#             break

# for i in range(len(user_list)):
#     user = user_list[i]
#     user.posts = user.posts[:5]


# for i in range(len(user_list)):
#     user = user_list[i]
#     for i in range(len(user.posts)):
#         user.posts[i].comments = user.posts[i].comments[:5]

user_list.append(User(username="u/ohgoshwheretobegin"))

user_list[-1].posts = [Post(author=user_list[1].username, title="Throwaway time! What's your secret that could literally ruin your life if it came out?")]
# posts.append(Post(author='u/ohgoshwheretobegin', title="Throwaway time! What's your secret that could literally ruin your life if it came out?"))

user_list.append(User(username="someguy"))
guy = user_list[-1]
thread = user_list[-2]
thread.posts[0].comments.append(Comment(content="'I'm pretty sure it fucked me up good, honestly. I never really properly appreciated the deep scars sexual abuse leaves on a victim until I looked back on my life with that in mind. I buried it for years and tried to pretend I was normal, but I was definitely different. I was a lot more melancholy, and have had a few streaks of depression. I've never really been too certain of my sexuality. I'm scared to death of sex, honestly, and I think it's because part of me is afraid that I'll wind up just as abusive as he was."))

thread.posts[0].comments.append(Comment(content="Two and a half years ago I was in dire financial straights, so I sold my home to keep my struggling business afloat. I neglected to tell the owners that they have an 800 sq. ft. bunker on the property that I built about seven years ago. The bunker that I've called home since I sold it. The entrance to it is well-hidden, but I still come and go very early/very late in the day."))

thread.posts[0].comments.append(Comment(content='''
I speak two languages so every time I received a new essay I would browse the topic in my own language and translate the text word-by-word to English then submitted it.

No one ever caught me for plagiarism before.
'''
))

thread.posts[0].comments.append(Comment(content='''
I cut off all contact with everyone I know and moved to Kenya, I tell people a fake name and a fake background and have made it appear to my family that I died on boat trip in the Pacific. No I am not joking. I am dead in the United States.
'''
))

thread.posts[0].comments.append(Comment(content='''
I run a cake business. I charge people hundreds for wedding cakes... 
Every last one is made using Pilsbury cake mix I buy for $1 a box at Walmart. 
I suck at baking. Every time I've ever tried to make a cake from scratch it sucked. 
But baking is like.. My whole deal. My friends all call me the cake girl. 
It's like my whole life is a lie. People compliment my cakes all the time. 
Telling me how delicious they are. Telling me it's so much better than box mix cake. 
Telling me they could never bake a cake so delicious. Well guess what? For $1, 
they too can make a cake just as delicious. Just add oil, eggs and water. In my defense, 
I love cake decorating. I make all of the frostings and fondant from scratch. 
I just hate baking fucking cakes!! I base my prices mostly on the decoration of the cakes
 and not of the cake itself of that makes sense. Still... No one knows about this except my husband.
  Even my best friends think I fucking slave over the oven mixing and baking these damn cakes.
   I have been doing this for YEARS. If anyone knew my business and reputation would be in the toilet for sure. 
   :/ I keep telling myself I have to learn how to make the damn cakes without the box mixes, 
   but I never do it. I feel like such a sham sometimes.
'''
))

thread.posts[0].comments = thread.posts[0].comments[-5:]
# z = zip(first_25, [post.comments for post in first_25])
# d = dict(z)
# dict_items = list(d.items())
thread.posts[0].comments.append(Comment(content='''
Ok, so this is a secret I've kept for nearly 20 years.
During the summers when I was growing up, my parents would often leave my brother and I(I'm male) with our aunt and uncle who lived out in the country. It was great as they had 4 sons of ages close to ours so we had a lot of fun doing kids stuff.
One summer when I was 8, the oldest cousin was maybe 16. We somehow got talking and he asked me if I wanted to sleep in his room that night. He has the nicest room and bed so I was all for it. Got into bed and he asked if he could touch my penis. I was 8 and just thought it was ok so I let him. He rubs it for a bit and then asks me to do the same to him. So I do. This progresses and eventually I'm sucking his cock. I think I knew this was wrong so I said I didn't want to carry on. We stop and I goto sleep quite confused.
I wake up and he hands me some money and tells me never to tell anyone about what happened. Next night he tries to do the same thing.. But now all I care about is the money. So I do it. This carried on for 2 summers.
Eventually I got old enough to realize it was quite wrong regardless of the money and stopped.
I've not told anyone this. He's now married with 2 kids. I'm also married and we see them sometimes at family events. I don't have the balls to even try and talk to him about it.. Hell I'm not even sure what I'd say.
I'm sure this will get buried but just getting it off my chest makes me feel better.
Tldr I was a gay child hooker.
'''
))

thread.posts[0].comments.append(Comment(content='''
I once helped out my a female friend's family by taking care of their cat for a week. Every day for a week, 
I would go over there and snoop around their house. I found my friend's diary, and proceeded to read the entire thing. 
I used this information to get her to like me, and she is currently my wife.
'''
))
'''
 Anonymous 07/25/22(Mon)23:29:41 No.606992621   [Reply]▶>>607010219
The first thing I will do when I get this will put my hand in the Goblet of Fire.
+63 replies and 10 images omitted. Click here to view.
'''
