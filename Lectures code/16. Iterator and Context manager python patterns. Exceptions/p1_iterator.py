# a = [1,2,3]
# """Итератор - предназначен для последовательного прохода по значению"""
# a_iter = iter(a) # встроенная функция итератора
# print(next(a_iter))
# for i in a:
#     print(i)
# print()
# for i in a:
#     print(i)


# class SquareIterator:
#     """Создание своего итератора с помощью магических методов"""
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.current = start
#
#     def __iter__(self):
#         """вызывает встроенный итератор"""
#         print("In __iter__")
#         return self
#
#     def __next__(self):
#         """возвращает значения элементов. В данном случае - пока текущее значение в диапазоне заданных
#         возвращается его значение в квадрате"""
#         print("In __next__")
#         if self.current < self.stop:
#             result = self.current ** 2
#             self.current += 1
#             return result
#         else:
#             """исключение, которая сигналит обо окончании последоватеьности"""
#             raise StopIteration
#
# sq = SquareIterator(2, 5)
#
# """При использованни for мы будем сразу проходить по всему циклу значений"""
# for i in sq:
#     print(i)
#
# print()

"""повторный проход по значениям невозможен в рамках одного запуска (далее как решить)"""
# for i in sq:
#     print(i)

"""используя команды iter и вызов next мы будем последовательно вызывать следующее значение последовательности"""
# sq_iter = iter(sq)
# print(next(sq_iter))
# print(next(sq_iter))
# print(next(sq_iter))
# print(next(sq_iter))

"""
***Генератор класса более мощный иструмент, по сравнению с функцией и используется когда необходимо к итерируемым 
элементам применить несколько методов и сохранять состояния и данные
"""

#####################################################3

# class SquareIterator:
#     """
#     Для неограниченного прохода по итерируемому объекту можно в методе __iter__ возвращать не self,
#     а весь объявленный класс - используем рекурсию класса
#     *** метод __next__ становится излишним. Можно разбить итератор на два класса (ниже)
#     """
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#         self.current = start
#
#     def __iter__(self):
#         #print("In __iter__")
#         return SquareIterator(self.start, self.stop)
#
#     def __next__(self):
#         #print("In __next__")
#         if self.current < self.stop:
#             result = self.current ** 2
#             self.current += 1
#             return result
#         else:
#             raise StopIteration
#
#
# sq = SquareIterator(2, 5)
#
# for i in sq:
#     print(i)
#
# print()
#
# for i in sq:
#     print(i)

#####################################################3
"""разбиваем итератор на два класса"""

# class SquareIteratorLogic:
#     """Этот итератор нужен для перебора элементов"""
#     def __init__(self, start, stop):
#         self.current = start
#         self.stop = stop
#
#     def __next__(self):
#         #print("In __next__")
#         if self.current < self.stop:
#             result = self.current ** 2
#             self.current += 1
#             return result
#         else:
#             raise StopIteration


# class SquareIterator:
#     """Этот итератор вызывает перебор элементов в качестве класса"""
#     def __init__(self, start, stop):
#         self.start = start
#         self.stop = stop
#
#     def __iter__(self):
#         #print("In __iter__")
#         return SquareIteratorLogic(self.start, self.stop)
#
#
# sq = SquareIterator(2, 5)
#
# for i in sq:
#     print(i)
#
# print()
#
# for i in sq:
#     print(i)

#####################################################3
"""
Возникает проблема при ручном переборе элементов в случае создания нескольких экземпляров класса
так как счётчик итерируемых объектов остаётся один на все экземпляры
"""

class SquareIterator:

    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        #self.current = start

    def __iter__(self):
        #print("In __iter__")
        self.current = self.start
        return self

    def __next__(self):
        #print("In __next__")
        if self.current < self.stop:
            result = self.current ** 2
            self.current += 1
            return result
        else:
            raise StopIteration


sq = SquareIterator(2, 5)

for i in sq:
    print(i)

print()

for i in sq:
    print(i)

sq_iter1 = iter(sq)


print(f"1: {next(sq_iter1)}")

sq_iter2 = iter(sq)
print(f"1: {next(sq_iter1)}")

print(f"2: {next(sq_iter1)}")