"""1. Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента.
"""
# def change(lst: list):
#     lst[0], lst[-1] = lst[-1], lst[0]
#     return lst
#
#
# a = change([1, 2, 3, 4, 5])
# print(a)

"""2. Напишите функцию to_dict(lst), которая принимает аргумент в виде списка и возвращает словарь, в котором каждый
элемент списка является и ключом и значением.
Предполагается, что элементы списка будут соответствовать правилам задания ключей в словарях.
"""
# Решение 1. Через простой цикл
# def to_dict(lst: list):
#     my_dict = {}
#     length = len(lst)
#     for i in range(length):
#         my_dict[lst[i]] = lst[i]
#     return my_dict
#
#
# a = to_dict([7, 8, 9, 0])
# print(a)

# Решение 2. Comprehension

# def to_dict(lst: list):
#     my_dict = {lst[i-1]: lst[i-1] for i in lst}
#     return my_dict
#
#
# a = to_dict([1, 2, 3, 4, 5])
# print(a)

"""3. Напишите функцию sum_range(start, end), которая суммирует все целые числа от значения «start» 
до величины «end» включительно.
Если пользователь задаст первое число большее чем второе, просто поменяйте их местами."""

# def sum_range(start: int, end: int):
#     if start > end:
#         start, end = end, start
#     numbers = []
#     for i in range(start, end+1):
#         numbers.append(i)
#         b = sum(numbers)
#     return b
#
# a = sum_range(7, 5)
# print(a)

"""4. Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать 
построчно последние строки в количестве lines
(на всякий случай проверим, что задано положительное целое число)."""

# Решение 1. Split('\n')
# def read_last(lines: int, file):
#     if type(lines) == int and lines > 0:
#         for i in range(lines):
#             with open(f'{file}', 'r') as f:
#                 f = f.read()
#             f = list(f.split ('\n'))
#             f.reverse()
#             line = f[i]
#             print(line)
#     else:
#         print('Argument "LINES" is incorrect')
#
#
# read_last(2, 'data_HW8.txt')

# Решение 2. Splitlines

# st(lines: int, file):
#     if type(lines) == int and lines > 0:
#         for i in range(lines):
#             with open(f'{file}', 'r') as f:
#                 f = f.read()
#             f = list(f.splitlines())
#             f.reverse()
#             line = f[i]
#             print(line)
#     else:
#         print('Argument "LINES" is incorrect')
#
#
# read_last(3, 'data_HW8.txt')
