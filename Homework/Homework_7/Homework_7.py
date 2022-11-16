# Задание 1 Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers

# Решение с учётом замечаний.
# numbers = []
# with open('HW_7-1.txt', 'r') as f:
#     f = f.read().split()
# for i in f:
#     if i.isdigit():
#         numbers.append(i)
# print(numbers)

# А это решение разобьёт весь текст по символам и найдёт цифры внутри слов. Правла вернет не числа, а отдельные цифры
# numbers = []
# with open('HW_7-1.txt', 'r') as f:
#     f = list(f.read())
# for i in f:
#     if i.isdigit():
#         numbers.append(i)
# print(numbers)



# Первоначальное рещение, которое не читывает число в конце строки
# with open('HW_7-1.txt', 'r') as f:
#     f = str(f.readlines())
# numbers = []
# for i in f.split():
#     if i.isdigit():
#         numbers.append(i)
# print(numbers)

# Задание 2 Запросить у пользователя текст и записать его в файл data.txt

# a = input('Enter text: ')
# with open('data.txt', 'w') as f:
#     f.write(a)

# Задание 3 Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел

# N = int(input('Enter number N: '))
# A = ''
# for i in range(N):
#     number = input(f'Enter integer № {i + 1}: ')
#     A += number + ' '
# with open('numbers.txt', 'w') as f:
#     f.write(A)

# Задание 4 Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число

# import random
# with open('random_numbers.txt', 'w') as f:
#     for _ in range (100) :
#         r_int = random.randint(1, 100)
#         f.writelines(f'{r_int}\n')

# Задание 5 Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю

# a = 0
# with open('HW_7-1.txt', 'r') as f:
#     f = f.read()
#     for i in f.split():
#         a += 1
# print(a)

# Задание 6 Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел

# with open('HW_7-3.txt', 'r') as f:
#     f = f.read()
#     f = list(map(int, f.split()))
# print(sum(f))


# Задание 7 Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
# 'в' - 20 раз

# import collections
# with open('HW_7-1.txt', 'r') as f:
#     f = f.read()
#     f = list(f.split())
# counter = collections.Counter(f)
# common_values = counter.most_common()
# for i in range(5) :
#     print(f'\'{common_values[i][0]}\''+' - ' + f'{common_values[i][1]}' + ' раз')





















# ДЛЯ МЕНЯ!!! Тут я игрался с .readlines(), который выдаёт не цельнуя строку, а список, в котором элементы - строки текста

# Решение № 1 работает корректно, но меня напрягает, что первый объект, который оно считает это не слово, а - "['Lorem"
# a = 0
# with open('HW_7-1.txt', 'r') as f:
#     f = str(f.readlines())
#     for i in f.split():
#         a += 1
# print(f.split())

# Решение № 2 Вытащил элементы из списка и склеил их в единую строку, a затем заново в список. Не нравится тем, что элементов может быть и 100 и 1000
# a = 0
# with open('HW_7-1.txt', 'r') as f:
#     f = f.readlines()
#     f = f[0] + f[1] + f[2] + f[3] + f[4]
#     for i in f.split():
#         a += 1
# print(a)

# Решение № 3 По сути то же самое что и № 2, только склейка строк с помощью цикла
# a = 0
# b = ''
# with open('HW_7-1.txt', 'r') as f:
#     f = f.readlines()
#     for i in range(len(f)):
#         b += f[i]
# for i in b.split():
#     a += 1
# print(a)

# Сумма чисел в файле через readlines
#with open('HW_7-3.txt', 'r') as f:
#     f = f.readlines()
# a = list(map(int, f[0].split()))
# print(sum(a))