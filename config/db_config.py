# бд с данными для авторизации
auth_tname = 'auth'
auth_path = 'db/imit/auth/auth.db'
auth_fields = 'id TEXT, number TEXT, password TEXT, activate TEXT, ban TEXT'


# бд с характеристиками ботов
bot_char_tname = 'bot_char'
bot_char_path = 'db/imit/bot_char/bot_char.db'
bot_char_fields = 'id TEXT, dur_speed_from TEXT, dur_speed_to TEXT, typing_speed_from TEXT, typing_speed_to TEXT'


# бд с данными ботов
bot_data_tname = 'bot_data'
bot_data_path = 'db/imit/bot_data/bot_data.db'
bot_data_fields = 'id TEXT, screen_name TEXT, maiden_name TEXT, city_title TEXT, country_title TEXT, ' \
                  'skype TEXT, instagram TEXT, bdate TEXT, interests TEXT, about TEXT, books TEXT, tv TEXT, ' \
                  'quotes TEXT, games TEXT, movies TEXT, music TEXT, activities TEXT, site TEXT, status TEXT, ' \
                  'photo_link TEXT, mobile_phone TEXT, home_phone TEXT, career_city_name TEXT,' \
                  'career_from TEXT, career_until TEXT, career_position TEXT, career_company TEXT, ' \
                  'education_university_name TEXT, education_faculty TEXT,education_graduation TEXT,' \
                  'education_form TEXT, home_town TEXT, military_country_id TEXT, military_unit TEXT,' \
                  'military_unit_id TEXT, military_from TEXT, military_until TEXT, school_city TEXT, ' \
                  'school_class TEXT, school_country TEXT, school_name TEXT, school_type TEXT, ' \
                  'school_year_from TEXT, school_year_graduated TEXT, school_speciality TEXT, ' \
                  'personal_alcohol TEXT, personal_inspired_by TEXT, personal_langs TEXT, personal_life_main TEXT, ' \
                  'personal_people_main TEXT, personal_political TEXT, personal_religion TEXT, personal_smoking TEXT'


# бд с основными данными о пользователе
main_db_path = 'db/detect/main_data/main_data.db'
main_db_tname = 'main_data'
main_db_fields = 'user_id TEXT, first_name TEXT, last_name TEXT, sex TEXT, screen_name TEXT, nickname TEXT, ' \
                 'domain TEXT, maiden_name TEXT, city_id TEXT, city_title TEXT, country_id TEXT, ' \
                 'country_title TEXT, has_mobile TEXT, skype TEXT, bdate TEXT, interests TEXT, ' \
                 'about TEXT, books TEXT, tv TEXT, quotes TEXT,  games TEXT, movies TEXT, music TEXT, ' \
                 'activities TEXT, site TEXT, status TEXT, photo_link TEXT, followers_count text, mobile_phone TEXT, ' \
                 'home_phone TEXT,' \
                 'connections TEXT, last_seen_platform TEXT, last_seen_time TEXT, occupation_id TEXT,' \
                 'occupation_name TEXT, occupation_type TEXT, career_city_id TEXT, career_city_name TEXT,' \
                 'career_from TEXT, career_until TEXT, career_position TEXT, career_country_id TEXT,' \
                 'career_group_id TEXT, career_company TEXT, counters_albums TEXT, counters_videos TEXT,' \
                 'counters_audios TEXT, counters_photos TEXT, counters_notes TEXT, counters_friends TEXT,' \
                 'counters_groups TEXT, counters_online_friends TEXT, counters_user_videos TEXT,' \
                 'counters_followers TEXT, counters_pages TEXT, education_university TEXT,' \
                 'education_university_name TEXT, education_faculty TEXT,education_graduation TEXT,' \
                 'education_form TEXT, home_town TEXT, military_country_id TEXT, military_unit TEXT,' \
                 'military_unit_id TEXT, military_from TEXT, military_until TEXT, exports TEXT, school_city TEXT, ' \
                 'school_class TEXT, school_id TEXT, school_country TEXT, school_name TEXT, school_type TEXT, ' \
                 'school_type_str TEXT, school_year_from TEXT, school_year_graduated TEXT, school_speciality TEXT, ' \
                 'personal_alcohol TEXT, personal_inspired_by TEXT, personal_langs TEXT, personal_life_main TEXT, ' \
                 'personal_people_main TEXT, personal_political TEXT, personal_religion TEXT, personal_smoking TEXT, ' \
                 'relatives_id TEXT, relatives_type TEXT, has_photo TEXT, deactivated TEXT, is_closed TEXT'


