from typing import List


def read_csv(file_name: str) -> List[str]:
    file = open(file_name)
    result = file.readlines()
    return result


def generate_numbers():
    number = 0
    while True:
        number += 10
        yield number


# number_gen = generate_numbers()
# print(next(number_gen))
# print(next(number_gen))
# print(next(number_gen))
# print(next(number_gen))
# print(next(number_gen))


def read_csv_generator(file_name: str) -> str:
    line_count = 0
    for line in open(file_name):
        yield line
        line_count += 1
        print(f'Lines: {line_count}')


# gen = read_csv_generator('products.csv')
# apple_count = 0
#
# try:
#     while True:
#         val = next(gen)
#         if val.lower().find('apple') != -1:
#             apple_count += 1
# except StopIteration:
#     pass
# print(apple_count)
