import time
import requests
from config.db_config import users_id_db_path, users_id_db_tname, users_id_db_fields, users_data_db_path, \
    users_data_db_tname, main_db_fields
from config.pars_config import version, offset
from mods import db
from mods.pars import parser


def download_users_ids(token, group_ids):
    """
            Метод для получения списка id подписчиков групп
        """
    db.crash_db(users_id_db_path)  # удаляем старую бд
    db.make_db(  # создаем новую бд для id подписчиков групп
        users_id_db_path,
        users_id_db_tname,
        users_id_db_fields
    )
    for group_id in group_ids:
        data = requests.get(  # получаем данные от апи вк
            'https://api.vk.com/method/groups.getMembers',
            params={
                'access_token': token,
                'group_id': group_id,
                'offset': offset,
                'v': version
            })
        run_flag = False
        print(data.json())
        try:
            sub_count = int(data.json()['response']['count'])
            run_flag = True
        except:
            print(' Downloads users: проблема с токеном')
        offset_ = offset
        if run_flag:  # если данные получены
            while offset_ < sub_count:
                parser.users_parser(token, group_id, offset_)
                offset_ += 1000
                time.sleep(1)


def download_users_data(token):
    """
            Метод для получения полных данных о подписчиков групп
        """
    db.crash_db(users_data_db_path)  # удаление старой бд
    db.make_db(  # создание новой бд
        users_data_db_path,
        users_data_db_tname,
        main_db_fields
    )
    users_list = db.download(  # получаем список id пользователей для парсинга
        users_id_db_path,
        users_id_db_tname
    )
    cnt = 0
    for ids in users_list:
        cnt += 1
        if cnt % 100 == 0:
            print(f' Users count: {cnt}')
        parser.users_inf_parser(token, ids[1])  # парсим данные
