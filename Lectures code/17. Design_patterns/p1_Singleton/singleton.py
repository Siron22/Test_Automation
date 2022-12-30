"GoF"

def singleton(cls):
    def wrapper(*args, **kwargs):
        if not hasattr(cls, 'instance'):
            setattr(cls, 'instance', cls(*args, **kwargs))
        return getattr(cls, 'instance')
    return wrapper


@singleton
class King:
    #instance = object of King

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def __str__(self):
        return f"King {self.name}, {self.health}"
#King = singleton(King)
print(type(King))


king1 = King('Richard IV', 100)
print(king1)
print(type(king1))
king2 = King('John III', 200)
print(king2)
print(king1 is king2)

# ##############################################################
# Another implementation of singleton but for specific class


class LastPersonOnTheEarth:

    instance = None

    def __new__(cls, *args, **kwargs):
        if LastPersonOnTheEarth.instance:
            return LastPersonOnTheEarth.instance
        else:
            instance = super().__new__(LastPersonOnTheEarth)
            return instance

    def __init__(self, name, age):
        if LastPersonOnTheEarth.instance:
            pass
        else:
            self.name = name
            self.age = age
            LastPersonOnTheEarth.instance = self

    def __str__(self):
        return f"Person: name: {self.name}, age: {self.age}"


john = LastPersonOnTheEarth("John", 34)
print(john)
anna = LastPersonOnTheEarth("Anna", 23)
print(anna)
print(john is anna)