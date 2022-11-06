# a = ' ' * 0
#
# print('', '*', sep='-')
# print(1, 2, sep='-')

a = [1, 1, 2, 3, 44, 4, 5, 1]

count = 0

for i in a.copy():  # [2, 3, 44, 4, 5]
    a.remove(i)
    a.copy().count
    # a.append(i)
    count += 1
    print(i)
print(a)
print(count)

# a = 'Hello world'
#
# print(a.replace('l', '|').replace('o', '0'))

# numbers = [1, 2, None, 3, 45, None]
#
# new_numbers = list(filter(None, numbers))
# print(numbers)
# print(new_numbers)

# numbers = input('Enter numbers: ').split(',')
# new_numbers = sum(map(int, numbers))
# print(new_numbers)

# import random

# numbers = [(random.randint(1, 10), i) for i in range(10) if i % 2 == 0]
# numbers = [5, 10, 3, 8, 1, 4, 2, 9, 10, 3]
# numbers = [x for x in numbers if x < 5]

# print(numbers)

# numbers = [5, 10, 3, 8, 1, 4, 2, 9, 10, 3]
#
# print(numbers)

# del numbers[1]
# del numbers[12]
# del numbers[1]
# del numbers
#
# print(numbers)


# values = []
#
# for _ in range(4):
#     number = int(input('Enter a number: '))
#     print(f'Number = {number} | values = {values}')
#     # values.insert(0, number)
#     values.append(number)

# print(values.count(4))
# print(values.index(1))
# print(1 in values)
# print(1 is values)

# a = [1]
# b = [1]
#
# print(a == b)
# print(hex(id(a)), hex(id(b)))

# print(values)

# numbers = [5, 10, 3, 8, 1, 4, 2, 9, 10, 3]
#
# print(numbers)
# a = numbers.pop(1)
# print(a)
# print(numbers)
# print(numbers)
# numbers.insert(14, 2)
# numbers[1] = 2

# print(numbers)

# import copy
#
#
# a = [1, 2, ['Hello', 'world'], 3, 4, ]
# b = copy.deepcopy(a)
# # b[2] = b[2].copy()
# print(a is b)
# print(a[2] is b[2])
#
# print(a, b)
# b.append(5)
# b[2].append(False)
#
# print(a, b)
# import random
#
# values = []
#
# for i in range(10):
#     number = random.randint(1, 10)
#     print(number)
#     if number % 2 == 0:
#         continue
#
#     values.append(number)

# a = (1, 2, 3, 4, 1)

# print(a[::-1])
# print(a[-1])
# print(a.count(1))
# print(a.index(13))
# print(len(a))
# print(hex(id(a)))
# a = a + (1, 2)
# print(hex(id(a)))

# import sys

# a = (1, 2, [3, 4], False)

# a = (x for x in range(1000))
# b = [x for x in range(1000)]
#
# print(sys.getsizeof(a))
# print(sys.getsizeof(b))

# print(a)
# a[2].extend([5, 6])
# try:
#     a[2] += [5, 6]
# except TypeError as e:
#     print(e)
# a[0] += 3
# print(a)


# a = [1, 2,]
# b = [3, 4]
# print(a + b)


# a = {11, 22, 11, 33, (1, 2, 3)}

# print(a[1])

# for i in a:
#     print(i)

# print(113 in a)

# a = {1, 2, 3, 4, 5, 6}
# b = {3, 2, 1}
# b = {4, 5, 6, 7}
# a = {1, 2, 3}
# b = {1, 2, 3}
#
# print(b.issubset(a))
# print(a.issuperset(b))
# print(a | b)  # a.union(b)
# print(a & b)  # a.intersection(b)
# print(a.difference(b))  # a - b
# print(b.difference(a))  # b - a
# print(a.symmetric_difference(b))  # a ^ b

# a = 3
# b = 4
# a += b
# import random
#
# numbers = [random.randint(1, 10) for _ in range(10)]
# print(numbers)
# print(len(numbers) - len(set(numbers)))
