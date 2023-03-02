from datetime import datetime

class Human:

    def __init__(self, name, birth_year):
        self.name =name
        self.birth_year = birth_year
        self.__health = 100

    # Using property function

    # def get_health(self):
    #     return self.__health
    #
    # def set_health(self, value):
    #     print("Somebody tries to set health")
    #     self.__health = value
    #
    # def del_health(self):
    #     print("He was overworking:(")
    #     del self.__health
    #
    # health = property(fget=get_health, fset=set_health, fdel=del_health, doc="This attribute is talking about unit's health")

    # Using decorator
    @property
    def health(self):
        """This attribute is talking about unit's health"""
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = value

    @health.deleter
    def health(self):
        print("He was overworking:(")
        del self.__health

    @property
    def age(self):
        return datetime.now().year - self.birth_year


anna = Human("Anna", 1985)
#print(anna.__health)
print(anna.health)
anna.health = 130
print(anna.health)
del anna.health
print(Human.health.__doc__)

print(anna.age)
#anna.age = 34
