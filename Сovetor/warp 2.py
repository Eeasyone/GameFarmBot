


# ---------------------------------- ВАРП ПО ЗАПОЛНЕНИЮ КАРГО -----------------------------------------------------------

import pyautogui                                        # Библиотека для работы с устройствами ввода и экраном
import random                                           # Библиотека рандома
import time                                             # Библиотека для работы с временем 


while pyautogui.pixel(84,168) != (67,109,112):          # не равен зеленому
      pass

else:
    RND = random.randint                                # Сокращение функции рандома

    time.sleep(RND(1,3))                                # Рандом по ожиданию
    pyautogui.click(RND(1530,1590),RND(932,979))        # 1 ежик

    time.sleep(RND(1,2))
    pyautogui.click(RND(1629,1690),RND(932,979))        # 2 ежик

    time.sleep(RND(1,2))
    pyautogui.click(RND(1730,1790),RND(932,979))        # 3 ежик

    time.sleep(1)                                       # Ждем 1 сек
    pyautogui.click(RND(66,98),RND(288,326))            # Варп в док

