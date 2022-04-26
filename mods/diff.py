from config.db_config import prob_first_names_db_fields, prob_female_first_names_db_tname, \
        prob_male_first_names_db_tname, prob_db_path, prob_male_last_names_db_tname, prob_female_last_names_db_tname, \
        prob_last_names_db_fields
from mods import db


def for_loading_data(col_count):
    load = '('
    for i in range(col_count - 1):
        load += '?,'
    load += '?)'
    return load


def make_prob_db(new_users_type):
    """
        Метод для создания б с вероятностными распределениями
    """
    db.make_db(  # создание бд с таблицей мужских имен
        prob_db_path + '/' + new_users_type + '.db',
        prob_female_first_names_db_tname,
        prob_first_names_db_fields
    )
    db.make_db(  # создание бд с таблицей женских имен
        prob_db_path + '/' + new_users_type + '.db',
        prob_male_first_names_db_tname,
        prob_first_names_db_fields
    )
    db.make_db(  # создание бд с таблицей мужских фамилий
        prob_db_path + '/' + new_users_type + '.db',
        prob_male_last_names_db_tname,
        prob_last_names_db_fields
    )
    db.make_db(  # создание бд с таблицей женских фамилий
        prob_db_path + '/' + new_users_type + '.db',
        prob_female_last_names_db_tname,
        prob_last_names_db_fields
    )

