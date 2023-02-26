import sqlite3


class UsersTable:

    def __init__(self, path):
        self.connection = sqlite3.connect(path, isolation_level=None)
        self.cursor = self.connection.cursor()
        create_users_table = """
        CREATE TABLE IF NOT EXISTS Users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,
        age INTEGER, gender TEXT, nationality TEXT);
        """
        self.cursor.execute(create_users_table)
        self.connection.close()

    def add_one_user(self, name:str, age:int = None, gender:str = None, nationality:str = None):
        add_one_user = f"INSERT INTO Users (name, age, gender, nationality) VALUES ({name},{age},{gender},{nationality});"
        self.cursor.execute(add_one_user)
        self.connection.close()
        return 'One user added'

    def add_many_users(self, users_data:list):
        add_many_user = f"INSERT INTO Users (name, age, gender, nationality) VALUES ({users_data});"
        self.cursor.execute(add_many_user)
        self.connection.close()
        return 'More users added'

    def add_users_from_file(self, path):
        with open(path, 'r') as file:
            data = file.read()
        add_many_user = f"INSERT INTO Users (name, age, gender, nationality) VALUES ({data});"
        self.cursor.execute(add_many_user)
        self.connection.close()
        return 'Users from file added'

    def get_all_users(self):
        all_users = "SELECT * FROM Users;"
        self.cursor.execute(all_users)

        self.connection.close()






users_data = [('James', 25, 'male', 'USA'),
  ('Leila', 32, 'female', 'France'),
  ('Brigitte', 35, 'female', 'England'),
  ('Mike', 40, 'male', 'Denmark'),
  ('Elizabeth', 21, 'female', 'Canada')]
