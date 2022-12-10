# Написать функцию, которая возвращает слуайную строку заданной длины.
# Строка должна состоять из больших и маленьких латинских букв и цифр.

# Решение 1. С помощью random.choice
# import random
# import string
#
#
# def get_random_string(length: int) -> str:
#     character = string.ascii_letters + string.digits
#     rand_string = ''.join(random.choice(character) for _ in range(length))
#     return rand_string
#
#
# length = int(input("Введите длину строки: "))
# print(get_random_string(length))


# Решение 2. Неповторяющиеся значения с помощью random.sample
# import random
# import string
#
# def get_random_string(length):
#     character = string.ascii_letters + string.digits
#     rand_string = ''.join(random.sample(character, length))
#     return rand_string
#
#
# length = int(input("Введите длину строки: "))
# print(get_random_string(length))

