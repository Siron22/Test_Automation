#assert False
print("After assert")


def add(a, b):
    return a + b

a = 5
print("ddddddddcdc")


# assert condition, message
# if not condition:
#     raise AssertionError(message)

#print(f"In assertions {__name__}")

# 0000 0000 - 0, 255

# def add_bytes(a, b):
#     assert 0 <= a <= 127
#     assert 0 <= b <= 127
#     c = (a + b) % 256
#
#     return c
#
# print(add_bytes(255, 255))

# if __name__ == '__main__':
#
#     print(add(5, 7))
#     assert add(3, 5) == 8
#     assert add(0, 6) == 6
#     a = 1
#     assert add(a, 7) == 34, f"Something went wrong with var {a}"

print(__debug__)

if __debug__:
    print("")