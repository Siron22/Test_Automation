# Написать функцию, которая возвращает слуайную строку заданной длины.
# Строка должна состоять из больших и маленьких латинских букв и цифр.

# Решение. С помощью втроенной функции chr, которая возвращает случайный символ из диапазона ASCII кодов.
import random
def get_random_string(length: int) -> str:
    rand_string = ''
    for _ in range(length) :
        low_case = random.randint(97, 122)
        up_case = random.randint(65, 90)
        numbers = random.randint(48, 57)
        character = [low_case, up_case, numbers]
        a = chr(random.choice(character))
        rand_string += a
    return rand_string

length = int(input("Введите длину строки: "))
print(get_random_string(length))


