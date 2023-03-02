"""
Binary operators: __add__, __radd__, __iadd__
Destructor: __del__
Bit operators: __and__, __or__
"""

class Horse:

    def __init__(self, speed, strength):
        self.speed = speed
        self.strength = strength

    # def __add__(self, other):
    #     return Mule(self.speed, other.strength)
    #
    # def __radd__(self, other):
    #     return Mule(self.speed, other.strength)

    def __and__(self, other):
        return self.speed * other.strength

    def __iadd__(self, other):
        return Mule(self.speed, other.strength)

    def __str__(self):
        return f"Horse speed: {self.speed}, strength: {self.strength}"

    def __del__(self):
        print("Removed")


class Donkey:

    def __init__(self, speed, strength):
        self.speed = speed
        self.strength = strength

    def __str__(self):
        return f"Donkey speed: {self.speed}, strength: {self.strength}"


class Mule:

    def __init__(self, speed, strength):
        self.speed = speed
        self.strength = strength

    def __str__(self):
        return f"Mule speed: {self.speed}, strength: {self.strength}"

horse = Horse(speed=10, strength=2)
donkey = Donkey(speed=1, strength=8)

# print(horse + donkey)
# print(donkey + horse)

#horse = horse + donkey
# horse += donkey
# print(horse)
print(horse & donkey)
