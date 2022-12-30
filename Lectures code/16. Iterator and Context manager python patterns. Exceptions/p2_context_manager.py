# file = open("__init__.py", 'r')
#
# print(file.read())
#
# file.close()

# try:
#     file = open("__init__.py", 'r')
#     print(file.read())
# finally:
#     file.close()

# with open("__init__.py", 'r') as file:
#     print(file.read())

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
#
#
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

from contextlib import contextmanager

@contextmanager
def file(name, mode='r'):
    try:
        file_obj = open(name, mode)
        yield file_obj
    finally:
        file_obj.close()

with file("__init__.py") as f:
    print(f.read())