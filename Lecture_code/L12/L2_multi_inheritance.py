class Horse:
    name = "Chernysh"

    def __init__(self, speed):
        self.speed = speed


class Donkey:
    name = "Donny"

    def __init__(self, strength):
        self.strength = strength


class Mule(Horse, Donkey):

    def __init__(self, speed, strength):
        Horse.__init__(self, speed)
        Donkey.__init__(self, strength)


mule = Mule(120, 532)
print(mule.__class__)
print(mule.__class__.__name__)
print(Mule.__bases__)

print(mule.name)
print(mule.speed)
print(mule.strength)

"""
Donkey
^
Horse
^
Mule
^
mule_obj
"""