"""
    Параметры для бд с основными данными о друзьях пользователя
"""
friends_db_path = 'db/detect/friends_data/friends_data.db'  # путь до бд с друзьями пользователя
friends_db_tname = 'friends_data'                           # название таблицы с друзьями пользователя
# название полей таблицы с друзьями пользователя
friends_db_fields = ' friend_id TEXT, user_id TEXT, first_name TEXT, last_name TEXT, sex TEXT, screen_name TEXT, ' \
                    'nickname TEXT, domain TEXT, maiden_name TEXT, city_id TEXT, city_title TEXT, country_id TEXT, ' \
                    'country_title TEXT, has_mobile TEXT, skype TEXT, instagram TEXT, bdate TEXT, interests TEXT, ' \
                    'about TEXT, books TEXT, tv TEXT, quotes TEXT,  games TEXT, movies TEXT, music TEXT, ' \
                    'activities TEXT, site TEXT, status TEXT, photo_link TEXT, mobile_phone TEXT, home_phone TEXT,' \
                    'connections TEXT, last_seen_platform TEXT, last_seen_time TEXT, occupation_id TEXT,' \
                    'occupation_name TEXT, occupation_type TEXT, career_city_id TEXT, career_city_name TEXT,' \
                    'career_from TEXT, career_until TEXT, career_position TEXT, career_country_id TEXT,' \
                    'career_group_id TEXT, career_company TEXT, counters_albums TEXT, counters_videos TEXT,' \
                    'counters_audios TEXT, counters_photos TEXT, counters_notes TEXT, counters_friends TEXT,' \
                    'counters_groups TEXT, counters_online_friends TEXT, counters_user_videos TEXT,' \
                    'counters_followers TEXT, counters_pages TEXT, education_university TEXT,' \
                    'education_university_name TEXT, education_faculty TEXT,education_graduation TEXT,' \
                    'education_form TEXT, home_town TEXT, military_country_id TEXT, military_unit TEXT,' \
                    'military_unit_id TEXT, military_from TEXT, military_until TEXT, exports TEXT, school_city TEXT, ' \
                    'school_class TEXT, school_id TEXT, school_country TEXT, school_name TEXT, school_type TEXT, ' \
                    'school_type_str TEXT, school_year_from TEXT, school_year_graduated TEXT, school_speciality TEXT, ' \
                    'personal_alcohol TEXT, personal_inspired_by TEXT, personal_langs TEXT, personal_life_main TEXT, ' \
                    'personal_people_main TEXT, personal_political TEXT, personal_religion TEXT,personal_smoking TEXT,' \
                    'relatives_id TEXT, relatives_type TEXT, has_photo TEXT, deactivated TEXT, is_closed TEXT'


# бд с данными о постах пользователя
wall_db_path = 'db/detect/wall_data/wall_data.db'
wall_db_tname = 'wall_data'
wall_db_fields = 'user_id TEXT, post_id TEXT, from_id TEXT, owner_id TEXT, post_type TEXT, private_text TEXT, ' \
                 'photo_link TEXT, repost_id TEXT, repost_owner_id TEXT, repost_from_id TEXT, repost_post_type TEXT, ' \
                 'repost_text TEXT, repost_photo_link TEXT'


"""
    Параметры для бд с основными полями о пользователе (для имитации) для заполнения
"""
users_main_data_path = 'db/imit/bot_data/users_data.db'  # путь до бд с основными полями для заполнения
users_main_data_tname = 'users_data'                     # название таблицы
# поля таблицы
users_main_data_fields = 'id TEXT, activity TEXT, interests TEXT, music TEXT, movies TEXT, tv TEXT, books TEXT, ' \
                         'games TEXT, quotes TEXT, about_me TEXT'


