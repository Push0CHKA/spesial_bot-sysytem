import time
from mods import db
from mods.imit import action, auth
from config import act_config, db_config
import pyautogui as pag


bot_id = '1'
dur_speed_from = 1.2
dur_speed_to = 1.3
typing_speed_from = 0.5
typing_speed_to = 0.3

time.sleep(5)
action.move_and_click(act_config.box_favorite_tv, 0.2, 0.3)
#time.sleep(2)
#pag.screenshot('a.png')

