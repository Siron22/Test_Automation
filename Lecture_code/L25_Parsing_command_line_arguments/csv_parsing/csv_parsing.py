import csv

data = [['test_id', 'param1', 'param2', 'expected'],
        ['ID1', '111', 'eee', '4edd'],
        ['ID2', '343434', '34334', '4434']]

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerows(data)


with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    # print(next(reader))
    # print(next(reader))
    # print(next(reader))


    # data = []
    # for line in reader:
    #     #print(line)
    #     data.append(line)

# print(header)
# print(data)

