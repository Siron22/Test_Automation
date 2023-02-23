# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

class Person:

    object_number = 0

    def __new__(cls, *args, **kwargs):
        if Person.object_number >= 3:
            raise Exception("Exceeded number of objects")
        Person.object_number += 1
        return super().__new__(Person)

    def __init__(self, name, age):
        self.name = name
        self.age = age

# def object_limiter(max_object_number):
#     def decorator(cls):
#         cls.object_number = 0
#
#         class Wrapper:
#             def __init__(self, *args, **kwargs):
#                 if cls.object_number >= max_object_number:
#                     raise Exception("Exceeded number of objects")
#                 cls.object_number += 1
#                 self.wrapped = cls(*args, **kwargs)
#
#             def __getattr__(self, name):
#                 return getattr(self.wrapped, name)
#
#             def __del__(self):
#                 cls.object_number -= 1
#
#         return Wrapper
#     return decorator
#
#
# @object_limiter(3)
# class Person:
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age




p1 = Person("John", 34)
p2 = Person("Anna", 25)
p3 = Person("Andrew", 32)
del p3
p4 = Person("Ira", 53)
# try:
#     p5 = Person("Ira", 53)
      #save_to_db(p5)
# except:
#     pass
a = 3