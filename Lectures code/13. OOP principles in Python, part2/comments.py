"""
- Hiding
- Encapsulation
- Polymorphism
- Interfaces
- UML. Class diagram
"""

#Не надо объявлять переменные которые инициализируются в цикле
# i = 0
# for i in range(20):
#     print(i)
# print()
# print(i)


# Данные которые относятся к функции хранить внутри функции. Если это конфигурационный параметр, то передавать в функцию


# # Docstrings
def print_every_3_item(lst):
    """Prints every 3rd item of provided list"""
    MULTIPLICATOR = 3
    for i, value in enumerate(lst):
        if i % MULTIPLICATOR == 0:
            print(i)

print(print_every_3_item.__doc__)
#
# print_every_3_item(range(10))


# def print_every_n_item(lst, multiplicator=3):
#     """
#
#     :param lst:
#     :param multiplicator:
#     :return:
#     """
#     for i, value in enumerate(lst):
#         if i % multiplicator == 0:
#             print(i)
#
#
# m = 5
# print_every_n_item(range(30), 5)


from confluent_kafka import cimpl

# class field
# class A:
#
#     amount = 0
#
#     def __init__(self):
#         self.amount = 0