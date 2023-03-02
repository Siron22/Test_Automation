class Employee:

    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self._salary = salary
        self.__heartbeat = 90
        #print(f"heartbeat = {self.__heartbeat}")

    def _randomly_increase_salary(self):
        self._salary += 100

    def set_ny_bonus(self):
        self._randomly_increase_salary()

    def get_heartbeat(self):
        return self.__heartbeat

    def set_heartbeat(self, new_value):
        self.__heartbeat = new_value

class Tester(Employee):

    def strange_method(self):
        print(f"self._salary = {self._salary}")

    def method2(self):
        print(f"heartbeat = {self._Employee__heartbeat}")



employee = Employee("Olga", 54, 3400)
print(employee.get_heartbeat())
employee.set_heartbeat(120)
print(employee.get_heartbeat())
# print(employee.name)
# print(employee.age)
# employee.age = 34
# print(employee.age)
# print(employee._salary)
# employee._salary = 5600
# print(employee._salary)
# employee._randomly_increase_salary()
# print(employee._salary)
#print(employee.__heartbeat)
print(employee._Employee__heartbeat)
#employee._Employee__heartbeat = 120
#employee.__heartbeat = 120
print(employee._Employee__heartbeat)

tester = Tester("Oksana", 34, 2300)
print(tester._salary)
tester.strange_method()
tester.method2()