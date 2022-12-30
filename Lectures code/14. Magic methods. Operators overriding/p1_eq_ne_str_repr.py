from __future__ import annotations


class User:

    def __init__(self, name, age):
        """
        Инициализатор класса. Ему передаётся всё, с чем был вызван первоначальный конструктор
        """
        self.name = name
        self.age = age

    def __eq__(self, other: User):
        """Определяет поведение оператора равенства, =="""
        if not isinstance(other, User):
            return False
        if self is other:
            return True
        return self.name == other.name and self.age == other.age

    def __ne__(self, other):
        """Определяет поведение оператора неравенства, != """
        return not (self.name == other.name and self.age == other.age)

    def __str__(self):
        """Определяет поведение функции str(), вызванной для экземпляра вашего класса."""
        return f"class {self.__class__.__name__}:\nname: {self.name}\nage: {self.age}"

    def __repr__(self):
        """Определяет поведение функции repr(), вызыванной для экземпляра вашего класса.
        Главное отличие от str() в целевой аудитории. repr() больше предназначен для машинно-ориентированного вывода
        (более того, это часто должен быть валидный код на Питоне), а str() предназначен для чтения людьми."""
        return f"{self.__class__.__name__}('{self.name}', {self.age})"

class A:
    pass




john1 = User("John", 34)
john2 = User("John", 34)
anna = User("Anna", 23)

a = A()

john1 == a


# print(john1 == john2)
# print(john1 == anna)
# print(john1 != anna)

print(john1)
users = [john1, john2, anna]
print(users)

string_repr = repr(john1)
print(string_repr)
restored_obj = eval(string_repr)
print(restored_obj == john1)

# import datetime
# now = datetime.datetime.now()
# print(str(now))
# print(repr(now))