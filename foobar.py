for a in range(0,101):
    if (a%3 == 0) and (a%5 == 0):
        print('foobar')
    elif a%3 == 0:
        print('foo')
    elif a%5 == 0:
        print('bar')
    else:
        print(a)
