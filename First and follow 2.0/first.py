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

# first making:
for ob in objs:
    for c in ob.chunks:
        ob.first += ' ' + (c[0])

upper_case = string.ascii_uppercase
lower_case = string.ascii_lowercase
upper_case = list(upper_case)
lower_case = list(lower_case)


# first safe updater:
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
# global list to save all the firsts
global_first = ''


def get_next(obz, replace):
    for i in obz.chunks:
        for j in range(len(i)):
            if i[j] == replace:
                try:
                    return i[j + 1]
                except:
                    return 'kichu_nai'


global_first = ''


def custom_check(obz):
    for i in obz.first:
        if i in upper_case:
            obz.first_safe = False
        else:
            obz.first_safe = True


def recursive_remover(obz, chunks, up_next):
    global global_first
    replace = 'should not show'
    temp = ''
    replace = up_next
    print('replacing...', replace)
    for o in objs:
        if o.first_safe:
            if o.left == replace:
                # will add the variables now
                # but tokenize first to not to break epsilon
                o.first = word_tokenize(o.first)
                temp = ''
                for fst in o.first:

                    if fst != 'epsilon':
                        temp += ' ' + fst
                    else:
                        up_next = get_next(obz, replace)
                        print('next is', up_next)
                        if up_next == 'kichu_nai':
                            global_first += 'epsilon'
                        else:
                            recursive_remover(obz=obz, chunks=chunks, up_next=up_next)
    for t in word_tokenize(temp):
        global_first += ' ' + t
    obz.first = word_tokenize(global_first)
    custom_check(obz)


for ob in objs:
    if not ob.first_safe:
        print('sending...', ob.left)
        recursive_remover(ob, ob.chunks, ob.chunks[0][0])

# detokenizing...
for ob in objs:
    ob.first = TreebankWordDetokenizer().detokenize(ob.first)

print('--------------------------')
print('state:  first : first_safe')
for i in objs:
    print(i.left, ':', i.first, ':', i.first_safe)
print('--------------------------')
