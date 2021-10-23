import first as f

objs = f.objs


def get_first_of(up_next):
    for a in objs:
        if a.left == up_next:
            return a.first


def recursive_updater(i, chunk, index):
    up_next = chunk[index + 1]
    if up_next in f.lower_case:
        print('will add', up_next)
        i.follow += ' ' + up_next
    else:
        print('next in uppercase ->', up_next)
        up_next = get_first_of(up_next)
        tokens = f.word_tokenize(up_next)
        print(tokens)
        for tok in tokens:
            if tok not in i.follow and tok != 'epsilon':
                i.follow += ' ' + tok
            else:
                if tok == 'epsilon':
                    next_index = index + 1
                    last_index = len(chunk) - 1
                    if last_index >= next_index:
                        recursive_updater(i, chunk, next_index)
                    else:
                        print('Not handled yet')


for x in range(2):
    for i in objs:
        left = i.left
        for j in objs:
            for chunk in j.chunks:
                if left in chunk:
                    print('->', left, chunk)
                    index = chunk.index(i.left)
                    last_index = len(chunk) - 1
                    if index == last_index:
                        print('working...', j.left)
                        i_follows = f.word_tokenize(i.follow)
                        j_follows = f.word_tokenize(j.follow)
                        elements = (set(i_follows+j_follows))
                        blank = ''
                        for ele in elements:
                            blank += ' '+ele
                        i.follow = blank
                    else:
                        recursive_updater(i, chunk, index)

print('--------------------------')
print('state :  follow : follow_safe')
for i in objs:
    # duplicate removal
    i.follow = f.word_tokenize(i.follow)
    i.follow = ' '.join(list(set(i.follow)))
    print(i.left, ':', i.follow, ':', i.follow_safe)
print('--------------------------')
