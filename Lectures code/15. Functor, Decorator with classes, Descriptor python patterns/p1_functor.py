# class Multiply:
#
#     def __init__(self, multiplator):
#         self.multiplator = multiplator
#
#     def multiply(self, number):
#         return number * self.multiplator
#
# mul5 = Multiply(5)
# print(mul5.multiply(67))
# print(callable(mul5))
# mul5() # error


class Multiply:

    def __init__(self, multiplator):
        self.multiplator = multiplator

    def __call__(self, number):
        """придаёт экземпляру свойство callable и позволяет вызывать его не обращаясь к методу
        Удобно использовать:
         - когда в классе только один метод для сокращения кода
         - в качестве декоратора (превращает класс в функцию)"""
        return number * self.multiplator


mul5 = Multiply(5)
print(mul5(67))
print(callable(mul5))

print(type(mul5))

"""передача функции через вызываемый класс:
- позволяет хранить данные внутри класса без необходимости сохранения в глобальную зону видимости
"""

def perform_action(func, op1, op2):
    return func(op1, op2)


class Action:

    def __init__(self, operation):
        self.operation = operation

    def __call__(self, op1, op2):
        if self.operation == 'add':
            return op1 + op2
        elif self.operation == 'sub':
            return op1 - op2
        elif self.operation == 'mlp':
            return op1 * op2
        elif self.operation == 'div':
            return op1 / op2
        else:
            raise Exception("Unknown operation")

add = Action('add')
print(perform_action(add, 4, 8))