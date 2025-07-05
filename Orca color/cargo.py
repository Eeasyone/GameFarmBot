import pyautogui
import random
import time

RND = random.randint

# Разгрузка орки после дока (залет в ангар)
def main():
    while True:
        time.sleep(RND(3, 5))
        pyautogui.click(RND(70, 105), RND(178, 215))
        time.sleep(RND(2, 3))
        pyautogui.click(RND(82, 389), RND(762, 835))
        time.sleep(RND(1, 2))
        pyautogui.click(RND(1360, 1481), RND(900, 1000))
        time.sleep(RND(1, 2))
        pyautogui.click(RND(170, 332), RND(208, 270))
        time.sleep(RND(1, 2))
        pyautogui.click(RND(586, 1000), RND(220, 300))
        time.sleep(RND(3, 5))
        pyautogui.click(RND(1748, 1778), RND(74, 100))
        break
    