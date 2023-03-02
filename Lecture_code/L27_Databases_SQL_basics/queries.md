CREATE TABLE Data(data_id INTEGER PRIMARY KEY, name TEXT, data INTEGER CHECK(data<10));
INSERT INTO Data(name, data) VALUES ('Hello', 3);


CREATE TABLE Vendors(vendor_id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE, item TEXT, deal INTEGER, price REAL);


CREATE TABLE Customers(customer_id INTEGER PRIMARY KEY, name TEXT NOT NULL, vendor_name TEXT, deal INTEGER, money REAL);

INSERT INTO Customers(name, vendor_name, deal, money) VALUES ('Johnny', 'Johny', 3, 324234.4);
INSERT INTO Customers(name, vendor_name, deal, money) VALUES ('Anna', 'Johny', 5, 324234.4);
INSERT INTO Customers(name, money) VALUES ('Andrew', 324234.4);

INSERT INTO Vendors(name, item, deal, price) VALUES ('Olaf', 'Car', 3, 14.4);



INSERT INTO Vendors(name, item, deal, price) VALUES ('John', 'Train', 3, 14.4),
('Jerom', 'Tram', 1, 2.4),
('Anna', 'Plane', 7, 100),
('Igor', 'Helicopter', 11, 1200);


--
/* */

INSERT INTO Vendors(name, deal, price) VALUES ('Joseph', 7, 14.4), ('Albert', 111, 0);





id  name     item   deal  price
--  -------  -----  ----  -----------
5   Julius
6   Julius2  Car    3     3.56
7   Jimbo    Car2   3     1.56
8   Anna     Tram   1     100.222
9   Andrew   Train  10    1000000.222

