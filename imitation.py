import time
from mods import db
from mods.imit import action, auth, tasks, react
from config import act_config, db_config
import pyautogui as pag


bot_id = '1'
dur_speed_from = 1.2
dur_speed_to = 1.3
typing_speed_from = 0.5
typing_speed_to = 0.3
surf_length = 10
post_view_time = 5
like_post_in_feed_probability_ = 50
group_name = 'mdk'
boxes_data = [act_config.box_activities, act_config.box_interests, act_config.box_favorite_music,
              act_config.box_favorite_films, act_config.box_favorite_tv, act_config.box_favorite_books,
              act_config.box_favorite_games, act_config.box_favorite_quotes, act_config.box_about_me]
text_data = ['text1', 'text2', 'text3', 'text4', 'text5', 'text6', 'text7', 'text8', 'text9']


time.sleep(5)
#tasks.find_and_open_group(group_name, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to)
#tasks.surf_and_like(surf_length, post_view_time, like_post_in_feed_probability_, dur_speed_from, dur_speed_to)
#tasks.fill_main_data(boxes_data, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to)

#####
#react.like_post(dur_speed_from, dur_speed_to)
#react.like_comment(dur_speed_from, dur_speed_to)
comment = 'comment'

#pag.screenshot('a.png')
tasks.surf_friends(1, 10, 1, False, False, False, dur_speed_from, dur_speed_to)
#react.comment_post(comment, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to)
#react.comment_comment(comment, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to)
#react.repost_to_wall(dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to, comment)

