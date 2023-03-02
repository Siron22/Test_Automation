# a = 21
# print(a)

# print(a := 21)
# a += 2
# print(a)

# text = input("Enter")
# while text != 'Q':
#     text = input('Enter text')
#     print(len(text))

# while (text := input('Enter text')) != 'Q':
#     text = input('Enter text')
#     print(len(text))

# sqr = lambda x: x * x
# lst = [sqr(i) for i in range(10) if sqr(i) > 9]
# print(lst)
#
# lst = [temp for i in range(10) if (temp := sqr(i)) > 9]
# print(lst)


# a = True
# if a and (b := 4):
#     print("In IF")
#     print(b)
# print(b)

a = False
if a or (b := 4):
    print("In IF")
    print(b)
print(b)