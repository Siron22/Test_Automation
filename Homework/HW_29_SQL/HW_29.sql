1. Установить SQLite
2. Создать таблицу Persons(name: string, favorite_color: string, profit: float)
3. Создать таблицу Cars(model: string, color: string, price: float)
4. Заполнить таблицы данными
5. Вывести для каждого человека, который может купить автомобиль,
самый дешевый автомобиль его любимого цвета, который он может себе позволить (цена автомобиля должна быть меньше или равна дохода человека).
Отсортировать по имени чeловека в алфавитном порядке.

6*. Вывести для каждого человека самый дешевый автомобиль его любимого цвета, который он может себе позволить (цена
автомобиля должна быть меньше или равна дохода человека).
Отсортировать по имени чeловека в алфавитном порядке.
Решением должен быть файл с расширением .sql и всеми запросами

sqlite3 homework.db
CREATE TABLE Persons(name TEXT, favorite_color TEXT, profit FLOAT);
CREATE TABLE Cars(model TEXT, color TEXT, price FLOAT);
.headers ON
.mode column
INSERT INTO Persons(name, favorite_color, profit) VALUES ('Alex', 'Red', 100), ('John', 'Red', 300), ('Mike', 'Black', 100),
('Olaf', 'Green', 100), ('Kristof', 'Green', 500), ('Marta', 'Black', 456), ('Nikky', 'Yellow', 356), ('Susy', 'Yellow', 102);
INSERT INTO Cars(model, color, price) VALUES ('BMW M3', 'Red', 109), ('BMW M5', 'Red', 199), ('BMW M7', 'Red', 299),
('Panamera', 'Green', 140), ('Boxter', 'Green', 199), ('911', 'Green', 299), ('Mondeo', 'Black', 109), ('Escape', 'Black', 199),
('Fiesta', 'Black', 299), ('Uno', 'Yellow', 199), ('Punto', 'Yellow', 299), ('Julletta', 'Yellow', 109);

5.
select name, model, color, price, profit from persons inner join cars on favorite_color=color and price<profit
group by name having min(price) order by name ASC;



