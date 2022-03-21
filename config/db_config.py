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
                 'personal_people_main TEXT, personal_political TEXT, personal_religion TEXT, personal_smoking TEXT, ' \
                 'relatives_id TEXT, relatives_type TEXT, has_photo TEXT, deactivated TEXT, is_closed TEXT'
# бд с основными данными о друзьях пользователя
friends_db_path = 'db/detect/friends_data/friends_data.db'
friends_db_tname = 'friends_data'
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
