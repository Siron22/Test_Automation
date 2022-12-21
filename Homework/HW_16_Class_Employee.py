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

class Employee:
    employees_list = {}
    workers_counter = 0
    Teamlead_counter = 0

    def __init__(self, name: str, age: int, position='Worker' or 'Teamlead'):
        """конструктор принимает имя, возраст (от 18 до 65) и желаемую должность сотрудника,
        далее происходит проверка на соответствие возрасту, правильности должности
        и наличию вакансий. 
        При соответствии всех параметорв работника включают в штат - employees_list"""
        self.name = name
        self.age = age
        self.position = position
        if 65 > self.age >= 18:
            if position == 'Worker':
                if Employee.workers_counter < 4:
                    Employee.workers_counter += 1
                    Employee.employees_list[name] = position
                    print(f'New employer {name} is ready to work as a {position}!\n'
                          f'We need more {4 - Employee.workers_counter} workers')
                else:
                    print(f'Sorry {self.name}, we have no vacancy!')
            elif position == 'Teamlead':
                if Employee.Teamlead_counter < 1:
                    Employee.Teamlead_counter += 1
                    Employee.employees_list[name] = position
                    print(f'We have new Teamlead: {self.name}!')
                else:
                    print(f'Sorry {self.name}, Teamlead position is busy')
            else:
                print(f'Sorry {self.name}, we have no any position like {self.position}')
        elif 65 <= self.age:
            print(f'Sorry {self.name}, you are too old')
        else:
            print(f'Sorry {self.name}, you are too young')

    def im_ready(self):
        """Сотрудник выражает готовность приёма на работу и сообщает сколько ему осталось до пенсии"""
        print(f'Hello, my name is {self.name} and I have  to work {65 - self.age} years\n'
              f'before retirement as a {self.position}')

    def dismissal(self):
        """Увольнение сотрудника и удаление из штата. Проверяет чтобы сотрудник находился в штате"""
        if self.name in Employee.employees_list:
            if self.position == 'Worker':
                Employee.employees_list.pop(self.name, None)
                Employee.workers_counter -= 1
                print(f'Worker {self.name} is dismissed!\n'
                      f'We need more {4 - Employee.workers_counter} workers')
            elif self.position == 'Teamlead':
                Employee.Teamlead_counter -= 1
                Employee.employees_list.pop(self.name, None)
                print(f'We have no Teamlead for our team!')
            else:
                pass

    @staticmethod
    def who_work():
        """Статический метод, показывает поименный список действующих сотрудников"""
        print(f'{Employee.employees_list}')

    @staticmethod
    def vacancies():
        """Статический метод, показывает актуальное количество работников и вакансий поименный список"""
        print(f'We have {Employee.workers_counter} workers and we need {4 - Employee.workers_counter}')
        if Employee.Teamlead_counter == 1:
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
Employee.who_work()
Employee.vacancies()

