import pyautogui
import random
import time
RND = random.randint
go_to_dock = 0


# Перетягивание локала в угол экрана
def main():
    if pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95) != None:
        left, right, top, pog = pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95)
        print(left, right)
        pyautogui.moveTo(left, right)
        pyautogui.dragTo(0, 1000, 5, button='left')

    # Проверка по цвету
    while pyautogui.pixel(360, 611) == (26, 137, 25) or pyautogui.pixel(360, 611) == (26, 137, 25):
        pass
    else:
        global go_to_dock
        time.sleep(RND(1, 4))
        pyautogui.click(RND(1530, 1590), RND(932, 979))
        time.sleep(RND(1, 2))
        pyautogui.click(RND(1629, 1690), RND(932, 979))
        time.sleep(RND(1, 2))
        pyautogui.click(RND(1730, 1790), RND(932, 979))
        time.sleep(1)
        pyautogui.click(RND(66, 98), RND(288, 326))
        go_to_dock = 1
        