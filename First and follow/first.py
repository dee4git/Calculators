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


def variable_remover(ob, up_next):
    global global_first
    tokens = word_tokenize(ob.first)
    if up_next == '':
        pass
    elif up_next == 'epsilon':
        print('up next is epsilon')
    else:
        print('will handle')
        tokens = [up_next]
    print('tokens--->', tokens)
    for i in objs:
        if i.first_safe:
            # print('replacing...')
            if i.left in tokens:
                print('match found in ', i.left)
                index = tokens.index(i.left)
                print(index)
                # doing this because A is there which will be replaced
                tokens[index] = ''
                first = word_tokenize(i.first)
                for j in first:
                    if j != 'epsilon':
                        tokens[index] += ' ' + j
                    else:
                        print('Fount epsilon i am in danger')
                        current = ob.first
                        current = word_tokenize(current)
                        current = current[0]
                        for chunk in ob.chunks:
                            for item in chunk:
                                if item == current:
                                    item_index = chunk.index(item)
                                    try:
                                        next_item = chunk[item_index + 1]
                                        print('epsilon handle')
                                        variable_remover(ob, next_item)
                                    except:
                                        # global_first += 'epsilon'
                                        # global_first = TreebankWordDetokenizer().detokenize(global_first)
                                        # ob.first = global_first
                                        # safety_checker(ob)

                                        print('epsilon found at the end.')

            else:
                pass
                # print('Could not replace')
    print('last stage', tokens)
    tokens = TreebankWordDetokenizer().detokenize(tokens)
    tokens = word_tokenize(tokens)
    for tok in tokens:
        global_first += tok
    global_first = TreebankWordDetokenizer().detokenize(global_first)
    ob.first = global_first
    safety_checker(ob)


# for i in range(len(objs)):
for ob in objs:
    if not ob.first_safe:
        print('sending...', ob.left)
        variable_remover(ob, '')

print('--------------------------')
print('state:  first : first_safe')
for i in objs:
    print(i.left, ':', i.first, ':', i.first_safe)
print('--------------------------')
