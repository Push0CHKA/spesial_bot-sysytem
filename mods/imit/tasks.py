from mods.imit import react,action
from random import randint, uniform
from time import sleep
from config import act_config
import pyautogui as pag


# метод, реализующий серфинг ленты и лайк постов
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


# метод, реализующий поиск определенной группы и ее открытия
def find_and_open_group(group_name, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to):
    action.move_and_click(act_config.open_communities, dur_speed_from, dur_speed_to)
    sleep(randint(1, 2))
    action.print_text(group_name, typing_speed_from, typing_speed_to)
    pag.press('enter')
    sleep(randint(1, 2))
    x, y = pag.locateCenterOnScreen(act_config.search_results, grayscale=False)
    pag.moveTo(x, y + 80, duration=(uniform(dur_speed_from, dur_speed_to)))
    pag.click(x, y + 80)


# метод, реализующий заполнение основных данных о пользователе
def fill_main_data(boxes_data, text_data, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to):
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
            action.print_text(text_data[cnt], typing_speed_from, typing_speed_to)
            action.scroll_down(5)
            cnt += 1
        except:
            cnt += 1
            print(f' Проблема с изображениями {box}')
    action.move_and_click(act_config.save_button, dur_speed_from, dur_speed_to)
    sleep(randint(2, 5))










