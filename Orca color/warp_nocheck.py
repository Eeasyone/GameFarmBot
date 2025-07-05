import pyautogui
import random
import time 
RND = random.randint

go_to_dock = 0

def main():
        global go_to_dock
        time.sleep(RND(1,4))
        pyautogui.click(RND(1530,1590),RND(932,979))
        time.sleep(RND(1,2))
        pyautogui.click(RND(1629,1690),RND(932,979))
        time.sleep(RND(1,2))
        pyautogui.click(RND(1730,1790),RND(932,979))
        time.sleep(1)
        pyautogui.click(RND(66,98),RND(288,326))
        go_to_dock = 1
