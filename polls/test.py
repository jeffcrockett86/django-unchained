

# def isnt(funny):
#     print('I\'m')
#     return '?'

# def sub(isnt):
#     print('Just')
#     return isnt

# def this(sub):
#     print('Kidding')
#     return sub




# post_title = {'title': (this(sub(isnt('funny'))))}

# print(post_title)

# def test(sentence):
#     return sentence
# ... 
# def a(test):
#     return test(sentence)
# ... 
# def _is(a):
#    return a(test)

# # def this(_is):
# #     return 
# """
#  Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'this' is not defined
# >>> def this(is):
#   File "<stdin>", line 1
#     def this(is):
#              ^^
# SyntaxError: invalid syntax
# >>> def this(_is):
# ...   return is(a)
#   File "<stdin>", line 2
#     return is(a)
#            ^^
# SyntaxError: invalid syntax
# >>> def this(_is):
# ...   return _is(a)
# ... 
# >>> this(_is(a('test')))
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in a
# NameError: name 'sentence' is not defined
# >>> def a(sentence):
# ...   print(sentence):
#   File "<stdin>", line 2
#     print(sentence):
#                    ^
# SyntaxError: invalid syntax
# >>> def a(sentence):
# ...   print(sentence)
# ...   return sentence
# ... 
# >>> this(_is(a('test')))
# test
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in _is
# TypeError: 'str' object is not callable
# >>> def test(and):
#   File "<stdin>", line 1
#     def test(and):
#              ^^^
# SyntaxError: invalid syntax
# >>> def test(_and):
# ...   print(_and)
# ...   return _and
# ... 
# >>> this(_is(a(test('and'))))
# and
# and
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in _is
# TypeError: 'str' object is not callable
# >>> this(_is(a(test('_and'))))
# _and
# _and
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in _is
# TypeError: 'str' object is not callable
# >>> this(_is(a(test('_and'))))
# """

# """
#  this idea just popped into my head while i was playing
# scrabble with my mom. i've been working with similar concepts in python
# things much less creepy and weird, of course
#  i can walk you through the steps.

#  1. import the bible as a text file. 

#  2. split the string up into a list of words

#  3. go through the list and add a ( to each word.

#  4. keep a count of the number of (
#     increase the count by one each time you're in the loop

# 5. put quotation marks around the last word

# 6. finish it up with ) * the number of (

# 7. each pair of ( and ) is a function call. Think of it as like
# a 100,000 layer onion, and the innermost layer- the core of the onion-
# is just a string. that string is the last word of the bible.

# i think this will only work if the whole thing writes its name into
# a blank Python file. not sure about that actually. hmmm.



#  """


# """
"""
INTRO TO DSA

AKA DICK SUCKING ALGORITHMS

THESE ARE VERY IMPORTANT BECAUSE JOB INTERVIEWERS ASK
ABOUT DSA STUFF A LOT. SO HERE IS AN EXAMPLE OF SOME
CODE YOU SHOULD KNOW
"""

# from random import randint as ri

#it's like a dick factory lmao
class Dick:
    def __init__(self):
        self.be_long = True

def suck_that(dick):
    if dick.be_long:
        print('finna SUCK uWu')

#it's new dick time
dick = Dick()
suck_that(dick)
 