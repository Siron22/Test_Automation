# a = 4
# symbol = '*'
# b = [4, 5, 6, 1, 2, 7]
# c = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]
#
# for y in c:
#     for x in y:
#         print(x, end=' ', sep=',')
#     print()

# 0, 1, 2, 3
# for i in range(a):  # O(N^2)
#     print(f'{i} = {b.count(i)}')

# a = 3
# b = 4
#
# print(a + b)
#
# c = 3
# [1, 2, 3, 4, 5, 6, 7, 8]


# a = 'hello world'

# print(a[6])
# print( a.find('l', 3, 10) )
# print( a.rfind('l') )
# try:
#     print( a.index('easd') )
# except ValueError:
#     print('Not found')

# print( len(a) )  # str, list, set, tuple, frozenset, dict
#
# print(a.encode())
#
# data = open('aaa.png', 'rb').readlines()
# print(data)


# url = 'https://domain.com'

# print(url.rfind('.com'))

# if url.startswith('https://') and url.endswith('.com'):
#     print('OK')
# else:
#     print('Error')

# if url.find('https://') == -1 or url.find('.com') == -1:
#     print('ValueError')
# else:
#     print('OK')

# csv
# a = '1, 2, 3, 4, 5, 6'

# print(a[::-1].replace('o', 'O', 1)[::-1])

# items = a.split(', ')[:4]
# only_str_items = list(map(str, ['hello', 'world', 2, '1', '2']))

# for item in ['hello', 'world', 2, '1', '2']:
#     only_str_items.append(str(item))

# print(only_str_items)
# new_a = '-_'.join(only_str_items)

# print(new_a)

# a = 'ÖHeLLo 2 worlD'

# print(a.upper())
#
# print(a.lower())
# print(a.casefold())
#
# print(a.title())
# print(a.swapcase())
# print(a.capitalize())

# print('1test'.title())

# a = '  test  \n'

# print(a.lstrip())
# print(a.rstrip())
# print(a.strip())

# print('{} hello'.format('23'))


# items = ['Hello', 1, 2, 3, True, False]
# a = list()

# print(items[2:])
# print(len(items))
#
# print(items)

# for item in items:
#     print(item)
#
# for idx in range(len(items)):
#     print(items[idx])

# for idx, item in enumerate(items):
#     print(f'{idx} = {item}')


# coords = [1, 10, 4, 5, 6, 7, -2, 'Operation Error', 'IndexError']

# x = coords[0]
# y = coords[1]
# z = coords[2]

# *errors, x, y, z = coords
# x, y, z, *errors = coords
# x, *errors, z = coords

# print(*coords)
# print(1, 10, 4, 5, 6, 7, -2, 'Operation Error', 'IndexError')

# print(1 in coords)
# print('IndexErro123r' not in coords)

# a = [1, 2]
# b = [3, 4]

# print(a > b)
# print(a >= b)
# print( a == b )
# print( a != b )
# print( a * 3 )
# print( a + b )

# random.randint()

import random


# items = ['Hello world', 1, 2.5, True, False]

# print(random.choice(items))
# print(random.choices(items, k=4))
# print(random.sample(items, k=4))

# print(random.randint(1, 10))
#
# items = ['Hello', None, 1, 3, False, True, None]

# for _ in range(10):
#     random_number = random.randint(-10, 10)
#     items.append(random_number)
#
# print(items)

# map_out = list(map(float, items))
# reversed_out = list(reversed(items))
# filter_out = list(filter(None, items))

# print(items)
# print(filter_out)

# print(map_out)
# print(min(items))
# print(max(items))
# print(sorted(items, reverse=False))