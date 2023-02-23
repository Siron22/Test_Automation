# Вывести на экран квадрат 5 на 5 заполненный символами '#'

# print('#####')
# print('#####')
# print('#####')
# print('#####')
# print('#####')

# print('#####\n' * 5)

# print( (('#' * 5) + '\n') * 5 )

# for i in range(5):
#     print(i)

# print('Hello world\t')

# a = '#'
# b = ' '
#
# print(a + b + a + b + a)

# print(5 > 6)

# a = 1
#
# a = a + 1  # a += 1

# print(a)


# a = 10
# b = 4

# print( a > 5 and b < 5 )

# print( True and False and True )  # &&
# print( True or False or True )  # ||
# print( not False )


# status_code = 200
# # 200 .. 299
#
# print( status_code >= 200 and status_code <= 299 )
# print( 200 <= status_code <= 299 )

# string = 'Hello world'
# substring = 'w1'
#
# print( substring in string )
# print( substring not in string )

# print(2 in [1, 2, 3, 4, 5])
# print(123 not in [1, 2, 3, 4, 5])

# print( 2 in (1, 2, 3, 4, 5) )
# print( 123 in (1, 2, 3, 4, 5) )
#
# print( 2 in {1, 2, 3, 4, 5} )
# print( 123 in {1, 2, 3, 4, 5} )

# a = 4
# b = 5
#
# print(a is 4)
# print(a is not b)

# a = -4
# print( -a )

# print( True or False )
# print( False and True or False )


# temp = 42
#
#
# if temp >= 40:
#     print('Очень жарко')
# elif temp >= 30:
#     print('Жарко')
# else:
#     print(f'Температура: {temp}')
#
# print('End')

# if ...:
#     pass
# elif ...:
#     pass
# else:
#     pass
#
# if ...:
#     pass
# elif ...:
#     pass
#
# if ...:
#     pass
# else:
#     pass


if True:
    pass
elif True:
    print('2')
else:
    print('3')


"""
1) Если переменная a равна 10, то выведите 'Верно', иначе выведите 'Неверно'.
2) Если переменная а делится на 2 без остатка, то выведите 'Верно', иначе выведите 'Неверно'.
"""

# try:
#     a = int(input('Enter number A: '))
#     b = int(input('Enter number B: '))
# except ValueError as e:
#     print(f'Error: {e}')
#
# if a == 10 and b > a:
#     print('Верно')
# else:
#     raise ValueError(f'{a} != 10 и {b} <= {a}')

# try:
#     a = int(input('Enter number A: '))
#     b = int(input('Enter number B: '))
#     # c = []
#     # print(c[100])  # IndexError
#
#     print(a / b)
# except ZeroDivisionError as e:
#     print(f'Деление на ноль! {e}')
# except ValueError as e:
#     print(f'Неверно указано число! {e}')

# a = int(input('Enter number: '))

# if a % 2 == 0:
#     print('Верно')
# else:
#     print('Неверно')

# print('Верно' if a % 2 == 0 else 'Неверно')

# if a == 1:
#     print('1')
# elif a == 2:
#     print('2')
# else:
#     print('3')
#
# print('1' if a == 1 else '2' if a == 2 else '3')


# i = 0
#
# while i < 50:
#     i += 1
#     print(f'i = {i}')

"""
Запросить у пользователя число N, вывести все числа от 0 до N которые делятся на 3.
"""

# N = int(input('Enter number: '))  # 5
# i = 0
#
# while i < N:
#     i += 1
#     if i % 3 == 0:
#         print(i)
#     if i == 10:
#         break
# else:
#     print('Done')
#
# print('END')

# N1 = N2 = 1
# N1, N2 = 1, 1
# while True:
#     symbol = input('Enter symbol: ')
#     if symbol == 'q':
#         break
#     N2 = N1 + N2
#     N1 += 1
#     if N2 % 2 == 0:
#         continue
#     print(N2)


# for i in 10, -2, 33, 334, -500:
#     print(f' i = {i}')
# c = 10, -2, 33, 334, -500
# print(type(c))
# for i in 'Hello world':
#     print(f' i = {i}')

# for i in [10, -2, 33, 334, -500]:
#     print(f' i = {i}')

# range(10) - 0 до 10 (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
# range(4, 10) - 4 до 10 (4, 5, 6, 7, 8, 9)
# range(0, 10, 2) - 0 до 10 (0, 2, 4, 6, 8)
# range(10, 0, -1) - 10 до 0 (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)

# for i in range(10, 0, -1):
#
#     if i % 2 != 0:
#         break
#     print(i)

# a = 0
# b = 1
#
# for i in a, b:
#     i += 1
#
# print(a, b)


# for _ in range(10):
#     print('Hello', _)

"""
1) Пользователя вводит два числа A и B, нужно вывести сумму чисел в диапазоне от A до B.
2) Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.

3) Запросить у пользователя число N - ширина треугольника.

Задание максимум на 80 баллов:

3.1) Вывести треугольник #1 с шириной N с помощью цикла
3.2) Вывести треугольник #2 с шириной N с помощью цикла
Задание со звездочкой:

3.3) Вывести треугольник #3 с шириной N с помощью цикла
3.4) Вывести треугольник #4 с шириной N с помощью цикла
"""

