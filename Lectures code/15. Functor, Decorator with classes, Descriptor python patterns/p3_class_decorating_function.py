class Tracer:

    def __init__(self, func):
        self.func = func
        self.counter = 0

    def __call__(self, *args, **kwargs):
        self.counter += 1
        print(f"Function '{self.func.__name__}' is called {self.counter} times")
        return self.func(*args, **kwargs)



# @Tracer
# def hello():
#     print("HELLO!!!")
#
# hello()
# hello()

# class Person:
#
#     def __init__(self, name):
#         self.name = name
#
#     @Tracer # Don't decorate instance methods by classes
#     def hello(self):
#         print(f"Hello, {self.name}")
#
# john = Person("John")
# john.hello()