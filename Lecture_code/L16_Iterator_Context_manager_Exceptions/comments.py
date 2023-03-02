# Decorators class with class


# Problem with class fields calculation
class A:

    var1 = "var1"
    var2 = f"var2 referencing var1: {var1}"


a = A()
print(a.var1)  # var1
print(a.var2)  # var2 referencing var1: var1
A.var1 = "qqqq"
print(a.var1)  # qqqq
print(a.var2)  # var2 referencing var1: var1

a2 = A()
print(a2.var2)  # var2 referencing var1: var1

# Use classes more
# Bad
def print_user_data_to_file(name, age):
    pass
# Good
def print_user_data_to_file(user):
    pass

# Relations: Inheritance, association, aggregation (composition), delegation

# Clients code!!!

# Var with name id
id_ = 3
print(id_)

a = "q\nq"
print(a)
