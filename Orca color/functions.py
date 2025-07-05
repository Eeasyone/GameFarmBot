import pyautogui
import time
import random
import requests

RND = random.randint


def teleg_message(text: str):
    """отправка сообщения в telegram"""
    token = "6082492296:AAFmjDU9mnXME-LQsMU72eP8SJ0Lc_VVbZY"
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    channel_id = "@eeasyevebot"
    r = requests.post(url, data={"chat_id": channel_id, "text": text})
    if r.status_code != 200:
        raise Exception("post_text error")


# разгрузка корабля в доке 
def cargo():
    while True:
        time.sleep(RND(2, 3))
        pyautogui.click(RND(65, 100), RND(180, 210))
        time.sleep(RND(2, 3))
        pyautogui.click(RND(155, 385), RND(770, 835))
        time.sleep(RND(2, 3))
        pyautogui.click(RND(1360, 1480), RND(900, 1000))
        time.sleep(RND(2, 3))
        pyautogui.click(RND(170, 332), RND(208, 270))
        time.sleep(RND(2, 3))
        pyautogui.click(RND(586, 1000), RND(220, 300))
        time.sleep(RND(3, 5))
        pyautogui.click(RND(1748, 1778), RND(74, 100))

        move_local()
        break


# вход в док
def dock():
    time.sleep(1)
    pyautogui.click(RND(66, 98), RND(288, 326))
    time.sleep(RND(1, 4))
    pyautogui.click(RND(1530, 1590), RND(932, 979))
    time.sleep(RND(1, 2))
    pyautogui.click(RND(1629, 1690), RND(932, 979))
    time.sleep(RND(1, 2))
    pyautogui.click(RND(1730, 1790), RND(932, 979))


# выход корабля из дока
def undock():
    while pyautogui.pixel(360, 611) != (1, 44, 166):
        pass
    else:
        time.sleep(RND(1, 2))
        pyautogui.click(RND(1670, 1800), RND(350, 375))
        time.sleep(RND(12, 15))
        pyautogui.click(RND(1745, 1780), RND(575, 612))
        time.sleep(RND(1, 2))
        pyautogui.click(RND(1418, 1718), RND(327, 400))
        time.sleep(1)
        pyautogui.click(RND(1168, 1370), RND(438, 514))

        move_local()
        time.sleep(RND(2, 3))
        set_coords()
        time.sleep(RND(79, 83))
        pyautogui.click(RND(1230, 1280), RND(936, 974))
        time.sleep(RND(4, 6))
        pyautogui.click(RND(1230, 1280), RND(936, 974))
        time.sleep(RND(1, 3))
        pyautogui.click(RND(1090, 1126), RND(835, 875))


# двигаем локал в угол
def move_local():
    location = pyautogui.locateOnScreen("Screenshot_1.png", confidence=0.95)
    if location:
        left, right, top, pog = location
        print(left, right)
        pyautogui.moveTo(left, right)
        pyautogui.dragTo(0, 1000, 2, button='left')


# установка навигации
def set_coords():
    pyautogui.click(RND(66, 98), RND(288, 326))
    time.sleep(RND(2, 3))
    pyautogui.click(RND(109, 356), RND(816, 840))
    time.sleep(RND(1, 2))
    pyautogui.click(RND(480, 742), RND(360, 410))
    time.sleep(RND(3, 4))
    pyautogui.click(RND(357, 424), RND(363, 407))
