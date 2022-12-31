"""
def decorator:
pass
@decorator
class A:
pass
A = decorator(A)
"""

# def add_class_attribute(cls):
#     cls.new_attribute = "DEFAULT"
#     return cls
#
# @add_class_attribute
# class A:
#     def __init__(self):
#         self.inner = 3
#
# a = A()
# print(a.__dict__)
# print(a.new_attribute)


def decorator(cls):

    class Wrapper:
        def __init__(self, *args, **kwargs):
            self.wrapped = cls(*args, **kwargs)

        def __getattr__(self, name):
            return getattr(self.wrapped, name)

        def print_dict(self):
            print(self.wrapped.__dict__)
    return Wrapper


@decorator
class A:
    def __init__(self):
        self.inner = 3

a = A()
a.print_dict()

class Wrapper:
    def __init__(self, wrapped):
        self.wrapped = wrapped

b = Wrapper(a)
print(b.wrapped is a)