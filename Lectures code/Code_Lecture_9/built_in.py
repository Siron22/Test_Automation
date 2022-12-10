# print(abs(-65))
# print(abs(65))
# print(abs(1-65j))

# a = [3, 4, True]
# print(all(a))
# b = [4, []]
# print(all(b))
# c = []
# print(all(c))
# d = []
# print(bool(d and all(d)))

#None 0 "" [] () {}

# a = [0, 0, 0]
# print(any(a))

# print(ascii("ЇЇЇ"))
# print(ascii("hello"))

# print(bin(12))
# print(oct(8))
# print(hex(15))
# print(hex(255))
# print(type(hex(255)))
# print(f"{15:x}")
# print(f"{15:#b}")

# print(bool([]))
# a = b"efgfdssdadsf"
# print(a)
# print(type(a))

# a = bytearray()
# print(a)
# b = bytearray("dssdcscЇ", encoding='utf-8')
# print(b)

# print(callable(5))
# print(callable(len))

# print(chr(107))
# print(chr(108))
# print(ord('k'))

# print(dict())
# print(dict([('name', 'John')]))
#
# a = [56]
# print(dir(a))
# print(dir(5))

#print(divmod(13, 5))

# lst = ['aaa', 'bbb']
# for i, value in enumerate(lst, start=17):
#     print(f"{i}: {value}")

# a = [1,2,3,4,5]
# b = map(str, a)
# print(list(b))
#
# a = [1,2,3,4,5]
# b = [5,4,3]
# c = map(lambda x, y:x + y, a, b)
# print(list(c))

# a = [4,5,7,2, 1, -3]
# b= filter(lambda x: x <= 3, a)
# print(list(b))
#
# a = [4,5,7,2, 1, -3]
# b= filter(lambda x: x > 10, a)
# print(bool(b))
# print(list(b))

# a = [1, 2, 3, 5, 6, 7]
# b = [1, 2, 3, 5, 6]
# d = [7, 3]
# c = zip(a, b, d)
# print(list(c))
#
# q = [1, 2, 4]
# print(list(zip(q)))

from functools import reduce
a = [1, 2, 4, 6, 6, 3, 1]
# [1, 2, 4, 6]
# [3, 4, 6]
# [7, 6]
# [13]

# s = lambda x, y, z: x + y + z
# print(s(1,2,3))
#
# b = reduce(lambda x, y, z: x + y + z, a)
# print(b)

# minimal = reduce(lambda x, y: x if x < y else y, a)
# print(minimal)

# a = [[1, 2, 3], [4, 5, 6], [7, 8, [55, 66, 77], 9]]
# b = reduce(lambda x, y: x + y, a)
# print(b)

#a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# x = 2
# eval("print(x+6)")

# print(int("33"))
# print(float("54.7"))

# a = input("Enter data: ")
# print(a)

# print(format('q', '_>6'))
#
# id = "1"
# name = "John"
# salary = 1000.55433
# print(f"{id: >6} {name: >8} {salary: >.2f}")

#
# johny = {'name': 'Johny', 'age': 34}
# john = {'name': 'John', 'age': 34}
# anna = {'name': 'Anna', 'age': 44}
# oksana = {'name': 'Oksana', 'age': 49}
# persons = [johny, oksana, john, anna]
#
# print(sorted(persons, key=lambda p: (p['age'], len(p['name']))))
#
# print(min(persons, key=lambda p: len(p['name'])))
# #sorted(persons)

# import math
# a = 1.55336
# print(round(a, 2))
# print(math.floor(a))
# print(math.trunc(a))
# print(math.ceil(a))

# print(type(3))
# print(type((1,2,3)))
#
# print(isinstance(5, int))
# print(isinstance([1,3], list))
# print(isinstance(5, list))
#
# a = 1
# if type(a) == type(1):
#     print("PASS")
#
# print()
# a = [1, 2, 3]
# b = [1, 2, 3]
#
# print(id(a) == id(b))
#
# c = (1, 2, 3)
# d = (1, 2, 3)
# print(id(c) == id(d))
#
#
# print()

# c = a
# print(a is b)
#
# print(id(a) == id(c))
#

# a = 30000000
# b = 30000000
# print(id(a) == id(b))

# import string
# print(string.digits)
# print(string.ascii_letters)
# print(string.punctuation)