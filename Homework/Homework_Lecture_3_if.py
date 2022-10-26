# 1. Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no
# 2. Пользователь вводит с клавиатуры три числа в переменные a, b, c.
# Найдите наибольшее число из них и запишите в переменную max.

# a = int(input('Enter number A: '))
# b = int(input('Enter number B: '))
# c = int(input('Enter number C: '))
#
# Ответ 1
# if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
#     print('Yes')
# else:
#     print('No')

# Ответ 2. Решение с помощью словия if
# if a > b and a > c :
#     max = a
#     print(max)
# elif b > a and b > c:
#     max = b
#     print(max)
# else:
#     max = c
#     print(max)

# Ответ 2. Упрощенное решение с помощью оператора max
# max = max(a,b,c)
# print (max)


# 3. Пользователь вводит два числа A и B, нужно вывести сумму всех четных чисел в диапазоне от A до B.

# самое простое решение
# a = int(input('Enter number A: '))
# b = int(input('Enter number B: '))
# c = 0
# for i in range(a, b):
#     if i > 0 and i % 2 == 0:
#         c += i
# print(c)

# решение, которое предусматривает, что числа равны, либо второе число меньше первого
# a = int(input('Enter number A: '))
# b = int(input('Enter number B: '))
# c = 0
# if a < b:
#     for i in range(a, b):
#         if i > 0 and i % 2 == 0:
#             c += i
#     print(c)
# elif a > b:
#     for i in range(b, a):
#         if i > 0 and i % 2 == 0:
#             c += i
#     print(c)
# else:
#     print('числа равны попробуйте еще')

# Упрощенный вариант решения
# a = int(input('Enter number A: '))
# b = int(input('Enter number B: '))
# c = 0
# if a > b:
#     b, a = a, b
# elif a == b:
#     print('числа равны попробуйте еще')
# for i in range(a, b):
#     if i > 0 and not i % 2:  # конструкция Not i % 2 заменяет i % 2 == 0
#         c += i
# print(c)