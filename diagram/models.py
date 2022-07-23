from django.db import models
from random import randint as ri 
from . import nltk_words as nltk_words

class W(models.Model):
  spelling = models.CharField(max_length=100, default="spelling")
  pos = models.CharField(max_length=5, default="part of speech")
  def __init__(self, spelling = spelling, pos = pos):
    self.spelling = spelling 
    self.pos = pos 
    self.children = []

class N(models.Model):
  spelling = models.CharField(max_length = 100, default="spelling")
  pos = models.CharField(max_length=5, default="part of speech")
  def __init__(self, spelling, pos):
    self.spelling = spelling 
    self.pos = pos 
    self.children = []
    

class V(models.Model):
  spelling = models.CharField(max_length = 100)
  pos = models.CharField(max_length=5)
  def __init__(self, spelling=spelling, pos = pos):
    self.spelling = spelling 
    self.pos = pos   
    self.children = []
    

class Adj(models.Model):
  spelling = models.CharField(max_length = 100)
  pos = models.CharField(max_length=5)
  def __init__(self, spelling=spelling, pos = pos):
    self.spelling = spelling 
    self.pos = pos 
    self.children = []
    

class Art(models.Model):
  spelling = models.CharField(max_length = 100)
  pos = models.CharField(max_length=5)
  def __init__(self, spelling=spelling, pos = pos):
    self.spelling = spelling 
    self.pos = pos 
    self.children = []
    

class Adv(models.Model):
  spelling = models.CharField(max_length = 100)
  pos = models.CharField(max_length=5)
  def __init__(self, spelling=spelling, pos = pos):
    self.spelling = spelling 
    self.pos = pos 
    self.children = []

class Prep(models.Model):
  spelling = models.CharField(max_length = 100)
  pos = models.CharField(max_length=5)
  def __init__(self, spelling=spelling, pos = pos):
    self.spelling = spelling 
    self.pos = pos   
    self.children = []
    


class Word:
    def __init__(self, spelling='', pos=''):
        self.spelling = spelling 
        self.children = None
        self.children = []
    

class Noun: 
    def __init__(self, spelling='', pos=''):
        self.pos = 'NOUN'
        self.spelling = spelling 
        self.children = None


class Verb: 
    def __init__(self, spelling='', pos=''):
        self.pos = 'VERB'
        self.spelling = spelling 
        self.children = None
     

class Adjective: 
    def __init__(self, spelling='', pos=''):
        self.pos = 'ADJECTIVE'
        self.spelling = spelling 
        self.children = None


class Adverb:
  def __init__(self, spelling='', pos=''):
    self.pos = 'ADVERB'
    self.spelling = spelling 
    self.children = None

        

class Article: 
    def __init__(self, spelling='', pos=''):
        self.pos = 'ARTICLE'
        self.spelling = spelling 
        self.children = None
    

class Preposition:
    def __init__(self, spelling='', pos=''):
        self.pos = 'PREPOSITION'
        self.spelling = spelling 
        self.children = None

class NounPhrase:  
    def __init__(self, *args):
        self.head = "NOUN"
        # for arg in args:
        #     print(arg)
        self.children = args

class ArticlePhrase:
    def __init__(self, *args):
        self.head = "ARTICLE"

        # for arg in args:
        #     print(arg)
        self.children = args


class VerbPhrase:
    def __init__(self, *args):
        self.head = "VERB"
        # for arg in args:
        #     print(arg)
        self.children = args


class AdverbPhrase:
    def __init__(self, *args):
        self.head = "ADVERB"
        # for arg in args:
        #     print(arg)
        self.children = args

class AdjectivePhrase:
    def __init__(self, *args):
        self.head = "ADJECTIVE"

        # for arg in args:
            # print(arg)
        self.children = args

class PrepositionPhrase:
  def __init__(self, *args):
    self.head = 'PREPOSITION'
    self.children = args

class Sentence:
    def __init__(self, *args):
        self.head = "SENTENCE"

        # for arg in args:
        #     print(arg)
        self.children = args



ap = AdjectivePhrase(Adjective("big"), Noun("dog"))

ap = ArticlePhrase(Article("the"), ap)

