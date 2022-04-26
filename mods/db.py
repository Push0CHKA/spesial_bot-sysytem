from mods import diff
import sqlite3 as sq
import os


def make_db(path, tname, fields):  # метод для создания бд
    with sq.connect(f'{path}') as database:
        database.cursor()
        database.execute(f"""CREATE TABLE IF NOT EXISTS {tname}({fields})""")
    print(f' Таблица {tname} в {path} успешно создана')


def crash_db(path):  # метод для удаления бд
    if os.path.isfile(path):
        os.remove(path)
        print(f" Файл {path} успешно удален")
    else:
        print(f" Файла {path} не существует")


def download(path, name):  # метод для скачивания данных из бд
    with sq.connect(f'{path}') as database:
        database.cursor()
        data = database.execute(f"SELECT * FROM {name}")
        inf = data.fetchall()
    return inf


def loading(data, path, tname):  # метод для загрузки данных в бд
    col_count = len(data[0])
    load = diff.for_loading_data(col_count)
    with sq.connect(f'{path}') as database:
        cur = database.cursor()
        cur.executemany(f'INSERT INTO {tname} VALUES {load}', data)


def del_duplicates(path, tname, params):  # метод для удаления дубликатов
    with sq.connect(path) as photos_data_base:
        photos_data_base.cursor()
        photos_data_base.execute(f"""DELETE FROM {tname}
                    where rowid not in
                        (
                            SELECT min(rowid)
                            FROM {tname}
                            group BY
                            {params}
                        )""")
    print(f' Дубликаты в {tname} успешно удалены')
    