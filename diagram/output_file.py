from script import Noun
from script import Verb
from script import Adjective 
from script import Article 

the = Article("the")
big = Adjective("big")
dog = Noun("dog")
runs = Verb("runs") 

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

class AdjPhrase:
    def __init__(self, *args):
        self.head = "ADJECTIVE"

        # for arg in args:
            # print(arg)
        self.children = args

class Sentence:
    def __init__(self, *args):
        self.head = "SENTENCE"

        # for arg in args:
        #     print(arg)
        self.children = args



ap = AdjPhrase(Adjective("big"), Noun("dog"))

ap = ArticlePhrase(Article("the"), ap)

lst = [Article("The"), Adjective("red"), Noun("ball")]
# lst
# [<script.Article object at 0x10646eb30>, <script.Adjective object at 0x10a017970>, <script.Noun object at 0x10a017f10>]
the_red_ball = ArticlePhrase(Article("The"), Adjective("red"), Noun("ball"))
# <script.Article object at 0x10a017700>
# <script.Adjective object at 0x10a017dc0>
# <script.Noun object at 0x10a017fa0>
# the_red_ball
# <output_file.ArticlePhrase object at 0x10a017d90>
_is = Verb("is")
blue = Adjective("blue")

_is_blue = VerbPhrase(_is, blue)

the_red_ball_is_blue = Sentence(the_red_ball, _is_blue)

print(the_red_ball_is_blue)

NP = NounPhrase
AdjP = AdjPhrase
ArtP = ArticlePhrase
S = Sentence
VP = VerbPhrase
N = Noun
V = Verb
Adj = Adjective
Art = Article


"""
from output_file import *
Currently feeding Lassie
<script.Adjective object at 0x10a017310>
<script.Noun object at 0x10a017370>
<script.Article object at 0x10a017430>
<output_file.AdjPhrase object at 0x10a0173d0>
ap
<output_file.ArticlePhrase object at 0x10a017490>
ap.children
(<script.Article object at 0x10a017430>, <output_file.AdjPhrase object at 0x10a0173d0>)
ap.children[0]
<script.Article object at 0x10a017430>
ap.children[0].spelling
'the'
the = ap.children[0]
the = the.spelling
the
'the'
ap = AdjPhrase(Adjective("big"), Noun("dog"))
<script.Adjective object at 0x10646e0b0>
<script.Noun object at 0x10a017880>
ap.children
(<script.Adjective object at 0x10646e0b0>, <script.Noun object at 0x10a017880>)
big = ap.children[0].spelling
big = ap.children[1].spelling
big = ap.children[0]
dog = ap.children[1]
dog
<script.Noun object at 0x10a017880>
the_big_dog
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'the_big_dog' is not defined
big_dog
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'big_dog' is not defined
big_dog = AdjPhrase(big, dog)
<script.Adjective object at 0x10646e0b0>
<script.Noun object at 0x10a017880>
the_big_dog = ArticlePhrase(Article("the"), big_dog)
<script.Article object at 0x10a017a90>
<output_file.AdjPhrase object at 0x10a017a00>


class Sentence:
   def __init__(self, *args):
     self.children = args
 
the_big_dog_runs = Sentence(the_big_dog, VerbPhrase("runs"))
runs
the_big_dog_runs
<__main__.Sentence object at 0x10a017d00>
the_big_dog_runs.children
(<output_file.ArticlePhrase object at 0x10a017670>, <output_file.VerbPhrase object at 0x10a017ca0>)

            
"""
class ArticlePhrase:
   def __init__(self, *args):
     self.children = args
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
(<script.Article object at 0x1101720b0>, <output_file.NounPhrase object at 0x113d1b340>)
 ap.children[0]
<script.Article object at 0x1101720b0>
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
(<script.Adjective object at 0x113d1a830>, <script.Noun object at 0x113d1b2e0>)
ap.children[1].children[1]
<script.Noun object at 0x113d1b2e0>
ap.children[1].children[1].spelling
'dog
ap.children[1].children[1].pos
'Noun'
 









 ap = ArticlePhrase(Article('the'), np)
ap
<__main__.ArticlePhrase object at 0x113d1b820>
ap.children
(<script.Article object at 0x1101720b0>, <output_file.NounPhrase object at 0x113d1b340>)
ap.children[0]
<script.Article object at 0x1101720b0>
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
(<script.Adjective object at 0x113d1a830>, <script.Noun object at 0x113d1b2e0>)
ap.children[1].children[1]
<script.Noun object at 0x113d1b2e0>
ap.children[1].children[1].spelling
'dog'
ap.children[1].children[1].pos
'Noun'
the_big_dog = ap
the_big_dog.the = ap.children[0]
the_big_dog.the
<script.Article object at 0x1101720b0>
the_big_dog.the




the_big_dog.dog = Noun("dog")
the_big_dog
<__main__.ArticlePhrase object at 0x113d1b820>
the_big_dog.the
<script.Article object at 0x1101720b0>
the_big_dog.big
<script.Adjective object at 0x113d1a830>
dog
<script.Noun object at 0x110353b50>
ap
<__main__.ArticlePhrase object at 0x113d1b820>
ap.children
(<script.Article object at 0x1101720b0>, <output_file.NounPhrase object at 0x113d1b340>)
the_big_dog.children
(<script.Article object at 0x1101720b0>, <output_file.NounPhrase object at 0x113d1b340>)
type(the_big_dog.children)
<class 'tuple'>

"""