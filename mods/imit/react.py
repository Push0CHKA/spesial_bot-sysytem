import pyautogui as pag
import random
import time
import PIL


def like_post(dur_speed_from, dur_speed_to):
    x, y = pag.locateCenterOnScreen(r"img\react\like.png", grayscale=False)
    pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()


def like_comment(dur_speed_from, dur_speed_to):
    x, y = pag.locateCenterOnScreen(r"img\react\like_comment.png", grayscale=False)
    pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()


def comment_post(comment, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to):
    x, y = pag.locateCenterOnScreen(r"img\react\comment_post.png", grayscale=False)
    pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()
    pag.typewrite(comment, interval=(random.uniform(typing_speed_from, typing_speed_to)))
    time.sleep(random.uniform(0.5, 1))
    pag.press('enter')


def comment_comment(comment, dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to):
    x, y = pag.locateCenterOnScreen(r"img\react\answer_to_comment.png", grayscale=False)
    pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()
    pag.typewrite(comment, interval=(random.uniform(typing_speed_from, typing_speed_to)))
    time.sleep(random.uniform(0.5, 1))
    pag.press('enter')


def repost_wall(dur_speed_from, dur_speed_to, typing_speed_from, typing_speed_to, comment):
    x, y = pag.locateCenterOnScreen(r"img\react\repost.png", grayscale=False)
    pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()
    time.sleep(1)
    x, y = pag.locateCenterOnScreen(r"img\react\repost_to_wall.png", grayscale=False)
    pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()
    time.sleep(1)
    pag.typewrite(comment, interval=(random.uniform(typing_speed_from, typing_speed_to)))
    time.sleep(random.uniform(0.5, 1))
    x, y = pag.locateCenterOnScreen(r"img\react\share_entry_button.png", grayscale=False)
    pag.moveTo(x, y, duration=(random.uniform(dur_speed_from, dur_speed_to)))
    pag.click()

