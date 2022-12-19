class PrivacyMixin:
    def __setattr__(self, key, value):
        if key in self.private_fields:
            raise Exception(f"Attempt to set {key} private field")
        else:
            self.__dict__[key] = value


class Employee(PrivacyMixin):
    private_fields = ["salary"]

    def __init__(self, name):
        self.name = name
        #self.salary = 30
        self.set_salary(30)

    def set_salary(self, value):
        self.__dict__['salary'] = value


e1 = Employee("John")
print(e1)
#e1.salary = 30  # error
e1.set_salary(3000)
print(e1.salary)