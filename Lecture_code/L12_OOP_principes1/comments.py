# file creation
# issue from HW
# OOP fields/methods, unbound methods

# import os
# print(os.getcwd())
#
# with open("test.txt", 'w') as f:
#     f.write("QQQQ")

# #def get_all_user_list(simple_user=[]):
# def get_all_user_list(simple_user=None):
#     if not simple_user:
#         users = []
#     users.append("Admin")
#     return users
#     # simple_user.append("Admin")
#     # return simple_user
#
#
# users = get_all_user_list()
# print(users)
# users = get_all_user_list()
# print(users)


# def get_all_user_list(simple_users):
#     users = simple_users.copy()
#     users.append("Admin")
#     return users
#
# users = ["Andrew"]
#
# all_users = get_all_user_list(users)
# print(all_users)
# print(users)

lst1 = [1, 2, [3, 4, [4, 5]]]
import copy
lst2 = copy.deepcopy(lst1)


print(lst1)
print(lst2)

lst1[2].append("QQQQ")
lst1[2][2].append("PPPP")
print(lst1)
print(lst2)


class A:

    def add(a, b):
        return a+b

print(A.add(3,5))