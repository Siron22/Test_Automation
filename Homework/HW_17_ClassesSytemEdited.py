"""Выбрать систему, которая может быть описана несколькими классами.
Описать исползуя классы и применить принципы ООП:
- Наследование
- Абстрактные классы и/или интерфейсы
- Сокрытие
- Инкапсуляция
У классов должно быть состояние (поля) и реализация поведения через методы.
Требований к типам полей (экземпляра/класса) и методов (экземпляра/класса/статические) нет,
по необходимости как вы видите.
Написать код который создает необходимые экземпляры и демонстрирует работу систему.
Ограничений на количество классов нет, но конечно их тут будет не пара.
Это задание на это и следующие занятие. Пока советую выбрать систему, и порисовать из чего она состоит."""
from abc import ABC, abstractmethod


class BuhgalterMixin:
    """Вспомогательный класс, предназначен для учёта количества зверей и птиц,
    проживающих на ферме, количества корма, необходимого чтобы их прокормить в течении года
    и колиство с/х продукции, которая будет получена по окончанию года"""
    farm_name = '"Happy animals"'
    animals_counter = 0
    birds_counter = 0
    hay_counter = 0
    corn_counter = 0
    eggs_counter = 0
    wool_counter = 0
    milk_counter = 0
    feather_counter = 0

    @staticmethod
    def result():
        """записывает в файл окончательный результат"""
        text = f'Farm ==== {BuhgalterMixin.farm_name} ===\n' \
               f'In our barn live {BuhgalterMixin.animals_counter} animals\n' \
               f'In our chickencoop live {BuhgalterMixin.birds_counter} birds\n' \
               f'For feed them we need {BuhgalterMixin.hay_counter} kg of hay and ' \
               f'{BuhgalterMixin.corn_counter} kg of corn\n' \
               f'We will receive:\n' \
               f'- {BuhgalterMixin.eggs_counter} eggs;\n' \
               f'- {BuhgalterMixin.wool_counter} of wool;\n' \
               f'- {BuhgalterMixin.milk_counter}l milk\n' \
               f'- {BuhgalterMixin.feather_counter} feather'
        with open('Farm.txt', 'w') as f:
            f.write(text)
        return text


class DomesticAnimal(ABC):
    """Абстрактный класс домашнего животного"""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def set_property_label(self):
        """Абстрактный метод для проставления "клейма сщбственности" на каждом из животных """
        pass


class Animal(DomesticAnimal, BuhgalterMixin):
    """Класс животных. Имеет наследуемое поле - имя, неизменяемые поля - жильё (хлев) и еда (сено),
    а также изменяемое поле для экземляров - количество сена для питания.
    Создать экзумпляр класса нельзя, для этого введён абстрактный метод say_hellо"""

    def __init__(self, name: str, hay: int):
        super().__init__(name)
        self.__home = "Barn"
        self.__food = "hay"
        self.hay = hay

    def welcoming(self):
        """Приветствуем животное в новом доме"""
        print(f"Welcome to yor new {self.__home}, {self.name}, here is your favorite {self.__food}!")

    def buy_animal(self):
        """Покупаем животное и селим в хлев. Учитываем необходимость в сене для питания"""
        BuhgalterMixin.animals_counter += 1
        BuhgalterMixin.hay_counter += self.hay

    @abstractmethod
    def say_hello(self):
        """Абстрактный метод выводит на экран звук животного"""
        pass


class Bird(DomesticAnimal, BuhgalterMixin):
    """Класс птиц. Имеет наследуемое поле - имя, неизменяемые поля - жильё (курятник) и еда (кукуруза),
    а также изменяемое поле для экземляров - количество кукурузы для питания.
    Создать экзумпляр класса нельзя, для этого введён абстрактный метод sing_hellо"""

    def __init__(self, name: str, corn: int):
        super().__init__(name)
        self.__home = "Chickencoop"
        self.__food = "Corn"
        self.corn = corn

    def welcoming(self):
        """Приветствуем животное в новом доме"""
        print(f"Welcome to your new {self.__home}, {self.name}, here is your favorite {self.__food}!")

    def buy_bird(self):
        """Покупаем птицу и селим в курятник. Учитываем необходимость в кукурузе и для питания"""
        BuhgalterMixin.birds_counter += 1
        BuhgalterMixin.corn_counter += self.corn

    @abstractmethod
    def sing_hello(self):
        """Абстрактный метод выводит на экран пение птиц"""
        pass


