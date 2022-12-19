# __getattr__, __getattribute__, __setattr__

class Data:

    def __init__(self, data):
        self.data = data
        self.secret = None


    def __getattr__(self, name):
        print("In __geattr__")
        if name == 'corrupted_data':
            return self.data + 'QQQQQQQQQ'

    def __setattr__(self, key, value):
        if key == 'secret':
            print("Secret was set")
            self.__dict__['secret'] = value
        else:
            self.__dict__[key] = value

    def __getattribute__(self, name):
        print(f"Attribute {name} is taken")
        return super().__getattribute__(name)


data = Data("sdbafgf78444")
#print(data.data)
print(data.corrupted_data)
# data.secret = "323232323"
# print(data.secret)