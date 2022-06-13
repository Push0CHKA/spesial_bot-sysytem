import time

from flask import Flask, jsonify, request
from mods.db import download
from config.db_config import auth_path, auth_tname, prob_db_path, bot_char_path, bot_char_tname
from config.act_config import boxes_data, open_news, open_communities, open_friends
from mods.analys.worker import make_new_user_type
from mods.imit import auth, tasks
import os
import pyautogui as pag

app = Flask(__name__)


@app.route('/ibotlist', methods=['GET'])
def show_bot_list():
    ids_list = []
    bot_list = download(auth_path, auth_tname)
    for bl in bot_list:
        ids_list.append({'bot_id': bl[0]})
    return jsonify(ids_list)


@app.route('/imake-new-type', methods=['GET'])
def make_new_type():
    ids_list = request.args.get('ids').replace(';', '').split()
    new_type_name = request.args.get('name')
    try:
        make_new_user_type(ids_list, new_type_name)
        return jsonify('Success')
    except:
        return jsonify('Error')


@app.route('/ishow-bot-type', methods=['GET'])
def show_bot_type():
    dirname = prob_db_path
    types_list = []
    files = os.listdir(dirname)
    for file in files:
        types_list.append({'user_type': file.split('.')[0]})
    return jsonify(types_list)


@app.route('/ibot-work', methods=['GET'])
def bot_worker():
    bot_id = request.args.get('id')
    work_list = request.args.get('task').replace(';', '').split()

    bot_char = download(bot_char_path, bot_char_tname)
    bot_auth = download(auth_path, auth_tname)
    bchar = []
    for bc in bot_char:
        if int(bot_id) == bc[0]:
            bchar = bc
            break
    bauth = []
    for ba in bot_auth:
        if bot_id == ba[0]:
            bauth = ba
            break
    for wl in work_list:
        tsk = wl.replace(',', ' ').split()
        if int(tsk[0]) == 0:  # серфинг ленты
            surf_posts_count = int(tsk[1])
            like = False
            if int(tsk[2]) == 1:
                like = True
            repost = False
            if int(tsk[3]) == 1:
                repost = True
            comment = False
            if int(tsk[4]) == 1:
                comment = True
            auth.log_in(bot_id=bot_id, login=bauth[1], password=bauth[2], dur_speed_from=float(bchar[1]),
                        dur_speed_to=float(bchar[2]), typing_speed_from=float(bchar[3]),
                        typing_speed_to=float(bchar[4]))
            tasks.open_page(open_news, dur_speed_from=float(bchar[1]),
                            dur_speed_to=float(bchar[2]))
            tasks.surf(bot_id=int(bot_id), surf_posts_count=surf_posts_count, like=like, comment=comment, repost=repost)
            tasks.close_window(dur_speed_from=float(bchar[1]), dur_speed_to=float(bchar[2]))

        if int(tsk[0]) == 1:  # серфинг группы
            surf_posts_count = int(tsk[1])
            group_name = tsk[2]
            if int(tsk[3]) == 1:
                like = True
            else:
                like = False
            if int(tsk[4]) == 1:
                repost = True
            else:
                repost = False
            if int(tsk[5]) == 1:
                comment = True
            else:
                comment = False
            auth.log_in(bot_id=bot_id, login=bauth[1], password=bauth[2], dur_speed_from=float(bchar[1]),
                        dur_speed_to=float(bchar[2]), typing_speed_from=float(bchar[3]),
                        typing_speed_to=float(bchar[4]))
            tasks.find_and_open_group(group_name, dur_speed_from=float(bchar[1]),
                                      dur_speed_to=float(bchar[2]), typing_speed_from=float(bchar[3]),
                                      typing_speed_to=float(bchar[4]))
            time.sleep(3)
            tasks.surf(bot_id=int(bot_id), surf_posts_count=surf_posts_count, like=like, comment=comment, repost=repost)
            tasks.close_window(dur_speed_from=float(bchar[1]), dur_speed_to=float(bchar[2]))

        if int(tsk[0]) == 2:  # серфинг друзей
            surf_posts_count = int(tsk[1])
            friends_cnt = int(tsk[2])
            like = False
            if int(tsk[3]) == 1:
                like = True
            repost = False
            if int(tsk[4]) == 1:
                repost = True
            comment = False
            if int(tsk[5]) == 1:
                comment = True
            auth.log_in(bot_id=bot_id, login=bauth[1], password=bauth[2], dur_speed_from=float(bchar[1]),
                        dur_speed_to=float(bchar[2]), typing_speed_from=float(bchar[3]),
                        typing_speed_to=float(bchar[4]))
            tasks.open_page(open_friends, dur_speed_from=float(bchar[1]),
                            dur_speed_to=float(bchar[2]))
            tasks.surf_friends(bot_id=int(bot_id), friends_cnt=friends_cnt, posts_cnt=surf_posts_count,
                               like=like, comment=comment, repost=repost, dur_speed_from=float(bchar[1]),
                               dur_speed_to=float(bchar[2]))
            tasks.close_window(dur_speed_from=float(bchar[1]), dur_speed_to=float(bchar[2]))
    return jsonify({'Answer': 'done!'})


if __name__ == '__main__':
    time.sleep(3)
    pag.screenshot('a.png')
    app.run(debug=False, host='127.0.0.1')
