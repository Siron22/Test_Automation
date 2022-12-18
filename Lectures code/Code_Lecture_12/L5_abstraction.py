from abc import ABC, ABCMeta, abstractmethod, abstractclassmethod, abstractstaticmethod


class Cat(metaclass=ABCMeta):

    def sleep(self):
        print("Sleeping...")

    @abstractmethod
    def meow(self):
        pass


class DomesticCat(Cat):
    def meow(self):
        print("Meow")


class Tiger(Cat):
    def meow(self):
        print("Rrrrr")



cat = Cat()
print(cat.meow())

domestic_cat = DomesticCat()
domestic_cat.meow()

tiger = Tiger()
tiger.meow()