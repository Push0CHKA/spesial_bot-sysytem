from config import react_config
import pyautogui as pag
import random
import time
import PIL


def like_post(dur_speed_from, dur_speed_to):
    x, y = pag.locateCenterOnScreen(react_config.like_post,
                                    grayscale=False)
    pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()


def like_comment(dur_speed_from, dur_speed_to):
    x, y = pag.locateCenterOnScreen(react_config.like_comment,
                                    grayscale=False)
    pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()


def comment_post(comment, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to):
    x, y = pag.locateCenterOnScreen(react_config.comment_post,
                                    grayscale=False)
    pag.moveTo(x, y,
               duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()
    pag.typewrite(comment,
                  interval=(random.uniform(typing_speed_from, typing_speed_to)))
    time.sleep(random.uniform(0.5, 1))
    pag.press('enter')


def comment_comment(comment, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to):
    x, y = pag.locateCenterOnScreen(react_config.comment_comment,
                                    grayscale=False)
    pag.moveTo(x, y,
               duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()
    pag.typewrite(comment,
                  interval=(random.uniform(typing_speed_from, typing_speed_to)))
    time.sleep(random.uniform(0.5, 1))
    pag.press('enter')


def repost_to_wall(dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to, comment):
    x, y = pag.locateCenterOnScreen(react_config.repost,
                                    grayscale=False)
    pag.moveTo(x, y,
               duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()
    time.sleep(1)
    x, y = pag.locateCenterOnScreen(react_config.repost_to_wall_button,
                                    grayscale=False)
    pag.moveTo(x, y,
               duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()
    time.sleep(1)
    pag.typewrite(comment,
                  interval=(random.uniform(typing_speed_from, typing_speed_to)))
    time.sleep(random.uniform(0.5, 1))
    x, y = pag.locateCenterOnScreen(react_config.share_entry_button,
                                    grayscale=False)
    pag.moveTo(x, y,
               duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()

