import sys

# a = {1, 2, 3, 2, 3, 3}
# b = [1, 2, 3, 2, 3, 3]  # 123
#
# str_val = 'Hello world'
# print(hash(a))
# a.add(str_val)
# print(a, b)

# c = frozenset({1, 2, 3, 2, 3, 3})
# a.add(c)
# print(hash(c))
# print(c)
# print(a)
# print(sys.getsizeof(a))
# print(sys.getsizeof(c))
# print(sys.getsizeof(4))
#
# for i in c:
#     print(i)
#
# d = set(c)
# d.add(6)
# print(c)
# c = frozenset(d)
# print(c)


contacts = {
    'John': '+3807777777777',
    'Petr': '+3801231231233',
    'Maria': ['+3807766554434', '+3801231244554'],
    'John #2': '+1123123123123'
}

# print(contacts['John #2'])
# print(contacts['Maria'][0], contacts['Maria'][1])
# print(contacts[(1, 2, 3)])
# print(contacts)
# print('Sasha' in contacts)
# contacts['Sasha'] = '+3809955443322'
# del contacts['Petr']
# petr = contacts.pop('Petr')
# maria = contacts.pop('Maria')
# remove_list = ('Petr', 'Maria', (1, 2, 3))
# removed_items = [contacts.pop(x) for x in remove_list]
# print(removed_items)
# print('Sasha' in contacts)

# dict_comp = {key: value for key in dict if statement}

# for key in contacts:
#     print(key, '=', contacts[key])

# for key, value in contacts.items():  # for idx, value in enumerate(list)
#     print(key, '=', value)

# for value in contacts.values():
#     print(value)

# contacts.keys() - dict_keys([key_1, key_2, ...])
# contacts.values() - dict_values([value_1, value_2, ...])
# contacts.items() - dict_items([(key_1, value_1), (key_2, value_2)])

# new_contacts = dict.fromkeys([1, 2, 3, 4], None)
# print(new_contacts)

# if 'Sasha' in contacts:
#     print(contacts['Sasha'])
# print(contacts.get('Petr', '+380999999999'))

# print(contacts)
# print(contacts.popitem())
# print(contacts)


# print(contacts)
# contacts.update({
#     'key': 'value',
#     'John #2': None
# })

# item = contacts.setdefault('John #3', '+380999999999')
# item = contacts.get('John #3', '+380999999999')
# contacts['John #3'] = item

# print(item)


# print(item, contacts)


import collections
import random


# random_items = [random.randint(1, 10) for _ in range(100)]
# counter = collections.Counter(random_items)
#
# print(random_items)
# print(counter)
# print(counter[6])

# users = collections.defaultdict(list, {
#     'John': ['+3807777777777', '+3801231231233'],
#     'Petr': ['+3807766554434'],
# })

# print(users['John'])

# for _ in range(2):
#     name = input('Enter name: ')
#     phone = input('Enter phone: ')
#     users[name].append(phone)
#
# print(users)


# f = open('data.txt', 'r')
# print(f.read())
# data = f.readline()
# while data:
#     print(data)
#     data = f.readline()
# else:
#     print('EOF')

# print(f.readlines())
# f.close()


# f = open('./project/data__3.txt', 'rb')
# f = open('../../../../../../Desktop/data__3.txt', 'rb')
# f.write('Hello world\n')

# f.writelines(['Hello world\n', 'Hello world\n', 'Hello world\n'])
# f.write(b'Hello world\n')
# print(f.read())
# f.close()

# with open('data.txt', 'w') as f:
#     f.write('Hello world\n')
#     f.write('Hello world 2\n')
#     f.write('Hello world 3\n')


# f.write('End!')
# print('Hello world')


# with open('dog.jpg', 'rb') as f:
#     print(f.read())

# import shutil
# import os
#
# os.remove('data.txt')

import pickle

# print(contacts)

# with open('contacts.txt', 'wb') as f:
    # pickle.dump(contacts, f)
    # or
    # bytes_source = pickle.dumps(contacts)
    # f.write(bytes_source)

# with open('contacts.txt', 'rb') as f:
    # from_file = pickle.loads(f.read())
    # or
    # from_file = pickle.load(f)
# print(from_file)


import json


with open('contacts.json', 'w') as f:
    json.dump(contacts, f)
    # or
    # json_str = json.dumps(contacts)
    # f.write(json_str)

with open('contacts.json', 'r') as f:
    from_file = json.loads(f.read())
    # or
    # from_file = json.load(f)
print(from_file)

