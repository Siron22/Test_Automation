def function(data):
    if isinstance(data, str):
        print(data)
    elif isinstance(data, int):
        print(data + 100)


class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print("Tyap-lyap and to production")

    def increase_salary_annually(self, increase_param):
        self.salary += self.salary * (1 + increase_param)


class Manager(Employee):

    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def work(self):
        print("Everybody work hard!!!")
        super().work()

    def increase_salary_annually(self, increase_param):
        super().increase_salary_annually(increase_param)
        self.salary += self.bonus
        #self.salary += self.salary * increase_param + bonus



employee = Employee("John", 2300)
employee.work()
print(employee.salary)
employee.increase_salary_annually(0.1)
print(employee.salary)

manager = Manager("Michael", 5400, 2000)
manager.work()
print(manager.salary)
manager.increase_salary_annually(0.1)
print(manager.salary)