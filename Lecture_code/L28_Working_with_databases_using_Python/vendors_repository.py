import sqlite3

#vendor_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, item TEXT, deal INTEGER, price REAL
class Vendor:

    def __init__(self, name, item, deal, price):
        self.name = name
        self.item = item
        self.deal = deal
        self.price = price

    def __repr__(self):
        return f"Vendor(name={self.name}, item={self.item}, deal={self.deal}, price={self.price})"


class BaseRepository:

    def __init__(self, db_path):
        self._connection = sqlite3.connect(db_path, isolation_level=None)
        self._cursor = self._connection.cursor()


class VendorsRepository(BaseRepository):

    def __init__(self, db_path):
        super().__init__(db_path)
        self._cursor.execute('CREATE TABLE IF NOT EXISTS Vendors(vendor_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, item TEXT, deal INTEGER, price REAL);')

    def get_all(self):
        pass

    def get_all_vendors(self):
        self._cursor.execute('select * from Vendors;')
        rows = self._cursor.fetchall()
        return [self.row2object(row) for row in rows]

    def get_all_vendors_generator(self):
        for row in self._cursor.execute('select * from Vendors;'):
            yield self.row2object(row)

    def add_vendor(self, vendor: Vendor):
        self._cursor.execute("insert into Vendors(name, item, deal, price) VALUES (?, ?, ?, ?);", (vendor.name, vendor.item, vendor.deal, vendor.price))

    def get_all_vendors_names(self):
        self._cursor.execute('select name from Vendors;')
        return [row[0] for row in self._cursor.fetchall()]

    def get_vendors_with_price_higher_than(self, price):
        self._cursor.execute('select * from Vendors where price > (?);', (price,))
        rows = self._cursor.fetchall()
        return [self.row2object(row) for row in rows]


    def row2object(self, row):
        return Vendor(row[1], row[2], row[3], row[4])


vendors_repository = VendorsRepository('db/orders.db')
print(vendors_repository.get_all_vendors())
vendor1 = Vendor('Bill 2', 'Jet', 23, 55665.33)
vendors_repository.add_vendor(vendor1)
print(vendors_repository.get_all_vendors())

print(vendors_repository.get_all_vendors_names())

print(vendors_repository.get_vendors_with_price_higher_than(15))
