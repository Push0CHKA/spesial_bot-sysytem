from config.db_config import prob_first_names_db_fields, prob_female_first_names_db_tname, \
        prob_male_first_names_db_tname, prob_db_path, prob_male_last_names_db_tname, prob_female_last_names_db_tname, \
        prob_last_names_db_fields, prob_maiden_names_db_tname, prob_maiden_names_db_fields, prob_city_title_db_tname, \
        prob_city_title_db_fields, prob_country_title_db_tname, prob_country_title_db_fields, prob_bdate_db_tname, \
        prob_bdate_db_fields, prob_occupation_name_db_tname, prob_occupation_name_db_fields, \
        prob_occupation_type_db_tname, prob_occupation_type_db_fields, prob_education_form_db_tname, \
        prob_education_form_db_fields, prob_university_name_db_tname, prob_university_name_db_fields, \
        prob_home_town_db_tname, prob_home_town_db_fields, prob_school_name_db_tname, prob_school_name_db_fields, \
        prob_school_type_db_tname, prob_school_type_db_fields, prob_school_year_graduated_db_tname, \
        prob_school_year_graduated_db_fields, prob_personal_alcohol_db_tname, prob_personal_alcohol_db_fields, \
        prob_personal_langs_db_tname, prob_personal_langs_db_fields, prob_personal_life_main_db_tname, \
        prob_personal_life_main_fields, prob_personal_people_main_db_tname, prob_personal_people_main_fields, \
        prob_personal_political_db_tname, prob_personal_political_fields, prob_personal_religion_db_tname, \
        prob_personal_religion_fields, prob_personal_smoking_db_tname, prob_personal_smoking_fields, \
        prob_is_closed_db_tname, prob_is_closed_db_fields, prob_main_fields_db_tname, prob_main_fields_db_fields, \
        prob_counter_albums_db_tname, prob_counter_albums_db_fields, prob_counter_video_db_tname, \
        prob_counter_video_db_fields, prob_counter_audios_db_tname, prob_counter_audios_db_fields, \
        prob_counter_photos_db_tname, prob_counter_photos_db_fields, prob_counter_friends_db_tname, \
        prob_counter_friends_db_fields, prob_counter_groups_db_tname, prob_counter_groups_db_fields
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
    db.make_db(  # создание бд с таблицей девичьх фамилий фамилий
        prob_db_path + '/' + new_users_type + '.db',
        prob_maiden_names_db_tname,
        prob_maiden_names_db_fields
    )
    db.make_db(  # создание бд с таблицей названий городов
        prob_db_path + '/' + new_users_type + '.db',
        prob_city_title_db_tname,
        prob_city_title_db_fields
    )
    db.make_db(  # создание бд с таблицей названий стран
        prob_db_path + '/' + new_users_type + '.db',
        prob_country_title_db_tname,
        prob_country_title_db_fields
    )
    db.make_db(  # создание бд с таблицей дат рождения
        prob_db_path + '/' + new_users_type + '.db',
        prob_bdate_db_tname,
        prob_bdate_db_fields
    )
    db.make_db(  # создание бд с таблицей названий родов деятельности
        prob_db_path + '/' + new_users_type + '.db',
        prob_occupation_name_db_tname,
        prob_occupation_name_db_fields
    )
    db.make_db(  # создание бд с таблицей типов родов деятельности
        prob_db_path + '/' + new_users_type + '.db',
        prob_occupation_type_db_tname,
        prob_occupation_type_db_fields
    )
    db.make_db(  # создание бд с таблицей форм образовательных учреждений
        prob_db_path + '/' + new_users_type + '.db',
        prob_education_form_db_tname,
        prob_education_form_db_fields
    )
    db.make_db(  # создание бд с таблицей названий образовательных учреждений
        prob_db_path + '/' + new_users_type + '.db',
        prob_university_name_db_tname,
        prob_university_name_db_fields
    )
    db.make_db(  # создание бд с таблицей названий родных городов
        prob_db_path + '/' + new_users_type + '.db',
        prob_home_town_db_tname,
        prob_home_town_db_fields
    )
    db.make_db(  # создание бд с таблицей названий школ
        prob_db_path + '/' + new_users_type + '.db',
        prob_school_name_db_tname,
        prob_school_name_db_fields
    )
    db.make_db(  # создание бд с таблицей типов школ
        prob_db_path + '/' + new_users_type + '.db',
        prob_school_type_db_tname,
        prob_school_type_db_fields
    )
    db.make_db(  # создание бд с таблицей времени выпуска со школ
        prob_db_path + '/' + new_users_type + '.db',
        prob_school_year_graduated_db_tname,
        prob_school_year_graduated_db_fields
    )
    db.make_db(  # создание бд с отношением к алкоголю
        prob_db_path + '/' + new_users_type + '.db',
        prob_personal_alcohol_db_tname,
        prob_personal_alcohol_db_fields
    )
    db.make_db(  # создание бд с языками
        prob_db_path + '/' + new_users_type + '.db',
        prob_personal_langs_db_tname,
        prob_personal_langs_db_fields
    )
    db.make_db(  # создание бд с главное в жизни
        prob_db_path + '/' + new_users_type + '.db',
        prob_personal_life_main_db_tname,
        prob_personal_life_main_fields
    )
    db.make_db(  # создание бд с главное в людях
        prob_db_path + '/' + new_users_type + '.db',
        prob_personal_people_main_db_tname,
        prob_personal_people_main_fields
    )
    db.make_db(  # создание бд с политический взгляд
        prob_db_path + '/' + new_users_type + '.db',
        prob_personal_political_db_tname,
        prob_personal_political_fields
    )
    db.make_db(  # создание бд с религия
        prob_db_path + '/' + new_users_type + '.db',
        prob_personal_religion_db_tname,
        prob_personal_religion_fields
    )
    db.make_db(  # создание бд с отношение к курению
        prob_db_path + '/' + new_users_type + '.db',
        prob_personal_smoking_db_tname,
        prob_personal_smoking_fields
    )
    db.make_db(  # создание бд с закрытость
        prob_db_path + '/' + new_users_type + '.db',
        prob_is_closed_db_tname,
        prob_is_closed_db_fields
    )
    db.make_db(  # создание бд с основные поля (обо мне, любимая музыка, игры и тд)
        prob_db_path + '/' + new_users_type + '.db',
        prob_main_fields_db_tname,
        prob_main_fields_db_fields
    )
    db.make_db(  # создание бд с счетчиками альбомов
        prob_db_path + '/' + new_users_type + '.db',
        prob_counter_albums_db_tname,
        prob_counter_albums_db_fields
    )
    db.make_db(  # создание бд с счетчиками видео
        prob_db_path + '/' + new_users_type + '.db',
        prob_counter_video_db_tname,
        prob_counter_video_db_fields
    )
    db.make_db(  # создание бд с счетчиками музыки
        prob_db_path + '/' + new_users_type + '.db',
        prob_counter_audios_db_tname,
        prob_counter_audios_db_fields
    )
    db.make_db(  # создание бд с счетчиками фото
        prob_db_path + '/' + new_users_type + '.db',
        prob_counter_photos_db_tname,
        prob_counter_photos_db_fields
    )
    db.make_db(  # создание бд с счетчиками друзей
        prob_db_path + '/' + new_users_type + '.db',
        prob_counter_friends_db_tname,
        prob_counter_friends_db_fields
    )
    db.make_db(  # создание бд с счетчиками групп
        prob_db_path + '/' + new_users_type + '.db',
        prob_counter_groups_db_tname,
        prob_counter_groups_db_fields
    )
