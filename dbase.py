# модуль методов для работы с базой данных
import sqlite3
#from config import db_name

# для разработки, после закоментить
db_name = "dbase.db"


class Database_engine():

    def __init__(self, filename_db):

        self.connect = sqlite3.connect(filename_db)
        print("Database connection OK!")
        self.cursor = self.connect.cursor()

    def __del__(self):
        self.connect.close()

    def create_tables(self, str_script):
        self.cursor.executescript(str_script)

    # вернуть список с именами всех групп
    def get_names_all_groups(self):
        self.cursor.executescript("SELECT name FROM groups;")
        return self.cursor.fetchall()

    # Интерфейс для прямого обращения к базе
    def script_get(self, data):
        if  isinstance(data, list):
            data = "".join(data)
            self.cursor.executemany(data)
            return self.cursor.fetchall()
        else:
            self.cursor.execute(str(data))
            return self.cursor.fetchall()

    # интерфей прямой записи в бд
    def _insert_to_db_script(self, data):
        if  isinstance(data, list):
            print(f"добавление в бд {len(data)} записей")
            data = "".join(data)
            self.cursor.executemany(data)
            self.connect.commit()
            return True
        else:
            print("добавление в бд записи")
            self.cursor.execute(data)
            self.connect.commit()
            return True

data_object = Database_engine(db_name)

