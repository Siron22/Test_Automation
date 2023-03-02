import sqlite3

connection = sqlite3.connect('db/orders.db', isolation_level=None)
cursor = connection.cursor()

# for row in cursor.execute('select name from Vendors;'):
#     print(row)

# cursor.execute('select * from Vendors;')
# data = cursor.fetchall()
# print(data)
# print(len(data))
# print(type(data[0][4]))

# for i in range(9):
#     row = cursor.fetchone()
#     print(row)

# for i in range(4):
#     data = cursor.fetchmany(2)
#     print((data))

# cursor.execute('select * from Vendors where price > 20 order by name desc;')
# data = cursor.fetchall()
# print(data)
# print(len(data))
# print(type(data[0][4]))

#cursor.execute("insert into Vendors(name, item, deal, price) VALUES ('Jordan II', 'DoubleCar', 13, 14.4);")
#connection.commit()
# cursor.execute("select * from Vendors;")
# data = cursor.fetchall()
# print(data)


#cursor.execute("select * from Vendors where name like 'J%' AND price > 10;")
#cursor.execute("select * from Vendors where name like (?) AND price > (?);", ('J%', 10))
#cursor.execute("select * from Vendors where price > (?);", (10,))
# cursor.execute("select * from Vendors where name like :name AND price > :price;", {'name': 'J%', 'price': 10})
# data = cursor.fetchall()
# print(data)

# cursor.executemany("insert into Vendors(name, item, deal, price) VALUES (?, ?, ?, ?);",
#                    [('Johnsy', 'DoubleCar', 13, 14.4),
#                     ('Andrew III', 'DoubleCar', 13, 14.4)])
# cursor.execute("select * from Vendors;")
# data = cursor.fetchall()
# print(data)

with open('test.sql', 'r') as f:
    cursor.executescript(f.read())

cursor.execute("select * from Data;")
data = cursor.fetchall()
print(data)


cursor.close()
connection.close()