class Cow(Animal):
    """Создает животное корову с полями класса "животное" и собственным параметром - количество молока"""

    def __init__(self, name: str, hay: int, milk: int):
        super().__init__(name, hay)
        self.milk = milk
        print(f"Here is good cow {self.name}, \n"
              f"She eats {self.hay} of hay for a day and gives you {self.milk} l milk")

    def buy_cow(self):
        """Покупаем корову и селим в хлев. Учитываем необходимость в сене и сколько будем получать молока"""
        super().buy_animal()
        BuhgalterMixin.milk_counter += self.milk
        print(f"One more cow in a barn. We have now {BuhgalterMixin.animals_counter} animals")

    def say_hello(self):
        """Метод выводит на экран звук животного"""
        print('Mooooo')

    def set_property_label(self):
        """Клеймо собственности"""
        print(f'This cow {self.name} is the property of {BuhgalterMixin.farm_name} farm')


class Sheep(Animal):
    def __init__(self, name: str, hay: int, wool: int):
        """Создает животное овцу с полями класса "животное" и собственным параметром - количество шерсти"""
        super().__init__(name, hay)
        self.wool = wool
        print(f"Here is good sheep {self.name}, \n"
              f"She eats {self.hay} of hay for a day and gives you {self.wool} wool")

    def buy_sheep(self):
        """Покупаем овцу и селим в хлев. Учитываем необходимость в сене и сколько будем получать шерсти"""
        BuhgalterMixin.wool_counter += self.wool
        super().buy_animal()
        print(f"One more sheep in a barn. We have now {BuhgalterMixin.animals_counter} animals")

    def say_hello(self):
        """метод выводит на экран звук животного"""
        print('Beeeeee')

    def set_property_label(self):
        """Клеймо собственности"""
        print(f'This sheep {self.name} is the property of {BuhgalterMixin.farm_name} farm')


class Chicken(Bird):
    """Создает птицу курицу с полями класса "птица" и собственным параметром - количество яиц"""

    def __init__(self, name: str, corn: int, eggs: int):
        super().__init__(name, corn)
        self.eggs = eggs
        print(f"Here is good chicken {self.name}, \n"
              f"She eats {self.corn} of corn for a day and gives you {self.eggs} eggs")

    def buy_chicken(self):
        """Покупаем курицу и селим в курятник. Учитываем необходимость в кукурузе и сколько будем получать яиц"""
        BuhgalterMixin.eggs_counter += self.eggs
        super().buy_bird()
        print(f"One more chicken in a chickencoop. We have now {BuhgalterMixin.animals_counter} animals")

    def sing_hello(self):
        """метод выводит на экран пение птицы"""
        print('Coo-co-co')

    def set_property_label(self):
        """Клеймо собственности"""
        print(f'This chicken {self.name} is the property of {BuhgalterMixin.farm_name} farm')


class Duck(Bird):
    """Создает птицу утку с полями класса "птица" и собственным параметром - количество пуха"""

    def __init__(self, name: str, corn: int, feather: int):
        super().__init__(name, corn)
        self.feather = feather
        print(f"Here is good duck {self.name}, \n"
              f"She eats {self.corn} of corn for a day and gives you {self.feather} feather")

    def buy_duck(self):
        """Покупаем утку и селим в курятник. Учитываем необходимость в кукурузе и сколько будем получать пуха"""
        BuhgalterMixin.feather_counter += self.feather
        super().buy_bird()
        print(f"One more duck in a chickencoop. We have now {BuhgalterMixin.animals_counter} animals")

    def sing_hello(self):
        """метод выводит на экран пение птицы"""
        print('Ckrya-ckrya')

    def set_property_label(self):
        """Клеймо собственности"""
        print(f'This duck {self.name} is the property of {BuhgalterMixin.farm_name} farm')


Murka = Cow('Murka', 10, 15)
Murka.buy_cow()
Murka.welcoming()
Murka.say_hello()
Murka.set_property_label()
print('-----------------------')
Sheep1 = Sheep('Sheep1', 4, 16)
Sheep1.buy_sheep()
Sheep1.welcoming()
Sheep1.say_hello()
Sheep1.set_property_label()
print('-----------------------')
Ryaba = Chicken('Ryaba', 1, 1)
Ryaba.buy_chicken()
Ryaba.welcoming()
Ryaba.sing_hello()
Ryaba.set_property_label()
print('-----------------------')
Scrudj = Duck('Scrudj', 2, 6)
Scrudj.buy_duck()
Scrudj.welcoming()
Scrudj.sing_hello()
Scrudj.set_property_label()
print('-----------------------')
BuhgalterMixin.result()
print(BuhgalterMixin.result())

A = BuhgalterMixin()

print(A)