"""
    Параметры для бд с данными о новых пользователях (для сосотавления нового типа личности)
"""
users_id_db_path   = 'db/pars/users.db'             # путь к бд с id пользователей
users_id_db_tname  = 'users'                        # название таблицы с id пользователей
users_id_db_fields = 'group_id TEXT, user_id TEXT'  # поля для бд группа-пользователь


"""
    Параметры для бд с данными о пользователях для формирования нового типажа  
"""
users_data_db_path  = 'db/pars/users_data.db'  # путь до бд с данными о пользователях для формирования нового типажа
users_data_db_tname = 'users_data'             # название табллицы с данными о пользователях для формирования нового типажа


"""
    Параметры для бд с вероятностями (для имитации жизнедеятельности)
"""
prob_db_path                     = 'db/prob'             # папка с бд для вероятностей

# имена
prob_male_first_names_db_tname   = 'male_first_names'    # таблица с распределением вероятностей мужских имен
prob_female_first_names_db_tname = 'female_first_names'  # таблица с распределением вероятностей женских имен
# поля для бд с вероятностным распределением имен пользователей
prob_first_names_db_fields       = 'id INTEGER PRIMARY KEY, first_name TEXT, probability TEXT'

# фамилии
prob_male_last_names_db_tname   = 'male_last_names'    # таблица с распределением вероятностей мужских фамилий
prob_female_last_names_db_tname = 'female_last_names'  # таблица с распределением вероятностей женских фамилий
# поля для бд с вероятностным распределением фамилий пользователей
prob_last_names_db_fields       = 'id INTEGER PRIMARY KEY, last_name TEXT, probability TEXT'

# девичьи фамилии
prob_maiden_names_db_tname  = 'maiden_names'    # таблица с распределением вероятностей девичьих фамилий фамилий
# поля для бд с вероятностным девичьих
prob_maiden_names_db_fields = 'id INTEGER PRIMARY KEY, last_name TEXT, probability TEXT'

# города
prob_city_title_db_tname  = 'city_titles'    # таблица с распределением вероятностей городов
# поля для бд с вероятностным названий городов пользователей
prob_city_title_db_fields = 'id INTEGER PRIMARY KEY, city_title TEXT, probability TEXT'

# страны
prob_country_title_db_tname  = 'country_titles'    # таблица с распределением вероятностей стран
# поля для бд с вероятностным названий стран пользователей
prob_country_title_db_fields = 'id INTEGER PRIMARY KEY, country_title TEXT, probability TEXT'

# даты рождения
prob_bdate_db_tname  = 'bdates'    # таблица с распределением вероятностей дат рождения
# поля для бд с вероятностным дат рождения
prob_bdate_db_fields = 'id INTEGER PRIMARY KEY, bdate TEXT, probability TEXT'

# названия рода деятельности
prob_occupation_name_db_tname  = 'occupation_names'  # таблица с распределением вероятностей названий рода деятельности
# поля для бд с вероятностями названий рода деятельности
prob_occupation_name_db_fields = 'id INTEGER PRIMARY KEY, occupation_name TEXT, probability TEXT'

# название типов рода деятельности
prob_occupation_type_db_tname  = 'occupation_types'  # таблица с распределением вероятностей типов рода деятельности
# поля для бд с вероятностями рода деятельности
prob_occupation_type_db_fields = 'id INTEGER PRIMARY KEY, occupation_type TEXT, probability TEXT'

# название форм обучения
prob_education_form_db_tname  = 'education_forms'  # таблица с распределением вероятностей форм обучения
# поля для бд с вероятностями форм обучения
prob_education_form_db_fields = 'id INTEGER PRIMARY KEY, education_form TEXT, probability TEXT'

# названия университетов
prob_university_name_db_tname  = 'university_names'  # таблица с распределением вероятностей университетов
# поля для бд с вероятностями университетов
prob_university_name_db_fields = 'id INTEGER PRIMARY KEY, university_name TEXT, probability TEXT'

# названия родных городов
prob_home_town_db_tname  = 'home_towns'  # таблица с распределением родных городов
# поля для бд с вероятностями родных городов
prob_home_town_db_fields = 'id INTEGER PRIMARY KEY, home_town TEXT, probability TEXT'

# названия школ
prob_school_name_db_tname  = 'school_names'  # таблица с распределением вероятностей названий школ
# поля для бд с вероятностями названий школ
prob_school_name_db_fields = 'id INTEGER PRIMARY KEY, school_name TEXT, probability TEXT'

