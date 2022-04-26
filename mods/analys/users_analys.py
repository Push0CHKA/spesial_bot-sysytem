import sqlite3 as sql
from config.db_config import users_data_db_path, users_data_db_tname, prob_db_path, prob_male_first_names_db_tname, \
    prob_female_first_names_db_tname, prob_male_last_names_db_tname, prob_female_last_names_db_tname
from mods import db


usrdata = db.download(users_data_db_path, users_data_db_tname)
rows_cnt = len(usrdata)


def make_first_names_prob(new_user_type_name):
    """
        Метод для составления таблицы вероятности имен
    """
    # анализ мужских имен
    with sql.connect(users_data_db_path) as database:
        cur = database.execute(f'SELECT first_name, count(*) FROM {users_data_db_tname} '
                               f'GROUP BY first_name HAVING (count(*) > {rows_cnt/500}) and (sex == 2)')
        data = cur.fetchall()
        print(data)
        _values = []
        labels = []
        probability = []
        _all = 0
        for x, y, *z in data:
            if x is None or x == "":
                continue
            _values.append(y)
            _all += int(y)
            labels.append(str(x))
        for val in _values:
            probability.append((int(val)/_all).__round__(4))
    # загружаем данные в бд
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_male_first_names_db_tname} (first_name, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))
    # анализ женских имен
    with sql.connect(users_data_db_path) as data_base:
        cur = data_base.execute(f'SELECT first_name, count(*) FROM {users_data_db_tname} '
                                f'GROUP BY first_name HAVING (count(*) > {rows_cnt/500}) and (sex == 1)')
        data = cur.fetchall()
        print(data)
        _values = []
        labels = []
        probability = []
        _all = 0
        for x, y, *z in data:
            if x is None or x == "":
                continue
            _values.append(y)
            _all += int(y)
            labels.append(str(x))
        for val in _values:
            probability.append((int(val)/_all).__round__(4))
    # загружаем данные в бд
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_female_first_names_db_tname} (first_name, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_last_names_prob(new_user_type_name):
    """
            Метод для составления таблицы вероятности фамилий
    """
    # анализ мужских фамилий
    with sql.connect(users_data_db_path) as data_base:
        cur = data_base.execute(f'SELECT last_name, count(*) FROM {users_data_db_tname} '
                                f'GROUP BY last_name HAVING (count(*) > {rows_cnt/500}) and (sex == 2)')
        data = cur.fetchall()
        _values = []
        labels = []
        probability = []
        _all = 0
        for x, y, *z in data:
            if x is None or x == "":
                continue
            _values.append(y)
            _all += int(y)
            labels.append(str(x))
        for val in _values:
            probability.append((int(val)/_all).__round__(4))
    # загружаем данные в бд
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_male_last_names_db_tname} (last_name, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))
    # анализ вероятностного распределения женских имен
    with sql.connect(users_data_db_path) as data_base:
        cur = data_base.execute(f'SELECT last_name, count(*) FROM {users_data_db_tname} '
                                f'GROUP BY last_name HAVING (count(*) > {rows_cnt/500}) and (sex == 1)')
        data = cur.fetchall()
        _values = []
        labels = []
        probability = []
        _all = 0
        for x, y, *z in data:
            if x is None or x == "":
                continue
            _values.append(y)
            _all += int(y)
            labels.append(str(x))
        for val in _values:
            probability.append((int(val)/_all).__round__(4))
    # загружаем данные в бд
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_female_last_names_db_tname} (last_name, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))