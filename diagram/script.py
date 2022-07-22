from random import randint as ri


class Word:
    def __init__(self, spelling='', pos=''):
        self.spelling = spelling 
        self.pos = pos    

class Noun: 
    def __init__(self, spelling='', pos=''):
        self.head = 'NOUN'
        self.spelling = spelling 
        self.pos = pos

class Verb: 
    def __init__(self, spelling='', pos=''):
        self.head = 'VERB'
        self.spelling = spelling 
        self.pos = pos

class Adjective: 
    def __init__(self, spelling='', pos=''):
        self.head = 'ADJECTIVE'
        self.spelling = spelling 
        self.pos = pos

class Article: 
    def __init__(self, spelling='', pos=''):
        self.head = 'ARTICLE'
        self.spelling = spelling 
        self.pos = pos


    

f = open('train.txt', 'r')
lines = f.readlines()
lines = [line.lower() for line in lines]
tuples = [(line.split()[-3], line.split()[-2]) for line in lines if len(line.split()) >= 3]
spelling_and_pos = []
for tuple in tuples:
# print('word.spelling is', tuple[0])
# print('word and part of speech are', tuple[0], tuple[1])
    spelling_and_pos.append({'spelling': tuple[0], 'pos': tuple[1]})

# print('spelling_and_pos[:100] is', spelling_and_pos[:100])

#it's easier to type it this way
sap = spelling_and_pos

# #make the list of dictionaries smaller
# sap = sap[:1000]
# print(sap)

#we're not using this for now
# items = [list(item.items()) for item in sap]

print('\n\nspelling_and_part_of_speech at random index is', sap[ri(0, len(sap))])
