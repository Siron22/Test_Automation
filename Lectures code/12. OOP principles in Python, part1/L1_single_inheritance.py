# class Human:
#
#     value = 3
#
#     @staticmethod
#     def hello():
#         print("Hello")
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def human_info(self):
#         print(f"{self.name}, {self.age}")
#
#
# class Employee(Human):
#     pass
#
# john = Human("John", 23)
# john.human_info()
# john.hello()
# print(john.value)
#
#
# andrew = Employee("Andrew", 54)
# andrew.human_info()
# andrew.hello()
# print(andrew.value)

"""
Object
^
Animal
^
Human
^
Employee
^
employee_object
"""




class Animal:

    is_alive = True



class Human(Animal):

    value = 3

    @staticmethod
    def hello():
        print("Hello")

    def __init__(this, name, age):
        this.name = name
        this.age = age

    def human_info(self):
        print(f"{self.name}, {self.age}")

    def new_method(self):
        print("New")


class Employee(Human):

    def __init__(self, name, age, salary):
        super().__init__(name, age)
        # self.name = name
        # self.age = age
        self.salary = salary

    def increase_salary(self):
        self.salary += 100


john = Human("John", 23)
john.human_info()


andrew = Employee("Andrew", 54, 3400)
andrew.human_info()
print(andrew.salary)
andrew.increase_salary()
print(andrew.salary)
andrew.new_method()

Employee.human_info(andrew)

print(andrew.is_alive)