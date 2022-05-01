import sqlite3 as sql
from config.db_config import users_data_db_path, users_data_db_tname, prob_db_path, prob_male_first_names_db_tname, \
    prob_female_first_names_db_tname, prob_male_last_names_db_tname, prob_female_last_names_db_tname, \
    prob_maiden_names_db_tname, prob_city_title_db_tname, prob_country_title_db_tname, prob_bdate_db_tname, \
    prob_occupation_name_db_tname, prob_occupation_type_db_tname, prob_university_name_db_tname, \
    prob_education_form_db_tname, prob_home_town_db_tname, prob_school_name_db_tname, prob_school_type_db_tname, \
    prob_school_year_graduated_db_tname, prob_personal_alcohol_db_tname, prob_personal_langs_db_tname, \
    prob_personal_life_main_db_tname, prob_personal_people_main_db_tname, prob_personal_political_db_tname, \
    prob_personal_religion_db_tname, prob_personal_smoking_db_tname, prob_is_closed_db_tname, prob_main_fields_db_tname, \
    prob_counter_albums_db_tname, prob_counter_video_db_tname, prob_counter_audios_db_tname, \
    prob_counter_photos_db_tname, prob_counter_friends_db_tname, prob_counter_groups_db_tname
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


def make_maiden_names_prob(new_user_type_name):
    """
            Метод для составления таблицы вероятности девичьих фамилий
    """
    # анализ вероятностного распределения женских имен
    with sql.connect(users_data_db_path) as data_base:
        cur = data_base.execute(f'SELECT maiden_name, count(*) FROM {users_data_db_tname} '
                                f'GROUP BY maiden_name HAVING (count(*) > {rows_cnt / 1000}) and (sex == 1)')
        data = cur.fetchall()
        cur = data_base.execute(f'SELECT * FROM {users_data_db_tname} WHERE sex == 1')
        all_data = cur.fetchall()
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
            probability.append((int(val) / len(all_data)).__round__(5))
        labels.append('не указано')
        probability.append(((len(all_data) - len(probability))/len(all_data)).__round__(5))
        _values.append('1')

    # загружаем данные в бд
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_maiden_names_db_tname} (last_name, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_city_title_prob(new_user_type_name):
    """
            Метод для составления таблицы вероятности названий городов
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT city_title, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY city_title HAVING count(*) > {rows_cnt / 500}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT city_title FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        _all = len(data1) + len(data2)
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            all_cnt += int(y)
            _values.append(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_city_title_db_tname} (city_title, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_country_title_prob(new_user_type_name):
    """
        Распределение названия стран
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT country_title, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY country_title HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT country_title FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_country_title_db_tname} (country_title, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_bdate_prob(new_user_type_name):
    """
        Распределение дат рождения
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT bdate, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY bdate HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT bdate FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_bdate_db_tname} (bdate, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_occupation_name_prob(new_user_type_name):
    """
        Распределение названий занятости
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT occupation_name, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY occupation_name HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT occupation_name FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_occupation_name_db_tname} (occupation_name, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_occupation_type_prob(new_user_type_name):
    """
        Распределение типов занятости
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT occupation_type, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY occupation_type HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT occupation_type FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_occupation_type_db_tname} (occupation_type, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_education_university_name_prob(new_user_type_name):
    """
        Распределение названий университетов
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT education_university_name, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY education_university_name HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT education_university_name FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_university_name_db_tname} (university_name, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_education_form_prob(new_user_type_name):
    """
        Распределение форм обучений
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT education_form, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY education_form HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT education_form FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_education_form_db_tname} (education_form, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_home_town_prob(new_user_type_name):
    """
        Название родного города
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT home_town, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY home_town HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT home_town FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_home_town_db_tname} (home_town, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_school_name_prob(new_user_type_name):
    """
        Название школы
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT school_name, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY school_name HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT school_name FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_school_name_db_tname} (school_name, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_school_type_prob(new_user_type_name):
    """
        Тип школы
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT school_type_str, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY school_type_str HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT school_type_str FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_school_type_db_tname} (school_type, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_school_year_graduated_prob(new_user_type_name):
    """
        Распределение по годам выпуска со школ
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT school_year_graduated, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY school_year_graduated HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT school_year_graduated FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_school_year_graduated_db_tname} '
                              f'(school_year_graduated, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_personal_alcohol_prob(new_user_type_name):
    """
         Распределение вероятностей отношения к алкоголю
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT personal_alcohol, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY personal_alcohol HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT personal_alcohol FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_personal_alcohol_db_tname} '
                              f'(personal_alcohol, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_personal_langs_prob(new_user_type_name):
    """
         Распределение вероятностей знания языков
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT personal_langs, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY personal_langs HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT personal_langs FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_personal_langs_db_tname} '
                              f'(personal_langs, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_personal_life_main_prob(new_user_type_name):
    """
         Распределение вероятностей самое важное в жизни
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT personal_life_main, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY personal_life_main HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT personal_life_main FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_personal_life_main_db_tname} '
                              f'(life_main, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_personal_people_main_prob(new_user_type_name):
    """
         Распределение вероятностей самое важное в людях
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT personal_people_main, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY personal_people_main HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT personal_people_main FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_personal_people_main_db_tname} '
                              f'(people_main, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_personal_political_prob(new_user_type_name):
    """
         Распределение вероятностей самое важное в людях
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT personal_political, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY personal_political HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT personal_political FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_personal_political_db_tname} '
                              f'(political, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_personal_religion_prob(new_user_type_name):
    """
         Распределение вероятностей религий
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT personal_religion, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY personal_religion HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT personal_religion FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_personal_religion_db_tname} '
                              f'(religion, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_personal_smoking_prob(new_user_type_name):
    """
         Распределение вероятностей религий
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT personal_smoking, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY personal_smoking HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT personal_smoking FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data1) + len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    _values.append(len(data2) - all_cnt)
    labels.append('не указано')
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_personal_smoking_db_tname} '
                              f'(smoking, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_is_closed_prob(new_user_type_name):
    """
         Распределение вероятностей закрытости страницы
    """
    with sql.connect(users_data_db_path) as data_base:
        cur1 = data_base.execute(f'SELECT is_closed, count(*) FROM {users_data_db_tname} '
                                 f'GROUP BY is_closed HAVING count(*) > {rows_cnt / 1000}')
        data1 = cur1.fetchall()
        cur2 = data_base.execute(f'SELECT is_closed FROM {users_data_db_tname}')
        data2 = cur2.fetchall()
        _all = len(data2)
        _values = []
        labels = []
        probability = []
        all_cnt = 0
        for x, y, *z in data1:
            if x is None or x == "":
                continue
            _values.append(y)
            all_cnt += int(y)
            labels.append(str(x))
    for val in _values:
        probability.append((int(val)/_all).__round__(4))
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(_values)):
            data_base.execute(f'INSERT INTO {prob_is_closed_db_tname} '
                              f'(is_closed, probability) VALUES (?, ?)',
                              (labels[i], probability[i],))


