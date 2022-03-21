import pyautogui as pag
from time import sleep
import random
import PIL


def scroll_down(scroll_len):
    for i in range(scroll_len):
        pag.vscroll(random.randint(-50, -20))
        sleep(0.01)


def scroll_up(scroll_len):
    for i in range(scroll_len):
        pag.vscroll(random.randint(50, 20))
        sleep(0.01)


def move_and_click(from_act_config, dur_speed_from, dur_speed_to):
    x, y = pag.locateCenterOnScreen(from_act_config, grayscale=False)
    pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()


def print_text(text, typing_speed_from, typing_speed_to):
    pag.typewrite(text, interval=(random.uniform(typing_speed_from, typing_speed_to)))
