"""
1. Unit tests frameworks overview
2. Какие способы тестирования в Питон
3. Установка PyTest
4. Простой тест. Вывод консоли. pytest --help
5. Соглашение об именах
6. Где PyTest ищет тесты и способы запуска тестов. --collect-only опция
7. Assertions
8. Маркеры
9. Встроеннные маркеры
10. Опции для рана
11. Параметризированные тесты
12. Фикстуры
13. Встроенные фикстуры
14. Плагины
15. Конфигурационный файл
16. Организация тестов классами
"""

# # abstract methods
from abc import ABC, abstractmethod, abstractstaticmethod, abstractclassmethod, abstractproperty


class SomeClass(ABC):

    @abstractstaticmethod
    def static_method():
        pass

    @staticmethod
    @abstractmethod
    def another_static_method():
        pass

    @abstractproperty
    def property(self):
        pass

"""Порядок декорирования имеет значение. Снизу (первый) - абстракт, сверху (второй) - статик"""
    # # Error
    # @abstractmethod
    # @staticmethod
    # def one_more_static_method():
    #     pass


# Напомнить *args  в функциях

"""Лучше заранее определиться какие аргументы принимает функция, а если количество значений неизвестно лучше их 
помещать в список и передавать его в качестве аргумента.
 Если функция изначально предусматривает принятие *args, то нужно передавать распакованный список"""

def sum_income(*incomes):
    return sum(incomes[0])   # -> это неправильно

income = [1, 2, 4]
print(sum_income(income))

incomes = [1, 2, 4]
def sum_income1(incomes: list):
    return sum(incomes)
print(sum_income1(incomes))

def sum_income2(*income:int):
    return sum(income)
incomes = [1, 2, 4]
print(sum_income2(*incomes))
print(sum_income2(1, 3, 5))




def test_add_4_5():
    assert 1 == 1



