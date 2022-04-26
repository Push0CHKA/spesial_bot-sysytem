import requests
from mods import db
from config.pars_config import version, user_fields
from config.db_config import users_id_db_path, users_id_db_tname, users_data_db_path, users_data_db_tname


def users_parser(token, group_id, offset):
    """
        Метод для париснга id пользователей групп
    """
    sub_list = requests.get('https://api.vk.com/method/groups.getMembers',
                            params={
                                'access_token': token,
                                'group_id': group_id,
                                'offset': offset,
                                'v': version
                            })
    run_flag = False
    sub_list_data = []
    try:
        sub_list_data = sub_list.json()['response']['items']
        run_flag = True
    except:
        print(' Users parser: проблема с токеном')
    sub_data = []
    if run_flag:
        for sub in sub_list_data:
            sub_data.append([group_id, sub])
        db.loading(
            sub_data,
            users_id_db_path,
            users_id_db_tname
        )


def users_inf_parser(token, user_ids):
    """
        Метод для парсинга данных о пользователях
    """
    # получаем данные с сервера
    main_inf = requests.get('https://api.vk.com/method/users.get',
                            params={
                                'access_token': token,
                                'v': version,
                                'user_ids': user_ids,
                                'fields': user_fields
                            })
    run_flag = False
    # json
    try:
        main_inf = main_inf.json()['response']
        run_flag = True
    except:
        print(' Users inf parser: проблемы с токеном')
    all_data = []
    if run_flag:
        for data in main_inf:
            li = [data['id']]
            if data.get('first_name') is not None:
                li.append(str(data['first_name']))
            else:
                li.append('')
            if data.get('last_name') is not None:
                li.append(str(data['last_name']))
            else:
                li.append('')
            if data.get('sex') is not None:
                li.append(str(data['sex']))
            else:
                li.append('')
            if data.get('screen_name') is not None:
                li.append(str(data['screen_name']))
            else:
                li.append('')
            if data.get('nickname') is not None:
                li.append(str(data['nickname']))
            else:
                li.append('')
            if data.get('domain') is not None:
                li.append(str(data['domain']))
            else:
                li.append('')
            try:
                li.append(str(data['maiden_name']))
            except:
                li.append('')
            try:
                li.append(str(data['city']['id']))
            except:
                li.append('')
            try:
                li.append(str(data['city']['title']))
            except:
                li.append('')
            try:
                li.append(str(data['country']['id']))
            except:
                li.append('')
            try:
                li.append(str(data['country']['title']))
            except:
                li.append('')
            if data.get('has_mobile') is not None:
                li.append(str(data['has_mobile']))
            else:
                li.append('')
            if data.get('skype') is not None:
                li.append(str(data['skype']))
            else:
                li.append('')
            if data.get('bdate') is not None:
                li.append(str(data['bdate']))
            else:
                li.append('')
            if data.get('interests') is not None:
                li.append(str(data['interests']))
            else:
                li.append('')
            if data.get('about') is not None:
                li.append(str(data['about']))
            else:
                li.append('')
            if data.get('books') is not None:
                li.append(str(data['books']))
            else:
                li.append('')
            if data.get('tv') is not None:
                li.append(str(data['tv']))
            else:
                li.append('')
            if data.get('quotes') is not None:
                li.append(str(data['quotes']))
            else:
                li.append('')
            if data.get('games') is not None:
                li.append(str(data['games']))
            else:
                li.append('')
            if data.get('movies') is not None:
                li.append(str(data['movies']))
            else:
                li.append('')
            if data.get('music') is not None:
                li.append(str(data['music']))
            else:
                li.append('')
            if data.get('activities') is not None:
                li.append(str(data['activities']))
            else:
                li.append('')
            if data.get('site') is not None:
                li.append(str(data['site']))
            else:
                li.append('')
            if data.get('status') is not None:
                li.append(str(data['status']))
            else:
                li.append('')
            if data.get('photo_max_orig') is not None:
                li.append(str(data['photo_max_orig']))
            else:
                li.append('')
            if data.get('followers_count') is not None:
                li.append(str(data['followers_count']))
            else:
                li.append('')
            if data.get('mobile_phone') is not None:
                li.append(str(data['mobile_phone']))
            else:
                li.append('')
            if data.get('home_phone') is not None:
                li.append(str(data['home_phone']))
            else:
                li.append('')
            try:
                li.append(str(data['connections']['skype']))
            except:
                li.append('')
            try:
                li.append(str(data['last_seen']['platform']))
            except:
                li.append('')
            try:
                li.append(str(data['last_seen']['time']))
            except:
                li.append('')
            try:
                li.append(str(data['occupation']['id']))
            except:
                li.append('')
            try:
                li.append(str(data['occupation']['name']))
            except:
                li.append('')
            try:
                li.append(str(data['occupation']['type']))
            except:
                li.append('')
            try:
                li.append(str(data['career'][0]['city_id']))
            except:
                li.append('')
            try:
                li.append(str(data['career'][0]['city_name']))
            except:
                li.append('')
            try:
                li.append(str(data['career'][0]['from']))
            except:
                li.append('')
            try:
                li.append(str(data['career'][0]['until']))
            except:
                li.append('')
            try:
                li.append(str(data['career'][0]['position']))
            except:
                li.append('')
            try:
                li.append(str(data['career'][0]['country_id']))
            except:
                li.append('')
            try:
                li.append(str(data['career'][0]['group_id']))
            except:
                li.append('')
            try:
                li.append(str(data['career'][0]['company']))
            except:
                li.append('')
            try:
                li.append(str(data['counters']['albums']))
            except:
                li.append('')
            try:
                li.append(str(data['counters']['videos']))
            except:
                li.append('')
            try:
                li.append(str(data['counters']['audios']))
            except:
                li.append('')
            try:
                li.append(str(data['counters']['photos']))
            except:
                li.append('')
            try:
                li.append(str(data['counters']['notes']))
            except:
                li.append('')
            try:
                li.append(str(data['counters']['friends']))
            except:
                li.append('')
            try:
                li.append(str(data['counters']['groups']))
            except:
                li.append('')
            try:
                li.append(str(data['counters']['online_friends']))
            except:
                li.append('')
            try:
                li.append(str(data['counters']['user_videos']))
            except:
                li.append('')
            try:
                li.append(str(data['counters']['followers']))
            except:
                li.append('')
            try:
                li.append(str(data['counters']['pages']))
            except:
                li.append('')
            try:
                li.append(str(data['education']['university']))
            except:
                li.append('')
            if data.get('university_name') is not None:
                li.append(str(data['university_name']))
            else:
                li.append('')
            if data.get('faculty') is not None:
                li.append(str(data['faculty']))
            else:
                li.append('')
            if data.get('graduation') is not None:
                li.append(str(data['graduation']))
            else:
                li.append('')
            if data.get('education_form') is not None:
                li.append(str(data['education_form']))
            else:
                li.append('')
            if data.get('home_town') is not None:
                li.append(str(data['home_town']))
            else:
                li.append('')
            try:
                li.append(str(data['military'][0]['country_id']))
            except:
                li.append('')
            try:
                li.append(str(data['military'][0]['unit']))
            except:
                li.append('')
            try:
                li.append(str(data['military'][0]['unit_id']))
            except:
                li.append('')
            try:
                li.append(str(data['military'][0]['from']))
            except:
                li.append('')
            try:
                li.append(str(data['military'][0]['until']))
            except:
                li.append('')
            if data.get('exports') is not None:
                li.append(str(data['exports']))
            else:
                li.append('')
            try:
                li.append(str(data['schools'][0]['city']))
            except:
                li.append('')
            try:
                li.append(str(data['schools'][0]['class']))
            except:
                li.append('')
            try:
                li.append(str(data['schools'][0]['id']))
            except:
                li.append('')
            try:
                li.append(str(data['schools'][0]['country']))
            except:
                li.append('')
            try:
                li.append(str(data['schools'][0]['name']))
            except:
                li.append('')
            try:
                li.append(str(data['schools'][0]['type']))
            except:
                li.append('')
            try:
                li.append(str(data['schools'][0]['type_str']))
            except:
                li.append('')
            try:
                li.append(str(data['schools'][0]['year_from']))
            except:
                li.append('')
            try:
                li.append(str(data['schools'][0]['year_graduated']))
            except:
                li.append('')
            try:
                li.append(str(data['schools'][0]['speciality']))
            except:
                li.append('')
            try:
                li.append(str(data['personal']['alcohol']))
            except:
                li.append('')
            try:
                li.append(str(data['personal']['inspired_by']))
            except:
                li.append('')
            try:
                _langs = ''
                for i in range(len(data['personal']['langs'])):
                    _langs += str(data['personal']['langs'][i]) + " "
                li.append(_langs)
            except:
                li.append('')
            try:
                li.append(str(data['personal']['life_main']))
            except:
                li.append('')
            try:
                li.append(str(data['personal'].get('people_main')))
            except:
                li.append('')
            try:
                li.append(str(data['personal']['political']))
            except:
                li.append('')
            try:
                li.append(str(data['personal']['religion']))
            except:
                li.append('')
            try:
                li.append(str(data['personal']['smoking']))
            except:
                li.append('')
            try:
                li.append(str(data['relatives'][0]['id']))
            except:
                li.append('')
            try:
                li.append(str(data['relatives'][0]['type']))
            except:
                li.append('')
            if data.get('has_photo') is not None:
                li.append(str(data['has_photo']))
            else:
                li.append('')
            if data.get('deactivated') is not None:
                li.append(str(data['deactivated']))
            else:
                li.append('')
            if data.get('is_closed') is not None:
                li.append(str(data['is_closed']))
            else:
                li.append('')
            all_data.append(li)
    db.loading(  # загрузка данных
        all_data,
        users_data_db_path,
        users_data_db_tname
    )




