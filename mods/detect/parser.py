import os

import requests
from config import db_config, pars_config
from mods import db


def download_main_data(user_ids, token, friend_id=-1):
    all_data = []
    if not os.path.exists(db_config.main_db_path):
        db.make_db(db_config.main_db_path, db_config.main_db_tname, db_config.main_db_fields)
    main_inf = requests.get('https://api.vk.com/method/users.get',
                            params={
                                'access_token': token,
                                'v': pars_config.version,
                                'user_ids': user_ids,
                                'fields': pars_config.user_fields
                            })
    if main_inf.status_code == 200:
        main_data = main_inf.json()['response']
        for data in main_data:
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
            try:
                li.append(data['connections']['skype'])
            except:
                li.append('')
            try:
                li.append(data['instagram'])
            except:
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
                li.append(str(data['education'][0]['university']))
            except:
                li.append('')
            try:
                li.append(str(data['education'][0]['university_name']))
            except:
                li.append('')
            try:
                li.append(str(data['education'][0]['faculty']))
            except:
                li.append('')
            try:
                li.append(str(data['education'][0]['graduation']))
            except:
                li.append('')
            try:
                li.append(str(data['education'][0]['education_form']))
            except:
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
                li.append(str(data['personal']['people_main']))
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
            if friend_id != -1:
                li.insert(0, friend_id)
                all_data.append(li)
            else:
                db.loading([li], db_config.main_db_path, db_config.main_db_tname)
    if friend_id != -1:
        db.loading(all_data, db_config.friends_db_path, db_config.friends_db_tname)


def download_friends_data(user_id, token):
    db.make_db(db_config.friends_db_path, db_config.friends_db_tname, db_config.friends_db_fields)
    friends_list_inf = requests.get('https://api.vk.com/method/friends.get',
                                    params={
                                        'access_token': token,
                                        'v': pars_config.version,
                                        'user_id': user_id,
                                    })
    if friends_list_inf.status_code == 200:
        friends_list_data = friends_list_inf.json()['response']['items']
        for friend_id in friends_list_data:
            download_main_data(user_ids=friend_id, token=token, friend_id=user_id)


def download_wall_data(user_id, token):
    db.make_db(db_config.wall_db_path, db_config.wall_db_tname, db_config.wall_db_fields)
    wall_inf = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': pars_config.version,
                                'owner_id': user_id,
                                'count': 10,
                            }
                            )
    if wall_inf.status_code == 200:
        wall_inf_data = wall_inf.json()['response']['items']
        if len(wall_inf_data) > 0:
            data = []
            for wall_data in wall_inf_data:
                db_data = [user_id, wall_data['id'], wall_data['from_id'], wall_data['owner_id'], wall_data['type']]
                if wall_data['text'] is not None and wall_data['text'] != '':
                    db_data.append(wall_data['text'])
                else:
                    db_data.append('')
                try:
                    img_str = ''
                    try:
                        for i in range(len(wall_data['attachments'])):
                            img_str += wall_data['attachments'][i]['photo']['sizes'][6]['url'] + ';'
                    except:
                        img_str += wall_data['attachments'][0]['photo']['sizes'][6]['url'] + ';'
                    db_data.append(img_str)
                except:
                    db_data.append('')
                try:
                    db_data.extend((wall_data['copy_history'][0]['id'], wall_data['copy_history'][0]['owner_id'],
                                    wall_data['copy_history'][0]['from_id'], wall_data['copy_history'][0]['post_type']))
                    if wall_data['copy_history'][0]['text'] is not None and wall_data['copy_history'][0]['text'] != '':
                        db_data.append(wall_data['copy_history'][0]['text'])
                    else:
                        db_data.append('')
                    try:
                        img_str = ''
                        try:
                            for i in range(len(wall_data['copy_history'][0]['attachments'])):
                                img_str += wall_data['copy_history'][0]['attachments'][i]['photo']['sizes'][6]['url'] + ';'
                        except:
                            img_str += wall_data['copy_history'][0]['attachments'][0]['photo']['sizes'][6]['url'] + ';'
                        db_data.append(img_str)
                    except:
                        db_data.append('')
                except:
                    db_data.extend(('', '', '', '', '', ''))
                cnt = 0
                for dbd in db_data:
                    if dbd == '':
                        cnt += 1
                if cnt == 8:
                    continue
                data.append(db_data)
            db.loading(data, db_config.wall_db_path, db_config.wall_db_tname)
