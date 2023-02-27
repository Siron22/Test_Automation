import sqlite3


class UsersTable:
    CONNECTION = None

    def __init__(self, path:str):
        self.connection = sqlite3.connect(path, isolation_level=None)
        UsersTable.CONNECTION = self.connection
        self.cursor = self.connection.cursor()
        create_users_table = """
        CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
        age INTEGER, gender TEXT, nationality TEXT);
        """
        self.cursor.execute(create_users_table)
        print('New table created successful')
        self.connection.close()

    @staticmethod
    def _open_close_connection(method):
        def inner(*args, **kwargs):
            UsersTable.CONNECTION()
            UsersTable.CONNECTION.cursor()
            method(*args, **kwargs)
            UsersTable.CONNECTION.close()
        return inner

    @_open_close_connection
    def add_one_user(self, name:str, age:int = None, gender:str = None, nationality:str = None):
        add_one_user = "INSERT INTO Users (name, age, gender, nationality) VALUES (?, ?, ?, ?);"
        self.cursor.execute(add_one_user, (name,age,gender,nationality))
        print('One user added')

    def add_many_users(self, users_data:list):
        add_many_user = "INSERT INTO Users(name, age, gender, nationality) VALUES (?, ?, ?, ?);"
        self.cursor.executemany(add_many_user, users_data)
        print('More users added')

    def get_all_users(self):
        all_users = "SELECT * FROM Users;"
        self.cursor.execute(all_users)
        result = self.cursor.fetchall()
        print(result)
        return result

    def get_user_by_gender(self, gender:str):
        by_gender = f"SELECT * FROM Users WHERE gender=(?);"
        self.cursor.execute(by_gender, (gender,))
        result = self.cursor.fetchall()
        print(result)
        return result

    def new_name_for_men(self, new_name:str):
        update = f"UPDATE Users SET name=(?) where gender='male';"
        self.cursor.execute(update, (new_name, ))
        self.connection.commit()
        print('All names updated')

    def delete_all_olds(self, age:int):
        delete = f"DELETE FROM users WHERE age>(?);"
        self.cursor.execute(delete, (age, ))
        self.connection.commit()
        print('All olds deleted')


#=======>>>> TESTS <<<<=======

users_data = [('James', 25, 'male', 'USA'),('Leila', 32, 'female', 'France'),('Brigitte', 35, 'female', 'England'),
              ('Mike', 40, 'male', 'Denmark'),('Elizabeth', 21, 'female', 'Canada')]



users = UsersTable('Test_DB.db')
users.add_one_user('Rikky', age=60, gender='male', nationality='Uruguay')
# users.get_all_users()
# print('*' * 40)
# users.add_many_users(users_data)
# users.get_all_users()
# print('*' * 40)
# users.get_user_by_gender("female")
# print('*' * 40)
# users.delete_all_olds(50)
# users.get_all_users()
# print('*' * 40)
# users.new_name_for_men("Benya")
# users.get_all_users()
# users.connection.close()

