# __getattr__, __getattribute__, __setattr__

class Data:

    def __init__(self, data):
        self.data = data
        self.secret = None


    def __getattr__(self, name):
        """Вы можете определить поведение для случая, когда пользователь пытается обратиться к атрибуту, который
        не существует (совсем или пока ещё). Это может быть полезным для перехвата и перенаправления частых опечаток,
        предупреждения об использовании устаревших атрибутов (вы можете всё-равно вычислить и вернуть этот атрибут,
        если хотите), или хитро возвращать AttributeError, когда это вам нужно. """
        print("In __geattr__")
        if name == 'corrupted_data':
            return self.data + 'QQQQQQQQQ'

    def __setattr__(self, key, value):
        """В отличии от __getattr__, __setattr__ решение для инкапсуляции. Этот метод позволяет вам определить
        поведение для присвоения значения атрибуту, независимо от того существует атрибут или нет. То есть,
        вы можете определить любые правила для любых изменений значения атрибутов. """
        if key == 'secret':
            print("Secret was set")
            self.__dict__['secret'] = value
        else:
            self.__dict__[key] = value

    def __getattribute__(self, name):
        """Этот метод позволяет вам определить поведение для каждого случая доступа к атрибутам (а не только к
        несуществующим, как __getattr__(self, name)). Он страдает от таких же проблем с бесконечной рекурсией,
        как и его коллеги (на этот раз вы можете вызывать __getattribute__ у базового класса, чтобы их предотвратить).
        Он, так же, главным образом устраняет необходимость в __getattr__, который в случае реализации __getattribute__
        может быть вызван только явным образом или в случае генерации исключения AttributeError"""
        print(f"Attribute {name} is taken")
        return super().__getattribute__(name)


data = Data("sdbafgf78444")
#print(data.data)
print(data.corrupted_data)
# data.secret = "323232323"
# print(data.secret)