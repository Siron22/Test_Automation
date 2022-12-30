class AttributeDescriptor:

    def __get__(self, instance, owner):
        print(f"{self}\n{instance}\n{owner}")
        return 43

    def __set__(self, instance, value):
        raise AttributeError("Readonly field")


    # def __delete__(self, instance):
    #     pass

class A:
    attr = AttributeDescriptor()


a = A()

print(A.attr)

print(a.attr)
print(a.__dict__)
a.attr = 4
print(a.attr)
print(a.__dict__)

import datetime
class AgeDescriptor:

    def __get__(self, instance, owner):
        print(f"{self}\n{instance}\n{owner}")
        return datetime.datetime.now().year - instance.birth_year

    def __set__(self, instance, value):
        raise AttributeError("Readonly field")


class Person:

    age = AgeDescriptor()

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

p = Person("Anna", 1987)
print(p.age)