"""
Выбрать паттерн проектирования и реализовать его на конкретном примере (паттерн из GoF, который рассматривали
или не рассматривали, но не Singleton, не Iterator, не Decorator).

Pattern "Mediator"
<<< Brain >>>
"""
from abc import ABC, abstractmethod
from enum import Enum


class Event:
    """Типы возможных событий"""
    Food = "Food"
    Danger = "Danger"


class BodyPartType(Enum):
    """Типы частей тела"""
    Hand = 0
    Leg = 1
    Eye = 2
    Ear = 3


class Nerve(ABC):
    @abstractmethod
    def notify(self, body_part, event):
        pass


class BodyPart(ABC):
    """Абстрактный класс для частей тела"""

    @staticmethod
    def food_reaction():
        pass

    @staticmethod
    def danger_reaction():
        pass

    @abstractmethod
    def type(self):
        pass


class Eye(BodyPart):

    def __init__(self, mediator):
        self.mediator = mediator

    def something_see(self,):
        event = None
        answer = input("What have you seen (Food/Danger)?: ")
        if answer == "Food":
            event = Event.Food
        elif answer == "Danger":
            event = Event.Danger
        else:
            print("Try again")
            self.something_see()
        self.mediator.notify(self, event)

    @staticmethod
    def food_reaction():
        print("I see something eatable!")

    @staticmethod
    def danger_reaction():
        print("I see danger object")

    def type(self):
        return BodyPartType.Eye


class Ear(BodyPart):

    def __init__(self, mediator):
        self.mediator = mediator

    def something_hear(self):
        event = None
        answer = input("What have you heard (Food/Danger)?: ")
        if answer == "Food":
            event = Event.Food
        elif answer == "Danger":
            event = Event.Danger
        else:
            print("Try again")
            self.something_hear()
        self.mediator.notify(self, event)

    @staticmethod
    def food_reaction():
        print("I hear tasty piggy!")

    @staticmethod
    def danger_reaction():
        print("I hear hungry lion")

    def type(self):
        return BodyPartType.Ear


class Hand(BodyPart):

    def __init__(self, mediator):
        self.mediator = mediator

    @staticmethod
    def food_reaction():
        print("I take it!")

    @staticmethod
    def danger_reaction():
        print("I hit it!")

    def type(self):
        return BodyPartType.Hand


class Leg(BodyPart):

    def __init__(self, mediator):
        self.mediator = mediator

    @staticmethod
    def food_reaction():
        print("I catch it!")

    @staticmethod
    def danger_reaction():
        print("I run away")

    def type(self):
        return BodyPartType.Leg


class Brain(Nerve):

    @staticmethod
    def reaction_food():
        Hand.food_reaction()
        Leg.food_reaction()
        Eye.food_reaction()
        Ear.food_reaction()

    @staticmethod
    def reaction_danger():
        Hand.danger_reaction()
        Leg.danger_reaction()
        Eye.danger_reaction()
        Ear.danger_reaction()

    @staticmethod
    def no_reaction():
        print("I don`t know what is it!")

    def notify(self, body_part: BodyPart, event: Event):
        if body_part.type() is BodyPartType.Ear:
            if event is Event.Danger:
                print("I heard something danger")
                Brain.reaction_danger()
            elif event is Event.Food:
                print("I heard something for eating")
                Brain.reaction_food()
            else:
                Brain.no_reaction()
        else:
            if event is Event.Danger:
                print("I saw something danger")
                Brain.reaction_danger()
            elif event is Event.Food:
                print("I saw something for eating")
                Brain.reaction_food()
            else:
                Brain.no_reaction()


mediator = Brain()

eye = Eye(mediator)
hand = Hand(mediator)
leg = Leg(mediator)
ear = Ear(mediator)

eye.something_see()
print('*'*25)
ear.something_hear()
