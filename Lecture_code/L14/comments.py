"""
Equality: __eq__ and __ne__
String representation: __str__ and __repr__
Access control to attributes: __getattr__, __getattribute__, __setattr__
Private attrs, delegation, page
Sequences: __setitem__, __getitem__, __len__, __bool__
Binary operators: __add__, __radd__, __iadd__
Destructor: __del__
Bit operators: __and__, __or__
Comparison operators: __lt__, __gt__, __ge__, __le__, __cmp__
Hash value: __hash__
"""

print(__name__)


class A:
    pass


class B(A):
    def __init__(self):
        self.attr = 4

b = B()
print(b.__dict__)
print(b.__class__)
print(b.__class__.__name__)
#print(b.__base__)
print(B.__mro__)




# i = 2
# if i % 2 == 0:
#     pass
# elif i % 2 != 0:
#     pass
# # #######################
# if i % 2 == 0:
#     pass
# else:
#     pass
#
#
# a = [1, 2, 3]
# len_a = len(a)
# for i in range(10):
#     print(len_a)
