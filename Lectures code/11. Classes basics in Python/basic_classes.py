"""
1. Paradigms (procedure, OOP). Why they changed?
2. Basic syntax of class
3. What is class and class instance. Difference.
4. Members (attributes) of class.
5. How to create instance
6. How class fields are distributed (mutable, immutable). Overriding class field in instance.
7. Methods.
8. Static methods
9. Class methods.
10. Advanced on instance creation. __init__ vs __new__
11. Adding attributes dynamically
"""

# import comments
# comments.mapping = None
#
# lst = [["John", 32], ["Ann", 18]]
# print(comments.convert_list_to_dict(lst))

# name = "John"
# age = 34
#
# name2 = "Anna"
# age2 = 34
#
# persons = [{"name": "John", "age": 34},{"name": "Johnddd", "age": 34}]
# def get_ages(persons):
#     return [p['age'] for p in persons]
#
# print(get_ages(persons))


# class Human:
#     name = "John"
#
# print(Human)
# john = Human()
# print(john)
# print(john.name)
# ann = Human()
# print(ann.name)

# class Human:
#
#     def __init__(self, name, age=16):
#         print(self)
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#
# igor = Human("Igor")
# print(igor.age)
#
# #oksana = Human()  # Error
#
# john = Human("John", 54)
# print(john)
# print(john.get_name())
# print(john.name)
#anna = Human("Anna", 12)
#
# class Cat:
#     name = "Murzik"
#
# m1 = Cat()
# print(m1.name)
# print(id(m1))
# m2 = Cat()
# print(m2.name)
# print(id(m2))
# print(type(m1))
# print(isinstance(john, Human))
# print(isinstance(john, Cat))

# class Test:
#
#     class_mutable_field = []
#     class_immutable_field = 333
#
#     def __init__(self, instance_field):
#         self.instance_field = instance_field
#
# t1 = Test(111)
# t2 = Test(222)

# print(t1.instance_field)
# print(t2.instance_field)
# t1.instance_field = 111999
# print(t1.instance_field)
# print(t2.instance_field)

# print(t1.class_mutable_field)
# print(t2.class_mutable_field)
# print(Test.class_mutable_field)
#
# t1.class_mutable_field.append("qqqq")
# print(t1.class_mutable_field)
# print(t2.class_mutable_field)
# print(Test.class_mutable_field)
#
# t2.class_mutable_field.append("tttt")
# print(t1.class_mutable_field)
# print(t2.class_mutable_field)
# print(Test.class_mutable_field)
#
# Test.class_mutable_field.append("vvvvvv")
# print(t1.class_mutable_field)
# print(t2.class_mutable_field)
# print(Test.class_mutable_field)

# print(t1.class_immutable_field)
# print(t2.class_immutable_field)
# print(Test.class_immutable_field)
# print()
#
# t1.class_immutable_field = 444
# print(t1.class_immutable_field)
# print(t2.class_immutable_field)
# print(Test.class_immutable_field)
# print()
#
# Test.class_immutable_field = 555
# print(t1.class_immutable_field)
# print(t2.class_immutable_field)
# print(Test.class_immutable_field)
# print()
#
# t2.class_mutable_field = "44534524"
# print(t1.class_mutable_field)
# print(t2.class_mutable_field)
# print(Test.class_mutable_field)

# print(t1.__dict__)
# t1.class_mutable_field = 444
# print()
# print(t1.__dict__)


# class Human:
#
#     planet = "Earth"
#
#     def __init__(self, name, age):
#         #print(self)
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def set_name(self, new_name):
#         print("Update name")
#         self.name = new_name
#
#     def print_human(self):
#         print(f"{self.name}, {self.age}")
#
#
#     # def hello():
#     #     print("Hello")
#
#     @staticmethod
#     def get_year_sign(year):
#         return "Tiger"
#
#     def another(self):
#         print("Good bye")
#
#
#     @classmethod
#     def create_human_with_height(cls, name, age, height):
#         print(cls)
#         instance = cls(name, age)
#         print(instance)
#         instance.height = height
#         return instance
#
#     @classmethod
#     def set_planet(cls, new_planet):
#         cls.planet = new_planet
#
# john = Human("John", 34)
# john.print_human()
# john.set_name("Andrew")
# john.print_human()
# john.name = "Johnny"
#
# john.print_human()
# #john.hello()
# anna = Human("Anna", 24)
#
# # print(john.get_year_sign(2022))
# # print(anna.get_year_sign(2022))
# # print(Human.get_year_sign(2022))
#
# edvard = Human.create_human_with_height("Edvard", 33, 170)
# edvard.print_human()
# print(edvard.height)
# print(edvard.planet)
#
#
# Human.set_planet("Mars")
# print(edvard.planet)
# print(john.planet)

# class Human:

    # def __new__(cls, *args, **kwargs):
    #     instance = super().__new__(cls)


#     def __init__(self, name, age):
#             print(self.__dict__)
#             self.name = name
#             self.age = age
#             self.height = None
#
#     def hello(self):
#         self.height = 30
#         print("Hello")
#
# robin = Human("Robin", 65)
# print(robin.__dict__)
# robin.hello()
# Human.hello(robin)

# instance = object.__new__(Human)
# print(instance)
# print(instance.__dict__)
# instance.__init__("RRR", 34)
# print(instance.__dict__)

# robin.address = "Kharkiv"
# print(robin.address)
# print()
#
# def set_name(self, new_name):
#     self.name = new_name
#
# print(robin.name)
# #robin.set_name = set_name
# #robin.set_name(robin, "Andrew")
# from types import MethodType
# robin.set_name = MethodType(set_name, robin)
# robin.set_name("Andrew")
# print(robin.name)
