"""
Binary operators: __add__, __radd__, __iadd__
Destructor: __del__
Bit operators: __and__, __or__
"""

class Horse:

    def __init__(self, speed, strength):
        self.speed = speed
        self.strength = strength

    def __add__(self, other):
        """Сложение."""
        return Mule(self.speed, other.strength)

    def __radd__(self, other):
        """Отражённое сложение."""
        return Mule(self.speed, other.strength)

    def __and__(self, other):
        """Двоичное И, оператор &."""
        return self.speed * other.strength

    def __iadd__(self, other):
        """Сложение с присваиванием."""
        return Mule(self.speed, other.strength)

    def __str__(self):
        """Определяет поведение функции str(), вызванной для экземпляра вашего класса."""
        return f"Horse speed: {self.speed}, strength: {self.strength}"

    def __del__(self):
        """
        __del__ это его деструктор. Он не определяет поведение для выражения del x
        (поэтому этот код не эквивалентен x.__del__()). Скорее, он определяет поведение объекта в то время,
        когда объект попадает в сборщик мусора. Это может быть довольно удобно для объектов, которые могут
        требовать дополнительных чисток во время удаления, таких как сокеты или файловыве объекты.
        __del__ всегда вызывается по завершении работы интерпретатора.
        """
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