"""
Создать классы Employee (сотрудник) и Company (компания).
Классы должны содержать:
    минимум два поля экземпляров и одно поле класса
    минимум два метода экземпляра
    минимум один метод класса
    минимум один статический метод
К методам добавить строки документации.
Методы должные быть НЕ get/set поле, а что-то оригинальнее:) (но если надо их, тоже можно добавить)
Написать код который создает несколько экземпляров и взаимодействует с объектами
Задание в том числе и на фантазию
"""
from typing import Literal
POSITIONS = Literal['Worker', 'Teamlead']

class Employee:
    employees = {}
    w_reserve = {}
    t_reserve = {}
    workers_counter = 0
    teamlead_counter = 0
    max_workers = 4
    min_age = 18
    max_age = 65

    def __init__(self, name: str, age: int, position: POSITIONS = 'Worker'):
        """конструктор принимает имя, возраст (от 18 до 65) и желаемую должность сотрудника,
        далее происходит проверка на соответствие возрасту, правильности должности
        и наличию вакансий. 
        При соответствии всех параметорв работника включают в штат - employees"""
        self.name = name
        self.age = age
        self.position = position

        if Employee.max_age > age >= Employee.min_age:
            if position == 'Worker':
                if Employee.workers_counter < Employee.max_workers:
                    Employee.workers_counter += 1
                    Employee.employees[name] = position
                    print(f'New employer {name} is ready to work as a {position}!\n'
                          f'We need more {Employee.max_workers - Employee.workers_counter} workers')
                else:
                    print(f'Sorry {self.name}, we have no vacancy! You are appended to HR reserve.')
                    Employee.w_reserve[name] = position
            elif position == 'Teamlead':
                if Employee.teamlead_counter < 1:
                    Employee.teamlead_counter += 1
                    Employee.employees[name] = position
                    print(f'We have new Teamlead: {self.name}!')
                else:
                    print(f'Sorry {self.name}, Teamlead position is busy. You are appended to HR reserve.')
                    Employee.t_reserve[name] = position
            else:
                print(f'Sorry {self.name}, we have no any position like {self.position}')
        elif Employee.max_age <= self.age:
            print(f'Sorry {self.name}, you are too old')
        else:
            print(f'Sorry {self.name}, you are too young')

    def im_ready(self):
        """Сотрудник выражает готовность приёма на работу и сообщает сколько ему осталось до пенсии"""
        print(f'Hello, my name is {self.name} and I have  to work {Employee.max_age - self.age} years\n'
              f'before retirement as a {self.position}')

    def dismissal(self):
        """Увольнение сотрудника и удаление из штата. Проверяет чтобы сотрудник находился в штате"""
        if self.name in Employee.employees:
            if self.position == 'Worker':
                Employee.employees.pop(self.name, None)
                Employee.workers_counter -= 1
                print(f'Worker {self.name} is dismissed!\n'
                      f'We need more {Employee.max_workers - Employee.workers_counter} workers')
                if Employee.w_reserve:
                    res = list(Employee.w_reserve.keys())
                    new_worker = res[0]
                    print(f'We can recruit {new_worker} to work')
                    Employee.w_reserve.pop(new_worker)
                    Employee.employees[new_worker] = self.position
                    print(f'Hello, my name is {new_worker} and I`m ready to be a new Worker')
                else:
                    print('We have no anybody in reserve!')
            elif self.position == 'Teamlead':
                Employee.teamlead_counter -= 1
                Employee.employees.pop(self.name, None)
                print(f'Teamlead {self.name} is dismissed!\nWe have no Teamlead for our team!')
                if Employee.t_reserve:
                    res = list(Employee.t_reserve.keys())
                    new_lead = res[0]
                    Employee.workers_counter += 1
                    print(f'We can recruit {new_lead} to work')
                    Employee.t_reserve.pop(new_lead, None)
                    Employee.employees[new_lead] = self.position
                    Employee.teamlead_counter += 1
                    print(f'Hello, my name is {new_lead} and I`m ready to be a new Teamlead')
                else:
                    print('We have no anybody in reserve!')
            else:
                pass

    @staticmethod
    def who_work():
        """Статический метод, показывает поименный список действующих сотрудников"""
        print(f'{Employee.employees}')

    @staticmethod
    def vacancies():
        """Статический метод, показывает актуальное количество работников и вакансий поименный список"""
        print(f'We have {Employee.workers_counter} workers and we need '
              f'{Employee.max_workers - Employee.workers_counter}')
        if Employee.teamlead_counter == 1:
            print(f'We have a Teamlead!')
        else:
            print('We have no Teamlead')




# Posistive tests
Ivan = Employee('Ivan', 35, 'Worker')
Ivan.im_ready()
Mikhail = Employee('Mikhail', 30, 'Worker')
Sasha = Employee('Sasha', 56, 'Worker')
Petya = Employee('Petya', 21, 'Worker')
Eduard = Employee('Eduard', 57, 'Teamlead')
Employee.who_work()

# Negative tests
Kolya = Employee('Kolya', 42, 'Worker')
Grisha = Employee('Grisha', 65, 'Worker')
Kostya = Employee('Kostya', 17, 'Worker')
Serhii = Employee('Serhii', 43, 'Teamlead')
Employee.who_work()


# Dismiss tests
Sasha.dismissal()
Employee.who_work()
Kostya.dismissal()
Eduard.dismissal()
Employee.who_work()
Employee.vacancies()

