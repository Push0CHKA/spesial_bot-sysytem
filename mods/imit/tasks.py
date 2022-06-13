import time

from mods.imit import react, action
from mods.db import download
from random import randint, uniform
from time import sleep
from config import act_config
from config.db_config import users_main_data_path, users_main_data_tname
from mods import db
from config.db_config import comments_db_path, comments_db_tname

from config.db_config import bot_char_path, bot_char_tname

import pyautogui as pag


# метод, реализующий серфинг и лайк постов
def surf_(surf_posts_count, post_view_time):
    for length in range(surf_posts_count):
        action.scroll_down(32)
        sleep(post_view_time)


# метод, реализующий серфинг и лайк постов
def surf_and_like(surf_posts_count, post_view_time, like_post_in_feed_probability_, dur_speed_from, dur_speed_to):
    for length in range(surf_posts_count):
        # случайное число в интервале
        like_post_in_feed_probability = randint(1, 100)
        for i in range(3):
            try:
                # условия лайка поста
                if like_post_in_feed_probability < like_post_in_feed_probability_:
                    react.like_post(dur_speed_from, dur_speed_to)
                    break
                else:
                    action.scroll_down(10)
            except:
                pass
        action.scroll_down(32)
        sleep(post_view_time)


# метод, реализующий серфинг и лайк постов
def surf_and_like_and_repost(surf_posts_count, post_view_time, like_post_in_feed_probability_,
                             repost_feed_probability_, dur_speed_to, dur_speed_from, typing_speed_from,
                             typing_speed_to):
    action.move_and_click(act_config.open_news, dur_speed_from, dur_speed_to)
    for length in range(surf_posts_count):
        # случайное число в интервале
        like_post_in_feed_probability = randint(1, 100)
        repost_feed_probability = randint(1, 100)
        for i in range(3):
            try:
                # условия лайка поста
                if like_post_in_feed_probability < like_post_in_feed_probability_:
                    react.like_post(dur_speed_from, dur_speed_to)
                    break
                else:
                    action.scroll_down(10)
            except:
                pass
        for i in range(3):
            try:
                comment = ''
                # условия лайка поста
                if repost_feed_probability < repost_feed_probability_:
                    react.repost_to_wall(dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to, comment)
                    break
                else:
                    action.scroll_down(10)
            except:
                pass
        action.scroll_down(32)
        sleep(post_view_time)


# метод, реализующий серфинг и лайк постов
def surf_and_like_and_comment(surf_posts_count, post_view_time, like_post_in_feed_probability_,
                              comment_post_in_feed_probability_, dur_speed_from, dur_speed_to,
                              typing_speed_from, typing_speed_to):
    for length in range(surf_posts_count):
        # случайное число в интервале
        like_post_in_feed_probability = randint(1, 100)
        comment_post_in_feed_probability = randint(1, 100)
        for i in range(3):
            try:
                # условия лайка поста
                if like_post_in_feed_probability < like_post_in_feed_probability_:
                    react.like_post(dur_speed_from, dur_speed_to)
                    break
                else:
                    action.scroll_down(10)
            except:
                pass
        for i in range(3):
            try:
                comments = db.download(comments_db_path, comments_db_tname)
                random_ch = randint(0, len(comments) - 1)
                # условия лайка поста
                if comment_post_in_feed_probability < comment_post_in_feed_probability_:
                    react.comment_post(comments[random_ch][1], dur_speed_from, dur_speed_to, typing_speed_from,
                                       typing_speed_to)
                    break
                else:
                    action.scroll_down(10)
            except:
                pass
        action.scroll_down(32)
        sleep(post_view_time)


# метод, реализующий серфинг и лайк постов
def surf_and_like_and_comment_and_repost(surf_posts_count, post_view_time, like_post_in_feed_probability_,
                                         comment_post_in_feed_probability_, repost_post_in_feed_probability_,
                                         dur_speed_from, dur_speed_to,
                                         typing_speed_from, typing_speed_to):
    for length in range(surf_posts_count):
        # случайное число в интервале
        like_post_in_feed_probability = randint(1, 100)
        comment_post_in_feed_probability = randint(1, 100)
        repost_feed_probability = randint(1, 100)
        for i in range(3):
            try:
                # условия лайка поста
                if like_post_in_feed_probability < like_post_in_feed_probability_:
                    react.like_post(dur_speed_from, dur_speed_to)
                    break
                else:
                    action.scroll_down(10)
            except:
                pass
        for i in range(3):
            try:
                comments = db.download(comments_db_path, comments_db_tname)
                random_ch = randint(0, len(comments) - 1)
                # условия лайка поста
                if comment_post_in_feed_probability < comment_post_in_feed_probability_:
                    react.comment_post(comments[random_ch][1], dur_speed_from, dur_speed_to, typing_speed_from,
                                       typing_speed_to)
                    break
                else:
                    action.scroll_down(10)
            except:
                pass
        for i in range(3):
            try:
                comment = ''
                # условия лайка поста
                if repost_feed_probability < repost_post_in_feed_probability_:
                    react.repost_to_wall(dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to, comment)
                    break
                else:
                    action.scroll_down(10)
            except:
                pass
        action.scroll_down(32)
        sleep(post_view_time)


