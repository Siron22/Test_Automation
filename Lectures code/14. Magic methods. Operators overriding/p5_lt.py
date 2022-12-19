class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __lt__(self, other):
    #     return self.age < other.age

    def lt(self, other):
        return self.age < other.age

    def __qqq__(self):
        print("sdsdsdsd")

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash(self.name)


john = Human("John", 56)
anna = Human("Anna", 33)
#print(john < anna)
print(john.lt(anna))

john.__qqq__()
print(hash(john))

d = {
    john: 2300
}

print(d)

s = set()
s.add(john)
print(john in s)
john.name = "Anna"
print(john in s)
print(s)