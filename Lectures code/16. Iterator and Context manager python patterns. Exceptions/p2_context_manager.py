"""
Прямое обращение к файлу: открыть -> читать -> закрыть. Для каждого действия отдельная команда.
** Если в процессе обработки возникнет ошибка файл будет висеть в памяти до завершения работы приложения
"""
# file = open("__init__.py", 'r')
#
# print(file.read())
#
# file.close()

"""
Можно решить эту проблему путём добавления конструкции try.... и файл будет закрыть в любом случае
"""
# try:
#     file = open("__init__.py", 'r')
#     print(file.read())
# finally:
#     file.close()

"""Второй вариант использовать встроенный контекстный менеджер Питона with (синтаксический сахар), 
который также закроет файл после завершения работы
"""
# with open("__init__.py", 'r') as file:
#     print(file.read())


"""
Создание класса, который имитирует поведение файла и может быть использован с оператором with
"""
# class MockFile:
#
#     def __init__(self, name, mode='r'):
#         self.name = name
#         self.mode = mode
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         pass
#
#     def read(self):
#         return "TEST DATA"

"""
Для работы с этим виртуальным файлом переопределяем встроенную функцию open
Например, если имя файла test.txt, то запускается класс MockFile, если имя другое - стандартная работа с файловой системой
"""
# builtin_open = open
# def open(name, mode='r'):
#     if name == 'test.txt':
#         return MockFile("test.txt")
#     else:
#         return builtin_open(name, mode)
#
#
# with open("test.txt") as file:
#     print(file.read())

""""
Контекстный менеджер применяется:
 - при невозможности/нежелании работы с файловой системой
 - для хранения данных в одном месте, а не разбросанном по разным файлам
 - при выполнении парных операций: открыть/закрыть, засетать/сбросить, при многопоточном программировании
"""
########################################################################

"""
Создание конструкции контекст менеджера через генераторы
"""

from contextlib import contextmanager
"""
импорт встроенного менеджера из библиотеки. Работает как декоратор
"""

@contextmanager
def file(name, mode='r'):
    try:
        file_obj = open(name, mode)
        yield file_obj
    finally:
        file_obj.close()

with file("__init__.py") as f:
    print(f.read())
