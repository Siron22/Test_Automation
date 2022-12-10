# Написать функцию, которая возвращает слуайную строку заданной длины.
# Строка должна состоять из больших и маленьких латинских букв и цифр.

# 1. С помощью втроенной функции chr, которая возвращает случайный символ из диапазона ASCII кодов. Недостаток -
# включает спецсимволы
# import random
# def get_random_string(length: int) -> str:
#     rand_string = ''
#     for _ in range(length) :
#         a = chr(random.randint(65, 122))
#         rand_string += a
#     return rand_string
#
# print(get_random_string(23))

# 2. С помощью библиотек random & string
# import random
# import string
# letter = string.ascii_letters + string.digits
#
# def get_random_string(length: int) -> str:
#     rand_list = [''.join(random.choice(letter)) for _ in range(length)]
#     rand_string = ''.join(rand_list)
#     return rand_string


# length = int(input("Введите длину строки: "))
# print(get_random_string(length))

#
# 3. Библиотека secrets позволяет генерировать более безопасные комбинации
# import secrets
# import string
#
#
# def generate_alphanum_crypt_string(length):
#     letters_and_digits = string.ascii_letters + string.digits
#     crypt_rand_string = ''.join(secrets.choice(letters_and_digits) for i in range(length))
#     print("Cryptic Random string of length", length, "is:", crypt_rand_string)
#
#
# generate_alphanum_crypt_string(16)

# 4. Неповторяющиеся значения
# import random
# import string
#
#
# def generate_alphanum_random_string(length):
#     letters_and_digits = string.ascii_letters + string.digits
#     rand_string = ''.join(random.sample(letters_and_digits, length))
#     print("Alphanum Random string of length", length, "is:", rand_string)
#
#
# generate_alphanum_random_string(16)
