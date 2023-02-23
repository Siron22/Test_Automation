import yaml

# print(yaml.dump(['saasasas', 'errfffdfasf', 'dfgaddfdf']))
#
# print(yaml.dump({'name': 'Anna', 'age':74}))
#
#
# data = [
#     {
#         'name': 'John',
#         'age': 34
#     },
#     {
#         'name': 'Oksana',
#         'age': 36
#     }
# ]
# print(yaml.dump(data))

with open('example.yaml', 'r') as f:
    data = yaml.safe_load(f)