lst = [Article("The"), Adjective("red"), Noun("ball")]
# lst
# [<Article object at 0x10646eb30>, <Adjective object at 0x10a017970>, <Noun object at 0x10a017f10>]
the_red_ball = ArticlePhrase(Article("The"), AdjectivePhrase(Adjective("red"), Noun("ball")))
# <Article object at 0x10a017700>
# <Adjective object at 0x10a017dc0>
# <Noun object at 0x10a017fa0>
# the_red_ball
# <output_file.ArticlePhrase object at 0x10a017d90>
_is = Verb("is")
blue = Adjective("blue")

_is_blue = VerbPhrase(_is, blue)

the_red_ball_is_blue = Sentence(the_red_ball, _is_blue)

print(the_red_ball_is_blue)

# NP = NounPhrase
# AdjP = AdjectivePhrase
# ArtP = ArticlePhrase
# S = Sentence
# VP = VerbPhrase
# N = Noun
# V = Verb
# Adj = Adjective
# Art = Article
# PP = PrepositionPhrase

# s = Sentence(Article('the'), AdjectivePhrase(Adjective('little'), NounPhrase(Noun('dog')), VerbPhrase(Verb('runs'))))
# cat = N('cat')

# try:
#    if cat.children:
#      print('cat has children')
# except AttributeError:
#      print('cat has no children')

# b = open('bible.txt', 'r')
# b_lines = b.readlines()
# b_lines = [line.split('\t')[-1].lower().replace(r'[,.:;]', '') for line in b_lines]
lines = nltk_words.nltk_words.split('\n')
# lines = nltk_words.nltk_words.split('\n')
# print(lines)
d = {
  'words': [],
  'nouns': [],
  'verbs': [],
  'adjectives': [],
  'articles': [],
  'prepositions': [],
  'adverbs': [],
}

for line in lines:
    d['words'].append(line)
    if ' NN' in line:
      d['nouns'].append(Noun(line.split()[0]))
    if ' VBZ' in line:
      d['verbs'].append(Verb(line.split()[0]))
    if ' JJ' in line:
      d['adjectives'].append(Adjective(line.split()[0]))
    if ' IN' in line:
      d['prepositions'].append(Preposition(line.split()[0]))
    if ' DT' in line:
      d['articles'].append(Article(line.split()[0]))
    if ' RB' in line:
      d['adverbs'].append(Adverb(line.split()[0]))
  

rand_noun = d['nouns'][ri(0, len(d['nouns']))]
rand_noun2 = d['nouns'][ri(0, len(d['nouns']))]

rand_adj = d['adjectives'][ri(0, len(d['adjectives']))]
rand_adj2 = d['adjectives'][ri(0, len(d['adjectives']))]

rand_verb = d['verbs'][ri(0, len(d['verbs']))]
rand_verb2 = d['verbs'][ri(0, len(d['verbs']))]

rand_prep = d['prepositions'][ri(0, len(d['prepositions']))]
rand_prep2 = d['prepositions'][ri(0, len(d['prepositions']))]

rand_art = d['articles'][ri(0, len(d['articles']))]
rand_art2 = d['articles'][ri(0, len(d['articles']))]

sorted_nouns = sorted([noun.spelling for noun in d['nouns']])
sorted_verbs = sorted([verb.spelling for verb in d['verbs']])
sorted_adjectives = sorted([adj.spelling for adj in d['adjectives']])
sorted_prepositions = sorted([prep.spelling for prep in d['prepositions']])