def make_main_fields(new_user_type_name):
    """
        Распределение вероятностей заполнения основной информации
    """
    stat_list = [0] * 13
    with sql.connect(users_data_db_path) as data_base:
        cur = data_base.execute(f'SELECT interests, about, books, tv, quotes, games, movies, music, activities,'
                                f'site, status, mobile_phone, home_phone FROM {users_data_db_tname}')
        data = cur.fetchall()
    for dt in data:
        if dt[0] != '':
            stat_list[0] += 1
        if dt[1] != '':
            stat_list[1] += 1
        if dt[2] != '':
            stat_list[2] += 1
        if dt[3] != '':
            stat_list[3] += 1
        if dt[4] != '':
            stat_list[4] += 1
        if dt[5] != '':
            stat_list[5] += 1
        if dt[6] != '':
            stat_list[6] += 1
        if dt[7] != '':
            stat_list[7] += 1
        if dt[8] != '':
            stat_list[8] += 1
        if dt[9] != '':
            stat_list[9] += 1
        if dt[10] != '':
            stat_list[10] += 1
        if dt[11] != '':
            stat_list[11] += 1
        if dt[12] != '':
            stat_list[12] += 1
    for i in range(len(stat_list)):
        stat_list[i] = (stat_list[i]/len(data)).__round__(4)

    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        data_base.execute(f'INSERT INTO {prob_main_fields_db_tname} '
                          f'(interests_prob, about_prob, books_prob, tv_prob, quotes_prob, games_prob, movies_prob,'
                          f' music_prob, activities_prob, site_prob, status_prob, mobile_phone_prob, home_phone_prob) '
                          f'VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)',
                          stat_list)


