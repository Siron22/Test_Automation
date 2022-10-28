# 1. Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'

# a = str(input('Enter number A: '))
# if a == a[::-1]:
#     print('+')
# else:
#     print('-')

# 2. Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'

# a = str(input('Enter a text: '))
# b = str(input('Enter a word to find: '))
# if b in a:
#     print('YES')
# else:
#     print('NO')

# 3. Пользователь вводит строку. Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки
# 'zzz'.

# a = str(input('Enter a text: '))
# if a.startswith('abc'):
#     a = a.replace('abc', 'www')
#     print(a)
# else:
#     a = a + "zzz"
#     print(a)

# 4. Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.

# Решение № 1 с помощью цикла for
# a = list(input('Enter a text: '))
# c = ''
# for x in a:
#     if x.isdigit():
#         continue
#     else:
#         c += x
# print(c)

# Решение № 2 с помощью фильтра
# a = list(input('Enter a text: '))
# b = list(filter(lambda x: x.isalpha() or x.isspace(), a))
# c = ''.join(b)
# print(c)

# 5 Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить, что в почте есть символ '@' и '.', и если это так, то вывести "YES", иначе "NO"

# Решение № 1 соответствует, но не проверяет действительно ли введен e-mail. Пропускает "@."
# a = str(input('Enter a text: '))
# if '@' in a and '.' in a:
#     print('YES')
# else:
#     print('NO')

# Решение № 2 с использованием регулярного выражения

# import re
# a = str(input('Enter a text: '))
# if re.match(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', a):  # регулярку честно спросил у гугла))
#     print('YES')
# else:
#     print('NO')
















# ДЛЯ МЕНЯ! это решение убирает не все цифры, если ни идут подряд. Можно добавить циклы для повтороного перебора,
# но это слишком усложняет код
# a = list(input('Enter a text: '))
# for x in a:
#     if x.isdigit():
#         a.remove(x)
# for x in a:
#     if x.isdigit():
#         a.remove(x)
# c = ''.join(a)
# for x in a:
#     if x.isdigit():
#         a.remove(x)
# c = ''.join(a)
# print(c)

# ДЛЯ МЕНЯ! Это решение наоборот отфильтровывает только цифры
# a = list(input('Enter a text: '))
# b = list(filter(lambda x: x.isdigit(), a))
# c = ''.join(b)
# print(c)
