# l = [1,2,3]
# t = (1,2,3)
# d = {1: 'a', 2: 'b'}
#
# with open('test.txt') as f:
#     f_iter1 = iter(f)
#     f_iter2 = iter(f)
#     print(f_iter1 is f_iter2)
#     print(f is f_iter1)
#     for line in f:
#         print(line)
#     for line in f:
#         print(line)

# for i in l:
#     print(i)
#
# for i in l:
#     print(i)

#l_iter = iter(l)
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))
# print(next(l_iter))

# l = [1,2,3]
# l_iter1 = iter(l)
# l_iter2 = iter(l)
# print(l_iter1 is l_iter2)
# print(l is l_iter1)

# def number():
#     for i in range(10):
#         yield i
#
# g = number()
# for i in g:
#     print(i)
# for i in g:
#     print(i)

# a = (i for i in range(10))
# for i in a:
#     print(i)
# for i in a:
#     print(i)


# def g():
#     yield 1
#     yield 2
#     yield 3
#
# g_  = g()
# for i in g_:
#     print(i)

def g():
    for i in range(3):
        yield i

def f():
    for i in "abc":
        yield i

def q():
    yield from g()
    yield from f()

# for i in q():
#     print(i)

# from itertools import chain
# for i in chain(g(), f()):
#     print(i)


# print('ab' in 'cdrabgd')

def r():
    for i in range(10):
        yield i

r_ = r()
#print(1 in r_)
print(8 in r_)
print(1 in r_)
#print(18 in r_)
#print(1 in r_)