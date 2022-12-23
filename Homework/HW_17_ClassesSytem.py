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


class Farm(ABC):
    """Абстрактный класс, предназначен для учёта количества зверей и птиц,
    проживающих на ферме, количества корма, необходимого чтобы их прокормить в течении года
    и колиство с/х продукции, которая будет получена по окончанию года"""
    name = '"Happy animals"'
    animals_counter = 0
    birds_counter = 0
    hay_counter = 0
    corn_counter = 0
    eggs_counter = 0
    meat_counter = 0
    wool_counter = 0
    milk_counter = 0
    feather_counter = 0

    text = f'In our barn live {animals_counter} animals\n' \
           f'In our chickencoop live {birds_counter} birds\n' \
           f'For feed them we need {hay_counter} kg of hay and {corn_counter} kg of corn\n' \
           f'We will receive:\n' \
           f'- {eggs_counter} eggs;\n' \
           f'- {wool_counter} of wool;\n' \
           f'- {meat_counter} kg meat:\n' \
           f'- {milk_counter}l milk\n' \
           f'- {feather_counter} feather'

    @staticmethod
    def result():
        """записывает в файл окончательный результат"""
        with open('text.txt', 'w') as f:
            f.write(Farm.text)
        return Farm.text

    def set_property_label(self):
        print(f'This is the property of {Farm.name} farm')


class Animals(Farm):
    """Класс животных. Имеет неизменяемые поля - жильё и еда,
    а также изменяемые поля для экземляров - имя и количество сена для питания"""

    def __init__(self, name: str, hay: int):
        self.__home = "Barn"
        self.__food = "hay"
        self.hay = hay
        self.name = name

    def welcoming(self):
        """Приветствуем животное в новом доме"""
        print(f"Welcome to yor new {self.__home}, {self.name}, here is your favorite {self.__food}!")

    @abstractmethod
    def say_hello(self):
        """метод выводит на экран звук животного"""
        print('Everybody sounds great')  # Вот не понял я нужно ли здесь что-то печатать если
        # все равно это значение не вызывается


class Birds(Farm):
    """Класс птиц. Имеет неизменяемые поля - жильё и еда,
        а также изменяемые поля для экземляров - имя и количество кукурузы для питания"""

    def __init__(self, name: str, corn: int):
        self.__home = "Chickencoop"
        self.__food = "Corn"
        self.name = name
        self.corn = corn

    @abstractmethod
    def sing_hello(self):
        """метод выводит на экран пение птиц"""
        print('Everybody sounds great')

    def welcoming(self):
        """Приветствуем животное в новом доме"""
        print(f"Welcome to your new {self.__home}, {self.name}, here is your favorite {self.__food}!")


class Cow(Animals):
    """Создает животное корову с полями класса животное и собственным параметром - количество молова"""

    def __init__(self, name: str, hay: int, milk: int):
        super().__init__(name, hay)
        self.milk = milk
        print(f"Here is goog cow {self.name}, \n"
              f"She eats {self.hay} of hay for a day and gives you {self.milk} l milk")

    def buy_cow(self):
        """Покупаем корову и селим в хлев учитываем необходимость в сене и сколько будем получать молока"""
        Farm.animals_counter += 1
        Farm.milk_counter += self.milk
        Farm.hay_counter += self.hay
        print(f"One more cow in a barn. We have now {Farm.animals_counter} animals")

    def say_hello(self):
        """метод выводит на экран звук животного"""
        print('Mooooo')


class Pig(Animals, Birds):
    """Создает животное свинью, которая живет в сарае, как животное, но ест кукурузу, как птица,
     имеет собственный параметр - количество мяса"""

    def __init__(self, name: str, corn: int, meat: int):
        super().__init__(name, corn)
        self.meat = meat
        print(f"Here is goog pig {self.name}, \n"
              f"She eats {self.hay} of corn for a day and gives you {self.meat} kg meat")

    def buy_pig(self):
        """Покупаем свинью и селим в хлев учитываем необходимость в кукурузе и сколько будем получать мяса"""
        Farm.animals_counter += 1
        Farm.meat_counter += self.meat
        Farm.corn_counter += self.hay
        print(f"One more pig in a barn. We have now {Farm.animals_counter} animals")

    def say_hello(self):
        """метод выводит на экран звук животного"""
        print('Hru-Hru')

    def sing_hello(self):
        pass