# название типов школ
prob_school_type_db_tname  = 'school_types'  # таблица с распределением вероятностей типов школ
# поля для бд с вероятностями типов школ
prob_school_type_db_fields = 'id INTEGER PRIMARY KEY, school_type TEXT, probability TEXT'

# год выпуска со школы
prob_school_year_graduated_db_tname  = 'school_years_graduated'  # таблица с распределением вероятностей выпуска со школы
# поля для бд с вероятностями год выпуска со школы
prob_school_year_graduated_db_fields = 'id INTEGER PRIMARY KEY, school_year_graduated TEXT, probability TEXT'

# отношение к алкоголю
prob_personal_alcohol_db_tname  = 'personal_alcohol'  # таблица с распределением вероятностей отношение к алкоголю
# поля для бд с вероятностями отношение к алкоголю
prob_personal_alcohol_db_fields = 'id INTEGER PRIMARY KEY, personal_alcohol TEXT, probability TEXT'

# языки
prob_personal_langs_db_tname  = 'personal_langs'  # таблица с распределением вероятностей языков
# поля для бд с вероятностями языков
prob_personal_langs_db_fields = 'id INTEGER PRIMARY KEY, personal_langs TEXT, probability TEXT'

# главное в жизни
prob_personal_life_main_db_tname  = 'life_main'
prob_personal_life_main_fields = 'id INTEGER PRIMARY KEY, life_main TEXT, probability TEXT'

# главное в людях
prob_personal_people_main_db_tname  = 'people_main'
prob_personal_people_main_fields = 'id INTEGER PRIMARY KEY, people_main TEXT, probability TEXT'

# политический взгляд
prob_personal_political_db_tname  = 'political'
prob_personal_political_fields = 'id INTEGER PRIMARY KEY, political TEXT, probability TEXT'

# религия
prob_personal_religion_db_tname  = 'religion'
prob_personal_religion_fields = 'id INTEGER PRIMARY KEY, religion TEXT, probability TEXT'

# отношение к курению
prob_personal_smoking_db_tname  = 'smoking'
prob_personal_smoking_fields = 'id INTEGER PRIMARY KEY, smoking TEXT, probability TEXT'


# закрытость
prob_is_closed_db_tname  = 'is_closed'
prob_is_closed_db_fields = 'id INTEGER PRIMARY KEY, is_closed TEXT, probability TEXT'

# основные поля (обо мне, любимая музыка, игры и тд)
prob_main_fields_db_tname = 'main_fields'
prob_main_fields_db_fields = 'interests_prob TEXT, about_prob TEXT, books_prob TEXT, tv_prob TEXT, quotes_prob TEXT,' \
                             'games_prob TEXT, movies_prob TEXT, music_prob TEXT, activities_prob TEXT, site_prob TEXT,' \
                             'status_prob TEXT, mobile_phone_prob TEXT, home_phone_prob TEXT'

# количество альбомов
prob_counter_albums_db_tname  = 'counter_albums'
prob_counter_albums_db_fields = 'id INTEGER PRIMARY KEY, counter_albums TEXT, probability TEXT'

# количество видео
prob_counter_video_db_tname  = 'counter_videos'
prob_counter_video_db_fields = 'id INTEGER PRIMARY KEY, counter_videos TEXT, probability TEXT'

# количество музыка
prob_counter_audios_db_tname  = 'counter_audios'
prob_counter_audios_db_fields = 'id INTEGER PRIMARY KEY, counter_audios TEXT, probability TEXT'

# количество музыка
prob_counter_photos_db_tname  = 'counter_photos'
prob_counter_photos_db_fields = 'id INTEGER PRIMARY KEY, counter_photos TEXT, probability TEXT'

# количество друзей
prob_counter_friends_db_tname  = 'counter_friends'
prob_counter_friends_db_fields = 'id INTEGER PRIMARY KEY, counter_friends TEXT, probability TEXT'

# количество групп
prob_counter_groups_db_tname  = 'counter_groups'
prob_counter_groups_db_fields = 'id INTEGER PRIMARY KEY, counter_groups TEXT, probability TEXT'





