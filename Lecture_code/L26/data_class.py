class User:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"User('{self.name}', {self.age})"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        else:
            return self.name == other.name and self.age == other.age

user1 = User('John Smith', 43)
user2 = User('John Smith', 43)
print(user1)
print(user1 == user2)


from dataclasses import dataclass

@dataclass()
class UserData:
    name: str
    age: int

    def greetings(self):
        print(f"Hello, {self.name}")

user3 = UserData('John Smith', 43)
user4 = UserData('John Smith', 43)
print(user3)
print(user3 == user4)
user4.greetings()
