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


class Company:
    """класс предназначен для создания компаний и их регистрации"""
    companies_list = {}

    def __init__(self, name: str, city: str, activity: str):
        """Коструктор ринимает имя, город в котором расположена компания и сферу деятельности
        Вносит данные в справочник компаний (dict) -  companies_list"""
        self.name = name
        self.city = city
        self.activity = activity
        Company.companies_list[name] = {"name": name, "city": city, "activity": activity}
        print(f'New company {name} is registered')

    def personal(self, pers: int):
        """метод добавляет данные про численность штата компании
        и относит их к категориям: большая средняя или маленькая"""
        if 1 < pers < 50:
            size = "small"
        elif 50 <= pers < 500:
            size = "middle"
        else:
            size = "big"
        Company.companies_list[self.name]["size"] = size
        Company.companies_list[self.name]["pers"] = pers
        print(f"===> Information about about size of company {self.name} updated ")

    @staticmethod
    def golden_pages():
        """Статический метод, выводит справочник компаний. Проверяет наличие в словаре ключей
        "HR" и "Size" и в случае их остутствия добавляе в словарь"""
        print()
        print("***** Golden pages begin *****")
        for company in Company.companies_list:
            if 'pers' not in Company.companies_list[company]:
                Company.companies_list[company]["pers"] = "Unknown"
                Company.companies_list[company]["size"] = "Unknown"
            print(f'Company page <<{company}>>\nName: {Company.companies_list[company]["name"]}\n'
                  f'Location: {Company.companies_list[company]["city"]}\n'                  
                  f'Activity: {Company.companies_list[company]["activity"]}\n'
                  f'HR: {Company.companies_list[company]["pers"]}\n'
                  f'Size: {Company.companies_list[company]["size"]}\n'
                  f'--------------------------')
        print("***** Golden pages end *****")
        print()


IBM = Company("IBM", "New York", "IT")
Apfel = Company("Apfel", "Berlin", "Industry")
Sharashka = Company("Sharashka", "Mumbasa", "Lottery")

Company.golden_pages()

IBM.personal(49)
Apfel.personal(499)
Sharashka.personal(501)

Company.golden_pages()
