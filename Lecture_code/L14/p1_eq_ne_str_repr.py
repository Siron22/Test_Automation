from __future__ import annotations


class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other: User):
        if not isinstance(other, User):
            return False
        if self is other:
            return True
        return self.name == other.name and self.age == other.age

    def __ne__(self, other):
        return not (self.name == other.name and self.age == other.age)

    def __str__(self):
        return f"class {self.__class__.__name__}:\nname: {self.name}\nage: {self.age}"

    def __repr__(self):
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