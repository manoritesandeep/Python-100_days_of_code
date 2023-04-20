# Any number of positional arguments
def add1(*args):
    s = 0
    for n in args:
        s += n
    return s


def add(*args):
    return sum(args)


print(add1(3, 5, 6))

print((add(1, 2, 3, 4, 5)))
