# Задание 1:
# Запросить у пользователя 5 чисел и записать их в список

# Решение № 1 с использованием цикла и метода append
# numbers_list = []
# for i in range(5):
#     number = int(input(f'Enter integer № {i + 1}: '))
#     numbers_list.append(number)
# print(numbers_list)

# Решение № 2, когда пользователь вводит сразу все цифры. Работает только для однозначных чисел
# a = list(input('Enter 5 numbers: '))
# if len(a) == 5:
#     a = list(map(int, a))
#     print(a)
# else:
#     print('You have to enter strictly 5 numbers. Try again')

# Задание 2: Дан список A = [1, 2, 3, 4, 5] Удалить последнее число из списка

# A = [1, 2, 3, 4, 5]
# A.pop()
# print(A)

# Задание 3: Запросить у пользователя 10 чисел и записать их в список A. Запросить у пользователя число N.
# Вывести пользователю сколько в списке A повторяется число N
# A = []
# for i in range(10):
#     number = int(input(f'Enter integer № {i + 1}: '))
#     A.append(number)
# N = int(input('Enter number N: '))
# print(A.count(N))

# Задание 4: Запросить у пользователя число N. Запросить у пользователя N чисел и записать их в список A.
# Вывести список в обратной последовательности
# N = int(input('Enter number N: '))
# A = []
# for i in range(N):
#     number = int(input(f'Enter integer № {i + 1}: '))
#     A.append(number)
# print(A[::-1])

# Задание 5: Запросить у пользователя 5 чисел и записать их в список A. Записать все числа из списка A которые больше 5 в список C
# A = []
# C = []
# for i in range(5):
#     number = int(input(f'Enter integer № {i + 1}: '))
#     A.append(number)
#     if number > 5:
#         C.append(number)
# print(A)
# print(C)

# Задание 6: Запросить у пользователя число N. Запросить у пользователя N целых чисел и записать их в список A.
# Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min, max, sorted, sort). Вывести эти числа.
# N = int(input('Enter number N: '))
# A = []
# for i in range(N):
#     number = int(input(f'Enter integer № {i + 1}: '))
#     A.append(number)
# max_ = A[0]
# for x in A:
#     if x > max_:
#         max_ = x
# print(f'Максимальное значениe: {max_}')
# min_ = A[0]
# for x in A:
#     if x < min_:
#         min_ = x
# print(f'Минимальное значениe: {min_}')

# Задание 7: Пользователь вводит текст нужно вывести количество чисел в этом тексте

# Решение № 1 путём создания переменной-"счётчика"
# a = input('Enter text: ')
# b = 0
# for i in a.split():
#     if i.isdigit():
#         b += 1
# print(b)

# Решение № 2 путём помещения всех числовых элементов в новый список и подсчетом его длины
# a = input('Enter text: ')
# b = []
# for i in a.split():
#     if i.isdigit():
#         b.append(i)
# print(len(b))

# Решение № 3 путём создания копии списка, удаления из неё числовых элементов и подсчёта разницы длин
# a = input('Enter text: ')
# a = a.split()
# b = a.copy()
# for i in b.copy():
#     if i.isdigit():
#         b.remove(i)
# print(len(a) - len(b))



