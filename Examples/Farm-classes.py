from abc import ABC, ABCMeta, abstractmethod, abstractclassmethod, abstractstaticmethod

class Farm(ABC):
    """Абстрактный класс, предназначен для учёта количества зверей и птиц,
    проживающих на ферме, количества корма, необходимого чтобы их прокормить в течении года
    и колиство с/х продукции, которая будет получена по окончанию года"""
    animal_counter = 0
    birds_counter = 0
    hay_counter = 0
    corn_counter = 0
    eggs_counter = 0
    meat_counter = 0
    wool_counter = 0
    milk_counter = 0



    # text = f'In our barn live {animal_counter} animals\n' \
    #        f'In our chickencoop live {birds_counter} birds\n' \
    #        f'For feed them we need {hay_counter} kg of hay and {corn_counter} kg of corn\n' \
    #        f'And we will receive {eggs_counter} eggs, {wool_counter} kg of wool, {milk_counter} l milk and {meat_counter} '
    #
    # @staticmethod
    # def result():
    #     """записывает в файл окончательный результат"""
    #     with open('text.txt', 'w') as f:
    #         f.write(Farm.text)
    #     print(Farm.text)

class Animals(Farm):
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
        print('Everybody sounds great') # Вот не понял я нужно ли здесь что-то печатать если
        # все равно это значение не вызывается

class Cow(Animals):
    def __init__(self, name: str, hay: int, milk: int):
        super().__init__(name, hay)
        self.milk = milk
        print(f"Here is goog cow {self.name}, \n"
              f"She eats {self.hay} of hay for a day and gives you {self.milk} l milk")

    def buy_cow(self):
        Farm.animal_counter += 1
        Farm.milk_counter += self.milk
        Farm.hay_counter += self.hay
        print(f"One more cow in a barn/ We have now {Farm.animal_counter} animals")


    def say_hello(self):
        """метод выводит на экран звук животного"""
        print('Mooooo')

class Result(Farm):
    text = f'In our barn live {Farm.animal_counter} animals\n' \
           f'In our chickencoop live {Farm.birds_counter} birds\n' \
           f'For feed them we need {Farm.hay_counter} kg of hay and {Farm.corn_counter} kg of corn\n' \
           f'And we will receive {Farm.eggs_counter} eggs, {Farm.wool_counter} kg of wool, {Farm.milk_counter} l milk and {Farm.meat_counter} '

    @staticmethod
    def result():
        """записывает в файл окончательный результат"""
        with open('text.txt', 'w') as f:
            f.write(Result.text)
        print(Result.text)


Murka = Cow('Murka', 10, 15)
Murka.buy_cow()
Murka.welcoming()
Murka.say_hello()




print(Farm.animal_counter)
print(Farm.milk_counter)
print(Farm.hay_counter)
Result.result()