# print(f'{rand_art.spelling} {rand_adj.spelling} {rand_noun.spelling} {rand_verb.spelling} {rand_prep.spelling} {rand_art2.spelling} {rand_adj2.spelling} {rand_noun2.spelling}')
"""
from output_file import *
Currently feeding Lassie
<Adjective object at 0x10a017310>
<Noun object at 0x10a017370>
<Article object at 0x10a017430>
<output_file.AdjPhrase object at 0x10a0173d0>
ap
<output_file.ArticlePhrase object at 0x10a017490>
ap.children
(<Article object at 0x10a017430>, <output_file.AdjPhrase object at 0x10a0173d0>)
ap.children[0]
<Article object at 0x10a017430>
ap.children[0].spelling
'the'
the = ap.children[0]
the = the.spelling
the
'the'
ap = AdjPhrase(Adjective("big"), Noun("dog"))
<Adjective object at 0x10646e0b0>
<Noun object at 0x10a017880>
ap.children
(<Adjective object at 0x10646e0b0>, <Noun object at 0x10a017880>)
big = ap.children[0].spelling
big = ap.children[1].spelling
big = ap.children[0]
dog = ap.children[1]
dog
<Noun object at 0x10a017880>
the_big_dog
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'the_big_dog' is not defined
big_dog
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'big_dog' is not defined
big_dog = AdjPhrase(big, dog)
<Adjective object at 0x10646e0b0>
<Noun object at 0x10a017880>
the_big_dog = ArticlePhrase(Article("the"), big_dog)
<Article object at 0x10a017a90>
<output_file.AdjPhrase object at 0x10a017a00>


class Sentence:
   def __init__(self, *args):
     self.children = args
 
the_big_dog_runs = Sentence(the_big_dog, VerbPhrase("runs"))
runs
the_big_dog_runs
<__main__.Sentence object at 0x10a017d00>
the_big_dog_runchildren
(<output_file.ArticlePhrase object at 0x10a017670>, <output_file.VerbPhrase object at 0x10a017ca0>)

            
"""
"""
 np
<output_file.NounPhrase object at 0x113d1b340>
 ap = ArticlePhrase(Article('the'), np))
  File "<stdin>", line 1
    ap = ArticlePhrase(Article('the'), np))
                                          ^
SyntaxError: unmatched ')'
 ap = ArticlePhrase(Article('the'), np)
 ap
<__main__.ArticlePhrase object at 0x113d1b820>
 ap.children
(<Article object at 0x1101720b0>, <output_file.NounPhrase object at 0x113d1b340>)
 ap.children[0]
<Article object at 0x1101720b0>
 ap.children[1]
<output_file.NounPhrase object at 0x113d1b340>
 ap.children[1].spelliung
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NounPhrase' object has no attribute 'spelliung'
 ap.children[1].spelling
Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'NounPhrase' object has no attribute 'spelling'
ap.children[1].pos
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#AttributeError: 'NounPhrase' object has no attribute 'pos'
 ap.children[1]
#<output_file.NounPhrase object at 0x113d1b340>
 ap.children[1].pos
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NounPhrase' object has no attribute 'pos'
ap.children[1].children
(<Adjective object at 0x113d1a830>, <Noun object at 0x113d1b2e0>)
ap.children[1].children[1]
<Noun object at 0x113d1b2e0>
ap.children[1].children[1].spelling
'dog
ap.children[1].children[1].pos
'Noun'
 



S





 ap = ArticlePhrase(Article('the'), np)
ap
<__main__.ArticlePhrase object at 0x113d1b820>
ap.children
(<Article object at 0x1101720b0>, <output_file.NounPhrase object at 0x113d1b340>)
ap.children[0]
<Article object at 0x1101720b0>
ap.children[1]
<output_file.NounPhrase object at 0x113d1b340>
ap.children[1].spelliung
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NounPhrase' object has no attribute 'spelliung'
ap.children[1].spelling
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NounPhrase' object has no attribute 'spelling'
ap.children[1].pos
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NounPhrase' object has no attribute 'pos'
ap.children[1]
<output_file.NounPhrase object at 0x113d1b340>
ap.children[1].pos
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NounPhrase' object has no attribute 'pos'
ap.children[1].children
(<Adjective object at 0x113d1a830>, <Noun object at 0x113d1b2e0>)
ap.children[1].children[1]
<Noun object at 0x113d1b2e0>
ap.children[1].children[1].spelling
'dog'
ap.children[1].children[1].pos
'Noun'
the_big_dog = ap
the_big_dog.the = ap.children[0]
the_big_dog.the
<Article object at 0x1101720b0>
the_big_dog.the




the_big_dog.dog = Noun("dog")
the_big_dog
<__main__.ArticlePhrase object at 0x113d1b820>
the_big_dog.the
<Article object at 0x1101720b0>
the_big_dog.big
<Adjective object at 0x113d1a830>
dog
<Noun object at 0x110353b50>
ap
<__main__.ArticlePhrase object at 0x113d1b820>
ap.children
(<Article object at 0x1101720b0>, <output_file.NounPhrase object at 0x113d1b340>)
the_big_dog.children
(<Article object at 0x1101720b0>, <output_file.NounPhrase object at 0x113d1b340>)
type(the_big_dog.children)
<class 'tuple'>

"""

# class N(models.Model):
#     spelling = (models.CharField(default="word spelling"))

# class


