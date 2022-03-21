from config import act_config
import pyautogui as pag
import webbrowser as web
from time import sleep
import random
import PIL


def log_in(bot_id, login, password, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to):
    web.open('https://vk.com', new=2)
    sleep(5)
    try:
        x, y = pag.locateCenterOnScreen(act_config.simple, grayscale=False)
        pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
        pag.click(x, y)
        x, y = pag.locateCenterOnScreen(act_config.login_box, grayscale=False)
        pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
        pag.click(x, y)
        pag.typewrite(login, interval=(random.uniform(0.8 * typing_speed_from, 0.8 * typing_speed_to)))  # login
        pag.moveTo(x+300, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
        pag.click(x+300, y)
        x, y = pag.locateCenterOnScreen(act_config.password_box, grayscale=False)
        pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
        pag.click(x, y)
        pag.typewrite(password, interval=(random.uniform(typing_speed_from, typing_speed_to)))  # password
        sleep(1)
        pag.press('enter')
        sleep(5)
        print(f' Bot_id: {bot_id}. Авторизация прошла успешно')
    except:
        pass
