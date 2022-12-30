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
#    #add(1, [1,3])
#    add(1, 2)
# except:
#     print("In except")
# else:
#     print("In else")
# finally:
#     print("In finally")

# try:
#     input("Enter")
# except Exception:
#     print("IN EXCEPT")


# try:
#     raise ValueError("INcorrect value")
#     1/0
# except (ValueError, ZeroDivisionError) as e:
#     print(e)
#     print("Exception caught")


# try:
#     #raise ValueError("Incoreect value")
#     1/0
# except Exception:
#     print("In Exception")
# except ZeroDivisionError as e:
#     print("In Zero")
#     print(e)
# except ArithmeticError as e:
#     print("In Ar Err")
#     print(e)
# except ValueError as e:
#     print("In VAlue")
#     print(e)

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


try:
    1/0
except ZeroDivisionError as e:
    print("Processing error")
    raise ValueError("Parameter was equal 0") from e