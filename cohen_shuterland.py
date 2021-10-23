x_max = 2
y_max = 6
x_min = -3
y_min = 1
count = 0


def sign(param):
    print(round(param, 2), end=' >> ')
    if param > 0:
        print(1)
        return '1'
    else:
        print(0)
        return '0'


def binary_of(st):
    return '{0:04b}'.format(int(st, 2))


def get_code(x, y):
    print('Bit 1:', y, '-', y_max, end=' = ')
    one = sign(y - y_max)
    print('Bit 2:', y_min, '-', y, end=' = ')
    two = sign(y_min - y)
    print('Bit 3:', x, '-', x_max, end=' = ')
    three = sign(x - x_max)
    print('Bit 4:', x_min, '-', x, end=' = ')
    four = sign(x_min - x)
    # TBRL
    code = one + two + three + four
    # reverse TBRL
    # code = four + three + two + one
    print('code:', code)
    print('----')
    return binary_of(code)


def caller(new_c1, new_c2):
    decider(new_c1, new_c2)


def cutter(p):
    new_c1 = ''
    new_c2 = ''
    global count
    count += 1
    print()
    print('p' + str(count), end=" ")
    for i in range(len(p)):
        # print('Trying', p[i])
        if p[i] == 1:
            print('updating...', p)
            index = i
            if index == 0:
                print('Bit', index + 1, 'is 1:')
                new_y = y_max
                new_x = x1 + (y_max - y1) / m
                print('new_y = ', new_y)
                new_x = round(new_x, 2)
                print('new_x = ', x1, '+', '(', y_max, '-', y1, ')', '/', m, ' = ', new_x)

                print('After cut x,y =', end=" ")
                print(new_x, ',', new_y)
                # new_c2 = get_code(new_x, new_y)
            elif index == 1:
                print('Bit', index + 1, 'is 1:')
                new_x = x_max
                print('new_x = ', new_x)
                new_y = y1 + m * (x_max - x1)
                new_y = round(new_y, 2)
                print('new_y = ', y1, '+', m, '*', '(', x_max, '-', x1, ') = ', new_y)

                print('After cut x,y =', end=" ")
                print(new_x, ',', new_y)
                # new_c2 = get_code(new_x, new_y)
            elif index == 2:
                print('Bit', index + 1, 'is 1:')
                new_y = y_min
                print('new_y = ', new_y)
                new_x = x1 + (y_min - y1) / m
                new_x = round(new_x, 2)
                print('new_x = ', x1, '+', '(', y_min, '-', y1, ')', '/', m, ' = ', new_x)

                print('After cut x,y =', end=" ")
                print(new_x, ',', new_y)

                # new_c1 = get_code(new_x, new_y)
            elif index == 3:
                print('Bit', index + 1, 'is 1:')
                new_x = x_min
                print('new_x = ', new_x)
                new_y = y1 + m * (x_min - x1)
                print('new_y = ', y1, '+', m, '*', '(', x_min, '-', x1, ') =', new_y)
                new_y = round(new_y, 2)
                print('After cut x,y =', end=" ")
                print(new_x, ',', new_y)


def inspector(c1, c2):
    c1 = list(map(int, c1))
    c2 = list(map(int, c2))
    cutter(c1)
    cutter(c2)


def decider(c1, c2):
    logical_and = ''
    logical_or = ''

    c1 = list(map(int, c1))
    c2 = list(map(int, c2))
    for i, j in zip(c1, c2):
        logical_and += str(i & j)
        logical_or += str(i | j)

    print('logical_or =', logical_or)
    print('logical_and =', logical_and)

    if logical_or == '0000':
        print('->Accept')
    elif '1' in logical_and:
        print('->Reject')
    else:
        print('->Intersect')
        inspector(code1, code2)


# global input
x1, y1 = -1, 5
x2, y2 = 3, 8
# x1, y1 = -4, 2
# x2, y2 = -1, 7
m = round((y2 - y1) / (x2 - x1), 2)
print('P1 = ', x1, ',', y1)
print('P2 = ', x2, ',', y2)
print('m = ', m)
print('---')
print('P1 code >>>', x1, ',', y1)
code1 = get_code(x1, y1)
print('P2 code >>>', x2, ',', y2)
code2 = get_code(x2, y2)
decider(code1, code2)
