from django.db import models
from random import randint as ri 
from . import nltk_words
from . import bible
from . import quran 


def unpack(sentence, div_count=0):
  for child in sentence.children:
    print('sentence.children is', sentence.children)
    if not sentence.children:
      return '<div>' + sentence.spelling + '</div>'
 
    # return '<div>' + unpack(child, div_count + 1)
    return unpack(child)

def rand(lst):
  return lst[ri(0, len(lst))]

# def get_leaf_nodes(self):
#     leafs = []
#     def _get_leaf_nodes( node):
#         if node is not None:
#             if len(node.children) == 0:
#                 leafs.append(node)
#             for n in node.children:
#                 _get_leaf_nodes(n)
#     _get_leaf_nodes(self.root)
#     return leafs
  
  
  # return unpack(sentence.children, div_count + 1)

class W(models.Model):
  spelling = models.CharField(max_length=100, default="spelling")
  pos = models.CharField(max_length=5, default="part of speech")
  # def __init__(self, spelling = spelling, pos = pos):
  #   self.spelling = spelling 
  #   self.pos = pos 
  #   self.children = []

class N(models.Model):
  spelling = models.CharField(max_length = 100, default="spelling")
  pos = models.CharField(max_length=5, default="part of speech")
  # def __init__(self, spelling, pos):
  #   self.spelling = spelling 
  #   self.pos = pos 
  #   self.children = []
    

class V(models.Model):
  spelling = models.CharField(max_length = 100)
  pos = models.CharField(max_length=5)
  # def __init__(self, spelling=spelling, pos = pos):
  #   self.spelling = spelling 
  #   self.pos = pos   
  #   self.children = []
    

class Adj(models.Model):
  spelling = models.CharField(max_length = 100)
  pos = models.CharField(max_length=5)
  # def __init__(self, spelling=spelling, pos = pos):
  #   self.spelling = spelling 
  #   self.pos = pos 
  #   self.children = []
    

class Art(models.Model):
  spelling = models.CharField(max_length = 100)
  pos = models.CharField(max_length=5)
  # def __init__(self, spelling=spelling, pos = pos):
    # self.spelling = spelling 
    # self.pos = pos 
    # self.children = []
    

class Adv(models.Model):
  spelling = models.CharField(max_length = 100)
  pos = models.CharField(max_length=5)
  # def __init__(self, spelling=spelling, pos = pos):
  #   self.spelling = spelling 
  #   self.pos = pos 
  #   self.children = []

class Prep(models.Model):
  spelling = models.CharField(max_length = 100)
  pos = models.CharField(max_length=5)
  # def __init__(self, spelling=spelling, pos = pos):
  #   self.spelling = spelling 
  #   self.pos = pos   
  #   self.children = []
    


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
  

"""
To print all nodes of a tree using depth-first search, only few lines are required:
def printTree(root, level=0):
print(" " * level, root.x)
for child in root.children:
printTree(child, level + 1)
#tree = Node(..., children=[Node(...., ...), Node(...,....)] ...
printTree(tree)
"""

ap = AdjectivePhrase(Adjective("big"), Noun("dog"))
ap = ArticlePhrase(Article("the"), ap)
blue = Adjective("blue")
word_lines = nltk_words.nltk_words.split('\n')
wl_ = [line.split(' ')[:-1] for line in word_lines]
b = [line.split('\t') for line in bible.bible.split('\n')]
# b_ = [chunk.lower() for line in b for chunk in line]
b_ = [' '.join(line).lower() for line in b]
all_bible_lines = [' '.join(line.split()) for line in b_]
abl = [line for line in all_bible_lines if len(line) > 1]
# b = [chunk.lower() for line in b for chunk in line]
# q = quran.quran.split('\n\n')
bd = {}
# for pair in wl_:
#   for line in all_bible_lines:
#     split_line = line.split()
#     for word in split_line:
#       if word in pair:
#         bd[word] = pair
# f = open('bible_dict.py', 'w').write(str(bd))



pp = PrepositionPhrase(Preposition('to', 'PP'), ArticlePhrase(Article('the', 'DT'), NounPhrase(Noun('store'))))
vp = VerbPhrase(Verb('walked'), pp)
ap = ArticlePhrase(Article('the', 'DT'), NounPhrase(Noun('dog', 'NN')))
s = Sentence(ap, vp)
d = {
  'words': [],
  'nouns': [],
  'verbs': [],
  'adjectives': [],
  'articles': [],
  'prepositions': [],
  'adverbs': [],
}

for line in word_lines[1000:2000]:
    split_line = line.split(' ')
    # d['words'].append(line)
    if ' NN' in line:
      n = N.objects.create(spelling=split_line[0], pos = split_line[1])
      n.save()
      # d['nouns'].append(Noun(line.split()[0]))
    elif ' VBZ' in line:
      v = V.objects.create(spelling=split_line[0], pos = split_line[1])
      v.save()

      # d['verbs'].append(Verb(line.split()[0]))
    elif ' JJ' in line:
      adj = Adj.objects.create(spelling=split_line[0], pos = split_line[1])
      adj.save()
      # d['adjectives'].append(Adjective(line.split()[0]))
    elif ' IN' in line:
      prep = Prep.objects.create(spelling=split_line[0], pos = split_line[1])
      prep.save()
      # d['prepositions'].append(Preposition(line.split()[0]))
    elif ' DT' in line:
      art = Art.objects.create(spelling=split_line[0], pos = split_line[1])
      art.save()

      # d['articles'].append(Article(line.split()[0]))
    elif ' RB' in line:
      adv = Adv.objects.create(spelling=split_line[0], pos = split_line[1])
      adv.save()
      # d['adverbs'].append(Adverb(line.split()[0]))
  

# rand_noun = d['nouns'][ri(0, len(d['nouns']))]
# rand_noun2 = d['nouns'][ri(0, len(d['nouns']))]

# rand_adj = d['adjectives'][ri(0, len(d['adjectives']))]
# rand_adj2 = d['adjectives'][ri(0, len(d['adjectives']))]

# rand_verb = d['verbs'][ri(0, len(d['verbs']))]
# rand_verb2 = d['verbs'][ri(0, len(d['verbs']))]

# rand_prep = d['prepositions'][ri(0, len(d['prepositions']))]
# rand_prep2 = d['prepositions'][ri(0, len(d['prepositions']))]

# rand_art = d['articles'][ri(0, len(d['articles']))]
# rand_art2 = d['articles'][ri(0, len(d['articles']))]

# test_verse = rand(b_)
# print(test_verse)
def verse_without_numbers(verse):
  # example verse is 'job 27:16 though he heap up silver as the dust, and prepare raiment as the clay;'
  return ' '.join([word for word in rand(verse).split(' ') if not word.replace(':', '').isnumeric()])

vwn = verse_without_numbers

# sorted_nouns = sorted(d['nouns'])
# sorted_verbs = sorted([verb for verb in d['verbs']])
# sorted_adjectives = sorted([adj for adj in d['adjectives']])
# sorted_prepositions = sorted([prep for prep in d['prepositions']])
# sorted_adverbs = sorted([adv for adv in d['adverbs']])



