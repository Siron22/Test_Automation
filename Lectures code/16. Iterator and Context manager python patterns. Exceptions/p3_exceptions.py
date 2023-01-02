"""
- Exceptions
  - Alternatives for exceptions
  - Exceptions handling syntax
  - General exceptions hierarchy
  - except/Exception
  - Order of exception catching
  - Raising custom exceptions
  - Exceptions propagating (raise statement)
  - "raise from" statement
"""

# def div(a, b):
#     if b == 0:
#         return 0, False
#     return a / b, True
# print(div(2, 0))
#
# import os
# print(os.system("gi --version"))

# def add(a, b):
#     return a + b
#
# try:
#    add(1, [1,3])
#    # add(1, 2)
# except:                 # блок except выполняется когда во время выполнения допущена ошибка
#     print("In except")
# else:                   # блок else выполняется когда функция отработала успешно
#     print("In else")
# finally:                # блок finally выполняется всегда по окончанию выполнения кода независимо от результата
#     print("In finally")

# try:
#     input("Enter")
# except Exception:       # в блоке except принято указывать конкретное исключение для ошибки
#     print("IN EXCEPT")

"""
*** В широком понятии Exception используется для прогона и проверки правильности написания большого количества тестов.
Даже при наличии ошибок программа не прервется и все скрипты пройдут, а ошибки можно отдельно залогировать в файл
"""

# try:
#     raise ValueError("Incorrect value")
#     1/0
# except (ValueError, ZeroDivisionError) as e:
"""
если предусмотрена одна реакция система на различные виды ошибок, их можно перечислить в скобках
"""
#     print(e)
#     print("Exception caught")

"""
если для каждого вида ошибок свой код для них нужно создать отдельные блоки except.
*** ОБЯЗАТЕЛЬНО учитывать старшинство классов исключений. Например:
- Exception как самый общий класс перехватит абсолютно все ошибки если будет наверху;
- ArithmeticError является родительским классом для ZeroDivisionError и перехватит его если будет выше
"""
# try:
#     raise ValueError("Incorect value")
#     1/0
# except Exception:
#     print("In Exception")
# except ArithmeticError as e:
#     print("In Ar Err")
#     print(e)
# except ZeroDivisionError as e:
#     print("In Zero")
#     print(e)
# except ValueError as e:
#     print("In VAlue")
#     print(e)

"""
Кастомное исключение можно создать путем написания класса, который будет наследоваться от максимально близкого 
по значению встроенного класса исключений
"""
# class ParsingError(Exception):
#
#     def __init__(self, file, line):
#         self.file = file
#         self.line = line
#
#     def __str__(self):
#         return f"ParsingError in file '{self.file}' on line {self.line}"
#
#     def log_error(self):
#         pass
#
#
# try:
#     #raise ParsingError
#     raise ParsingError("data.txt", 23)
# except ParsingError as e:
#     e.log_error()
#     print(e)

# try:
#     1/0
# except ZeroDivisionError:
#     print("Processing error")
#     raise

"""
Используя конструкцию "except ...Error as e" можно сформировать исключение, которое стало причиной основной ошибки
"""
# try:
#     1/0
# except ZeroDivisionError as e:
#     print("Processing error")
#     raise ValueError("Parameter was equal 0") from e