class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, other):
        """Определяет поведение оператора меньше, < """
        return self.age < other.age

    def __gt__(self, other):
        """Определяет поведение оператора больше, > """
        return self.age > other.age

    def __le__(self, other):
        """Определяет поведение оператора меньше или равно, <= """
        return self.age <= other.age

    def __ge__(self, other):
        """Определяет поведение оператора больше или равно, >= """
        return self.age >= other.age

    def lt(self, other):
        return self.age < other.age

    def __qqq__(self):
        print("sdsdsdsd")

    def __eq__(self, other):
        """Определяет поведение оператора равенства, ==."""
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        """Определяет поведение функции hash(), вызыванной для экземпляра вашего класса. Метод должен возвращать
        целочисленное значение, которое будет использоваться для быстрого сравнения ключей в словарях. Заметьте,
        что в таком случае обычно нужно определять и __eq__ тоже. Руководствуйтесь следующим правилом: a == b
        подразумевает hash(a) == hash(b)."""
        return hash(self.name)


john = Human("John", 56)
anna = Human("Anna", 33)
#print(john < anna)
print(john.lt(anna))

john.__qqq__()
print(hash(john))

d = {
    john: 2300
}

print(d)

s = set()
s.add(john)
print(john in s)
john.name = "Anna"
print(john in s)
print(s)