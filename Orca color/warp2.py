


# --------------------------- ВАРП БЕЗ ПРОВЕРКИ ---------------------------------------

import pyautogui                                            # Библиотека для работы с устройствами ввода и экраном
import random                                               # Библиотека рандома
import time                                                 # Библиотека для работы с временем 
RND = random.randint                                        # Сокращение функции рандома

go_to_dock = 0

def main():
        global go_to_dock
        time.sleep(RND(1,4))                                # Рандом по ожиданию
        pyautogui.click(RND(1530,1590),RND(932,979))        # 1 ежик
        time.sleep(RND(1,2))                                # Рандом по ожиданию
        pyautogui.click(RND(1629,1690),RND(932,979))        # 2 ежик
        time.sleep(RND(1,2))                                # Рандом по ожиданию
        pyautogui.click(RND(1730,1790),RND(932,979))        # 3 ежик
        time.sleep(1)                                       # Ждем 1 сек
        pyautogui.click(RND(66,98),RND(288,326))            # Варп в док
        go_to_dock = 1

        