class Sheeps(Animals):
    def __init__(self, name: str, hay: int, wool: int):
        """Создает животное овцу с полями класса животное и собственным параметром - количество шерсти"""
        super().__init__(name, hay)
        self.wool = wool
        print(f"Here is goog sheep {self.name}, \n"
              f"She eats {self.hay} of hay for a day and gives you {self.wool} wool")

    def buy_sheep(self):
        """Покупаем овцу и селим в хлев учитываем необходимость в сене и сколько будем получать шерсти"""
        Farm.animals_counter += 1
        Farm.wool_counter += self.wool
        Farm.hay_counter += self.hay
        print(f"One more sheep in a barn. We have now {Farm.animals_counter} animals")

    def say_hello(self):
        """метод выводит на экран звук животного"""
        print('Beeeeee')


class Chicken(Birds):
    def __init__(self, name: str, corn: int, eggs: int):
        super().__init__(name, corn)
        self.eggs = eggs
        print(f"Here is goog chicken {self.name}, \n"
              f"She eats {self.corn} of corn for a day and gives you {self.eggs} l milk")

    def buy_chicken(self):
        Farm.animals_counter += 1
        Farm.eggs_counter += self.eggs
        Farm.corn_counter += self.corn
        print(f"One more chicken in a chickencoop. We have now {Farm.animals_counter} animals")

    def sing_hello(self):
        """метод выводит на экран звук животного"""
        print('Coo-co-co')


class Duck(Birds):
    def __init__(self, name: str, corn: int, feather: int):
        super().__init__(name, corn)
        self.feather = feather
        print(f"Here is goog duck {self.name}, \n"
              f"She eats {self.corn} of corn for a day and gives you {self.feather} feather")

    def buy_duck(self):
        Farm.animals_counter += 1
        Farm.feather_counter += self.feather
        Farm.corn_counter += self.corn
        print(f"One more duck in a chickencoop. We have now {Farm.animals_counter} animals")

    def sing_hello(self):
        """метод выводит на экран звук животного"""
        print('Ckrya-ckrya')


Murka = Cow('Murka', 10, 15)
Murka.buy_cow()
Murka.welcoming()
Murka.say_hello()
Murka.set_property_label()
print('-----------------------')
Pig1 = Pig('Pig1', 7, 120)
Pig1.buy_pig()
Pig1.welcoming()
Pig1.say_hello()
print('-----------------------')
Sheep1 = Sheeps('Sheep1', 4, 16)
Sheep1.buy_sheep()
Sheep1.welcoming()
Sheep1.say_hello()
print('-----------------------')
Ryaba = Chicken('Ryaba', 1, 1)
Ryaba.buy_chicken()
Ryaba.welcoming()
Ryaba.sing_hello()
print('-----------------------')
Scrudj = Duck('Scrudj', 2, 6)
Scrudj.buy_duck()
Scrudj.welcoming()
Scrudj.sing_hello()
print('-----------------------')
print(f'Farm.animals_counter: {Farm.animals_counter}')
print(f'Farm.milk_counter: {Farm.milk_counter}')
print(f'Farm.hay_counter: {Farm.hay_counter}')
print(f'Farm.corn_counter: {Farm.corn_counter}')
print(f'Farm.eggs_counter: {Farm.eggs_counter}')
print(f'Farm.wool_counter: {Farm.wool_counter}')
print(f'Farm.feather_counter: {Farm.feather_counter}')
print('-----------------------')
Farm.result()
print(Farm.result())
