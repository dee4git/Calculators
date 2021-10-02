import string

import nltk
from nltk.tokenize.treebank import TreebankWordDetokenizer

nltk.download('punkt')
from nltk.tokenize import word_tokenize

with open('txt.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]

objs = []


class Line:
    def __init__(self, left, right, chunks,
                 first, first_safe,
                 follow, follow_safe):
        self.left = left
        self.right = right
        self.chunks = chunks
        self.first = first
        self.first_safe = first_safe
        self.follow = follow
        self.follow_safe = follow_safe


def get_slices(line):
    left, right = line.split("->")
    clean_left = word_tokenize(left)
    chunks = right.split("|")
    clean_chunks = []
    for i in chunks:
        clean_chunks.append(word_tokenize(i))
    return clean_left[0], right, clean_chunks, '', True, '', True


# list of object creation
for line in lines:
    slices = get_slices(line)
    objs.append(Line(slices[0], slices[1], slices[2], slices[3], slices[4], slices[5], slices[6]))

objs[0].follow = '$'

# first:
for ob in objs:
    for c in ob.chunks:
        ob.first += ' ' + (c[0])

# first safe updater:
upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
upper_case = list(upper_case)
lower_case = list(lower_case)


def safety_checker(ob):
    first = ob.first
    tokens = word_tokenize(first)
    for t in tokens:
        if t in upper_case:
            ob.first_safe = False
        else:
            ob.first_safe = True


for ob in objs:
    safety_checker(ob)

# time to sort by state without variable
sorted_objs = sorted(objs, key=lambda x: x.first_safe, reverse=True)
objs = sorted_objs


def variable_remover(ob):
    print('To be treated: ', ob.first)
    tokens = word_tokenize(ob.first)
    print(tokens)
    for i in objs:
        if i.first_safe:
            if i.left in tokens:
                index = tokens.index(i.left)
                tokens[index] = i.first
                print('replaced')
            else:
                print('Could not replace')

    tokens = TreebankWordDetokenizer().detokenize(tokens)
    ob.first = tokens
    safety_checker(ob)


for i in range(len(objs)):
    for ob in objs:
        if not ob.first_safe:
            print('sending...', ob.left)
            variable_remover(ob)

print('--------------------------')
print('state:  first : first_safe')
for i in objs:
    print(i.left, ':', i.first, ':', i.first_safe)
print('--------------------------')

