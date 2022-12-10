# ######################################################################################################################
# Reduce accepts only functions with two parameters

# ######################################################################################################################
# Don't use range(len(args)). Use iteration by elements or enumerate()

def sum(*args):
    result = 0
    for i in args:
        result += i
    return result

#print(sum(1, 3, 7))


# ######################################################################################################################
# Don't use magic numbers

# import random
# def get_random_cat(animals):
#     start_cat_index = 2
#     end_cat_index = 6
#     return random.choice(animals[start_cat_index:end_cat_index])
#
# animals = ['Gayavata', 'Ponchik', 'Murzik', 'Barsik', 'Anfisa', 'Rockie', 'Bim', 'Bom', 'Alfa']
# print(get_random_cat(animals))

# ######################################################################################################################


m = map(int, ['1', '2', '3'], ['1'])
print(m)
print(list(m))  # Error is produced only when list is called