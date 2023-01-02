# Decorators class with class


# Problem with class fields calculation
class A:

    var1 = "var1"
    var2 = f"var2 referencing var1: {var1}"

    """
    Если одна переменная класса ссылается на другую, то её значение определяется при создании 
    ОБЪЕКТА КЛАССА и потом не может быть изменено при создании экземпляров (статическая переменная)
    *** Для динамического изменения переменных их нужно выносить в отдельные методы
    Класс становится объектом в момент его объявления (до создания экземляра)
    """

a = A()
print(a.var1)  # var1
print(a.var2)  # var2 referencing var1: var1
A.var1 = "qqqq"
print(a.var1)  # qqqq
print(a.var2)  # var2 referencing var1: var1

a2 = A()
print(a2.var2)  # var2 referencing var1: var1

# Use classes more
# Bad
"""
Если код предусматривает передачу в функцию большого количества параметров, касающихся одной структуры, лучше создать 
класс этой структуры и передавать его в функцию
"""

def print_user_data_to_file(name, age):
    pass
# Good
def print_user_data_to_file(user):
    pass

# Relations: Inheritance, association, aggregation (composition), delegation
"""Не забывать про различные связи между классами"""

# Clients code!!!
"""После написания кода оставлять примеры его использования"""

# Var with name id
"""Если пользовательская переменная совпадает по имени со встроенной переменной принято после имени ставить _"""

id_ = 3
print(id_)

a = r"q\nq" # печатает содержимое строки как есть (не нужно экранировать спецсимволы. Удобно для регулярок)
print(a)