def make_counter_albums(new_user_type_name):
    """
        Распределение вероятностей количества альбомов
    """
    cnt_list = [0] * 5
    labels_list = ['0', '1-3', '3-7', '7-15', '>15']
    all_cnt = 0
    with sql.connect(users_data_db_path) as data_base:
        cur = data_base.execute(f'SELECT counters_albums FROM {users_data_db_tname}')
        data = cur.fetchall()

    for dt in data:
        if dt[0] != '':
            all_cnt += 1
            if int(dt[0]) == 0:
                cnt_list[0] += 1
            if (int(dt[0]) > 0) and (int(dt[0]) < 3):
                cnt_list[1] += 1
            if (int(dt[0]) > 3) and (int(dt[0]) < 7):
                cnt_list[2] += 1
            if (int(dt[0]) > 7) and (int(dt[0]) < 15):
                cnt_list[3] += 1
            if int(dt[0]) > 15:
                cnt_list[4] += 1
    for cnt in range(len(cnt_list)):
        cnt_list[cnt] = (cnt_list[cnt] / all_cnt).__round__(4)

    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(cnt_list)):
            data_base.execute(f'INSERT INTO {prob_counter_albums_db_tname} '
                              f'(counter_albums, probability) VALUES (?, ?)',
                              (labels_list[i], cnt_list[i],))


def make_counter_videos(new_user_type_name):
    """
        Распределение вероятностей количества видео
    """
    cnt_list = [0] * 7
    labels_list = ['0', '1-10', '10-25', '25-50', '50-100', '100-200', '>200']
    all_cnt = 0
    with sql.connect(users_data_db_path) as data_base:
        cur = data_base.execute(f'SELECT counters_videos FROM {users_data_db_tname}')
        data = cur.fetchall()

    for dt in data:
        if dt[0] != '':
            all_cnt += 1
            if int(dt[0]) == 0:
                cnt_list[0] += 1
            if (int(dt[0]) > 0) and (int(dt[0]) < 10):
                cnt_list[1] += 1
            if (int(dt[0]) > 10) and (int(dt[0]) < 25):
                cnt_list[2] += 1
            if (int(dt[0]) > 25) and (int(dt[0]) < 50):
                cnt_list[3] += 1
            if (int(dt[0]) > 50) and (int(dt[0]) < 100):
                cnt_list[4] += 1
            if (int(dt[0]) > 100) and (int(dt[0]) < 200):
                cnt_list[5] += 1
            if int(dt[0]) > 200:
                cnt_list[6] += 1
    for cnt in range(len(cnt_list)):
        cnt_list[cnt] = (cnt_list[cnt] / all_cnt).__round__(4)
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(cnt_list)):
            data_base.execute(f'INSERT INTO {prob_counter_video_db_tname} '
                              f'(counter_videos, probability) VALUES (?, ?)',
                              (labels_list[i], cnt_list[i],))


def make_counter_audios(new_user_type_name):
    """
        Распределение вероятностей количества аудио
    """
    cnt_list = [0] * 7
    labels_list = ['0', '1-10', '10-25', '25-50', '50-100', '100-200', '>200']
    all_cnt = 0
    with sql.connect(users_data_db_path) as data_base:
        cur = data_base.execute(f'SELECT counters_audios FROM {users_data_db_tname}')
        data = cur.fetchall()

    for dt in data:
        if dt[0] != '':
            all_cnt += 1
            if int(dt[0]) == 0:
                cnt_list[0] += 1
            if (int(dt[0]) > 0) and (int(dt[0]) < 10):
                cnt_list[1] += 1
            if (int(dt[0]) > 10) and (int(dt[0]) < 25):
                cnt_list[2] += 1
            if (int(dt[0]) > 25) and (int(dt[0]) < 50):
                cnt_list[3] += 1
            if (int(dt[0]) > 50) and (int(dt[0]) < 100):
                cnt_list[4] += 1
            if (int(dt[0]) > 100) and (int(dt[0]) < 200):
                cnt_list[5] += 1
            if int(dt[0]) > 200:
                cnt_list[6] += 1
    for cnt in range(len(cnt_list)):
        cnt_list[cnt] = (cnt_list[cnt] / all_cnt).__round__(4)
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(cnt_list)):
            data_base.execute(f'INSERT INTO {prob_counter_audios_db_tname} '
                              f'(counter_audios, probability) VALUES (?, ?)',
                              (labels_list[i], cnt_list[i],))


def make_counter_photos(new_user_type_name):
    """
        Распределение вероятностей количества аудио
    """
    cnt_list = [0] * 7
    labels_list = ['0', '1-10', '10-25', '25-50', '50-100', '100-200', '>200']
    all_cnt = 0
    with sql.connect(users_data_db_path) as data_base:
        cur = data_base.execute(f'SELECT counters_photos FROM {users_data_db_tname}')
        data = cur.fetchall()

    for dt in data:
        if dt[0] != '':
            all_cnt += 1
            if int(dt[0]) == 0:
                cnt_list[0] += 1
            if (int(dt[0]) > 0) and (int(dt[0]) < 10):
                cnt_list[1] += 1
            if (int(dt[0]) > 10) and (int(dt[0]) < 25):
                cnt_list[2] += 1
            if (int(dt[0]) > 25) and (int(dt[0]) < 50):
                cnt_list[3] += 1
            if (int(dt[0]) > 50) and (int(dt[0]) < 100):
                cnt_list[4] += 1
            if (int(dt[0]) > 100) and (int(dt[0]) < 200):
                cnt_list[5] += 1
            if int(dt[0]) > 200:
                cnt_list[6] += 1
    for cnt in range(len(cnt_list)):
        cnt_list[cnt] = (cnt_list[cnt] / all_cnt).__round__(4)
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(cnt_list)):
            data_base.execute(f'INSERT INTO {prob_counter_photos_db_tname} '
                              f'(counter_photos, probability) VALUES (?, ?)',
                              (labels_list[i], cnt_list[i],))


