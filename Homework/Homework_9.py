# Написать функцию которая принимает целое число - number. Функция должна возвращать 'yes' если number является степенью двойки, иначе 'no'. Запрещено пользоваться функцией или оператором возведение в степень.
# Пример:
# is_power_of_two(256) # 'yes' потому что 2 в 8 степени это 256
# is_power_of_two(125) # 'no' потому что это не степень двойки

# Решение 1.1. Рекурсия

# def is_power_of_two(a: int, n=2) -> str:
#     if n > a :
#         print("NO")
#     elif n < a:
#         return is_power_of_two(a, n * 2)
#     else:
#         print("YES")
#
# a = int(input("Enter a number: "))
#
# is_power_of_two(a)

# Решение 1.2. Рекурсия. Не учитывает 0

# def is_power_of_two(a: int) -> str:
#     if type(a) == float:
#         print("NO")
#     elif a % 2:
#         return is_power_of_two(a / 2)
#     else:
#         print("YES")
#
# a = int(input("Enter a number: "))
#
# is_power_of_two(a)



# Решение 2. Цикл и умножение на два
# def is_power_of_two(a: int) -> str:
#     i = 1
#     while i < a:
#         i *= 2
#     if i == a:
#         print("YES")
#     else:
#         print("NO")
#
#
# a = int(input("Enter a number: "))
#
# is_power_of_two(a)

# Решение 3 и 4. С помощью бинарных операторов. Немного не понял, как работает сохраняю для себя
# def is_power_of_two(a: int) -> str:
#     if a & (a-1):
#         print("NO")
#     else:
#         print("YES")
#
#
# a = int(input("Enter a number: "))
#
# is_power_of_two(a)



# def is_power_of_two(a: int) -> str:
#     print(('NO', 'YES')[bin(a)[2:].count('1') == 1])
#
# a = int(input("Enter a number: "))
#
# is_power_of_two(a)