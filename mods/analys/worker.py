from mods.pars import worker
from mods.analys import users_analys
from mods import diff
from config.pars_config import token
from mods import db
from config.db_config import users_data_db_path, users_data_db_tname


def make_new_user_type(groups_ids, new_tipash):
    worker.download_users_ids(token, groups_ids)
    worker.download_users_data(token)
    diff.make_prob_db(new_tipash)
    usrdata = db.download(users_data_db_path, users_data_db_tname)
    rows_cnt = len(usrdata)
    users_analys.make_first_names_prob(new_tipash, rows_cnt)
    users_analys.make_last_names_prob(new_tipash, rows_cnt)
    users_analys.make_maiden_names_prob(new_tipash, rows_cnt)
    users_analys.make_city_title_prob(new_tipash, rows_cnt)
    users_analys.make_country_title_prob(new_tipash, rows_cnt)
    users_analys.make_bdate_prob(new_tipash, rows_cnt)
    users_analys.make_occupation_name_prob(new_tipash, rows_cnt)
    users_analys.make_occupation_type_prob(new_tipash, rows_cnt)
    users_analys.make_education_university_name_prob(new_tipash, rows_cnt)
    users_analys.make_education_form_prob(new_tipash, rows_cnt)
    users_analys.make_home_town_prob(new_tipash, rows_cnt)
    users_analys.make_school_name_prob(new_tipash, rows_cnt)
    users_analys.make_school_type_prob(new_tipash, rows_cnt)
    users_analys.make_school_year_graduated_prob(new_tipash, rows_cnt)
    users_analys.make_personal_langs_prob(new_tipash, rows_cnt)
    users_analys.make_personal_life_main_prob(new_tipash, rows_cnt)
    users_analys.make_personal_people_main_prob(new_tipash, rows_cnt)
    users_analys.make_personal_alcohol_prob(new_tipash, rows_cnt)
    users_analys.make_personal_smoking_prob(new_tipash, rows_cnt)
    users_analys.make_personal_political_prob(new_tipash, rows_cnt)
    users_analys.make_personal_religion_prob(new_tipash, rows_cnt)
    users_analys.make_is_closed_prob(new_tipash, rows_cnt)
    users_analys.make_main_fields(new_tipash)
    users_analys.make_counter_albums(new_tipash)
    users_analys.make_counter_videos(new_tipash)
    users_analys.make_counter_audios(new_tipash)
    users_analys.make_counter_photos(new_tipash)
    users_analys.make_counter_friends(new_tipash)
    users_analys.make_counter_groups(new_tipash)