def make_counter_friends(new_user_type_name):
    """
        Распределение вероятностей количества друзей
    """
    cnt_list = [0] * 10
    labels_list = ['0', '1-10', '10-25', '25-50', '50-100', '100-200', '200-500', '500-1000', '1000-3000', '>3000']
    all_cnt = 0
    with sql.connect(users_data_db_path) as data_base:
        cur = data_base.execute(f'SELECT counters_friends FROM {users_data_db_tname}')
        data = cur.fetchall()

    for dt in data:
        if dt[0] != '':
            all_cnt += 1
            if int(dt[0]) == 0:
                cnt_list[0] += 1
            if (int(dt[0]) > 0) and (int(dt[0]) < 10):
                cnt_list[1] += 1
            if (int(dt[0]) > 10) and (int(dt[0]) < 25):
                cnt_list[2] += 1
            if (int(dt[0]) > 25) and (int(dt[0]) < 50):
                cnt_list[3] += 1
            if (int(dt[0]) > 50) and (int(dt[0]) < 100):
                cnt_list[4] += 1
            if (int(dt[0]) > 100) and (int(dt[0]) < 200):
                cnt_list[5] += 1
            if (int(dt[0]) > 200) and (int(dt[0]) < 500):
                cnt_list[6] += 1
            if (int(dt[0]) > 500) and (int(dt[0]) < 1000):
                cnt_list[7] += 1
            if (int(dt[0]) > 1000) and (int(dt[0]) < 3000):
                cnt_list[8] += 1
            if int(dt[0]) > 3000:
                cnt_list[9] += 1
    for cnt in range(len(cnt_list)):
        cnt_list[cnt] = (cnt_list[cnt] / all_cnt).__round__(4)
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(cnt_list)):
            data_base.execute(f'INSERT INTO {prob_counter_friends_db_tname} '
                              f'(counter_friends, probability) VALUES (?, ?)',
                              (labels_list[i], cnt_list[i],))


def make_counter_groups(new_user_type_name):
    """
        Распределение вероятностей количества друзей
    """
    cnt_list = [0] * 10
    labels_list = ['0', '1-10', '10-25', '25-50', '50-100', '100-200', '200-500', '500-1000', '1000-3000', '>3000']
    all_cnt = 0
    with sql.connect(users_data_db_path) as data_base:
        cur = data_base.execute(f'SELECT counters_groups FROM {users_data_db_tname}')
        data = cur.fetchall()

    for dt in data:
        if dt[0] != '':
            all_cnt += 1
            if int(dt[0]) == 0:
                cnt_list[0] += 1
            if (int(dt[0]) > 0) and (int(dt[0]) < 10):
                cnt_list[1] += 1
            if (int(dt[0]) > 10) and (int(dt[0]) < 25):
                cnt_list[2] += 1
            if (int(dt[0]) > 25) and (int(dt[0]) < 50):
                cnt_list[3] += 1
            if (int(dt[0]) > 50) and (int(dt[0]) < 100):
                cnt_list[4] += 1
            if (int(dt[0]) > 100) and (int(dt[0]) < 200):
                cnt_list[5] += 1
            if (int(dt[0]) > 200) and (int(dt[0]) < 500):
                cnt_list[6] += 1
            if (int(dt[0]) > 500) and (int(dt[0]) < 1000):
                cnt_list[7] += 1
            if (int(dt[0]) > 1000) and (int(dt[0]) < 3000):
                cnt_list[8] += 1
            if int(dt[0]) > 3000:
                cnt_list[9] += 1
    for cnt in range(len(cnt_list)):
        cnt_list[cnt] = (cnt_list[cnt] / all_cnt).__round__(4)
    with sql.connect(f'{prob_db_path}/{new_user_type_name}.db') as data_base:
        for i in range(len(cnt_list)):
            data_base.execute(f'INSERT INTO {prob_counter_groups_db_tname} '
                              f'(counter_groups, probability) VALUES (?, ?)',
                              (labels_list[i], cnt_list[i],))
















