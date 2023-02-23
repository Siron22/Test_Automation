from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, context):
        pass


class MobileApp(Observer):

    def update(self, context):
        print(f"IN MOBILE: Current temperature is {context}")


class WebPortal(Observer):
    def update(self, context):
        print(f"IN WEBPORTAL: Current temperature is {context}")


class AirConditioner(Observer):

    def __init__(self, min_temp, max_temp):
        self.min_temp = min_temp
        self.max_temp = max_temp

    def update(self, context):
        if context < self.min_temp:
            print("Heating...")
        elif context > self.max_temp:
            print("Cooling...")
        else:
            print("Do nothing")