def open_page(page, dur_speed_from, dur_speed_to):
    action.move_and_click(page, dur_speed_from, dur_speed_to)


def surf(bot_id, surf_posts_count, like=False, comment=False, repost=False):
    data = db.download(bot_char_path, bot_char_tname)
    find_flag = False
    for d in data:
        if str(d[0]) == str(bot_id):
            find_flag = True
            dur_speed_from = d[1]
            dur_speed_to = d[2]
            typing_speed_from = d[3]
            typing_speed_to = d[4]
            post_view_time = d[5]
            like_post_feed_prob = d[6]
            repost_post_feed_prob = d[7]
            comment_post_feed_prob = d[8]
            break
    if not find_flag:
        return False
    for length in range(surf_posts_count):
        if like:
            like_post_in_feed_probability = randint(0, 100)
            for i in range(3):
                try:
                    # условия лайка поста
                    if like_post_in_feed_probability < like_post_feed_prob:
                        react.like_post(dur_speed_from, dur_speed_to)
                        break
                    else:
                        action.scroll_down(10)
                except:
                    pass
        if repost:
            repost_feed_probability = randint(0, 100)
            for i in range(3):
                try:
                    comment = ''
                    # условия лайка поста
                    if repost_feed_probability < repost_post_feed_prob:
                        react.repost_to_wall(dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to, comment)
                        break
                    else:
                        action.scroll_down(10)
                except:
                    pass
        if comment:
            comment_post_in_feed_probability_ = randint(0, 100)
            for i in range(3):
                try:
                    comments = db.download(comments_db_path, comments_db_tname)
                    random_ch = randint(0, len(comments) - 1)
                    # условия лайка поста
                    if comment_post_feed_prob < comment_post_in_feed_probability_:
                        react.comment_post(comments[random_ch][1], dur_speed_from, dur_speed_to, typing_speed_from,
                                           typing_speed_to)
                        break
                    else:
                        action.scroll_down(10)
                except:
                    pass
        action.scroll_down(32)
        sleep(post_view_time)


# метод, реализующий поиск определенной группы и ее открытия
def find_and_open_group(group_name, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to):
    action.move_and_click(act_config.open_communities, dur_speed_from, dur_speed_to)
    action.move_and_click(act_config.simple, dur_speed_from, dur_speed_to)
    sleep(randint(1, 2))
    action.move_and_click(act_config.search_results, dur_speed_from, dur_speed_to)
    action.print_text(group_name, typing_speed_from, typing_speed_to)
    pag.press('enter')
    sleep(randint(1, 2))
    x, y = pag.locateCenterOnScreen(act_config.results, grayscale=False)
    pag.moveTo(x, y + 80, duration=(uniform(dur_speed_from, dur_speed_to)))
    pag.click(x, y + 80)


def surf_friends(bot_id, friends_cnt, posts_cnt, like, comment, repost, dur_speed_from, dur_speed_to):
    open_page(act_config.open_friends, dur_speed_from=dur_speed_from, dur_speed_to=dur_speed_to)
    action.move_and_click(act_config.simple, dur_speed_from, dur_speed_to)
    for j in range(20):
        pag.vscroll(-10)
        sleep(0.01)
    icon_len = 0
    for i in range(friends_cnt):
        action.move_and_click(act_config.simple, dur_speed_from, dur_speed_to)
        for j in range(icon_len):
            pag.vscroll(-10)
            sleep(0.01)
        x, y = pag.locateCenterOnScreen(act_config.line, grayscale=False)
        pag.moveTo(x, y + 25, duration=(uniform(dur_speed_from, dur_speed_to)))
        icon_len += 30
        pag.click()
        sleep(3)
        surf(bot_id, posts_cnt, like=like, comment=comment, repost=repost)
        action.move_and_click(act_config.back_page, dur_speed_from=dur_speed_from, dur_speed_to=dur_speed_to)
        sleep(3)


# метод, реализующий заполнение основных данных о пользователе
def fill_main_data(boxes_data, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to):
    users_main_data = download(users_main_data_path, users_main_data_tname)
    random_num = randint(0, len(users_main_data) - 1)
    users_main_data = users_main_data[random_num]
    action.move_and_click(act_config.open_my_page, dur_speed_from, dur_speed_to)
    sleep(randint(3, 5))
    action.move_and_click(act_config.open_edit, dur_speed_from, dur_speed_to)
    sleep(randint(1, 2))
    action.move_and_click(act_config.open_interests, dur_speed_from, dur_speed_to)
    sleep(randint(1, 2))
    cnt = 0
    for box in boxes_data:
        try:
            action.move_and_click(box, dur_speed_from, dur_speed_to)
            action.print_text(users_main_data[cnt], typing_speed_from, typing_speed_to)
            action.scroll_down(4)
            cnt += 1
        except:
            cnt += 1
            print(f' Проблема с изображениями {box}')
    action.move_and_click(act_config.save_button, dur_speed_from, dur_speed_to)
    sleep(randint(2, 5))


def close_window(dur_speed_from, dur_speed_to):
    sleep(randint(1, 2))
    action.move_and_click(act_config.close_button, dur_speed_from, dur_speed_to)
    sleep(randint(1, 2))
