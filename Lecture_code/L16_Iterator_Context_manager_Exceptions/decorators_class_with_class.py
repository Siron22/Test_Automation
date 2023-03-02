# DON'T DO THIS

class Tracer:

    def __init__(self, aClass):
        self.aClass = aClass

    def __call__(self, *args, **kwargs):
        self.wrapped = self.aClass(*args, **kwargs)
        return self

    def __getattr__(self, item):
        print(f"Trace: {item}")
        return getattr(self.wrapped, item)


@Tracer
class Person:
    def __init__(self, name):
        self.name = name

    def print_name(self):
        print(self.name)


john = Person("John")
john.print_name()

print()

anna = Person("Anna")
anna.print_name()
print()

john.print_name()
