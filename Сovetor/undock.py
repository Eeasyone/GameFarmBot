


#------------------------- ВЫЛЕТ ИЗ ДОКА + ВАРП НА БЕЛТ + АКТИВАЦИЯ ДРОНОВ --------------------------

import pyautogui                                      # Библиотека для работы с устройствами ввода и экраном
import random                                         # Библиотека рандома
import time                                           # Библиотека для работы с временем 


if pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95) != None:
    left, right, top, pog = pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95)
    print(left,right)
    pyautogui.moveTo(left, right)
    pyautogui.dragTo(0, 1000, 5, button='left')
 
while pyautogui.pixel(341,614) != (26,137,25):         # Не равен зелен
        pass
else:
    RND = random.randint                              # Сокращение функции рандома
    
    time.sleep(RND(2,4))                              # Рандом по ожиданию
    pyautogui.click(RND(1670,1800),RND(350,375))      # Кнопка выхода из дока (ангар)

    time.sleep(RND(14,17))                            # Рандом по ожиданию
    pyautogui.click(RND(1745,1780),RND(575,612))      # Кнопка глазика (список белтов)

    time.sleep(RND(3,4))                              # Рандом по ожиданию
    pyautogui.click(RND(1418,1718),RND(327,400))      # Выбор белта 3 белта

    time.sleep(3)                                     # Ждем 1 сек
    pyautogui.click(RND(1168,1370),RND(438,514))      # Кнопка варп режима

    time.sleep(RND(20,22))                            # Ждем пока долетит до белтов
    pyautogui.click(RND(1230,1280),RND(936,974))      # Активация копательных дронов 1 нажатие

    time.sleep(RND(1,3))                              # Ждем
    pyautogui.click(RND(1355,1380),RND(936,974))      # Активация копательных дронов 2 нажатие

    time.sleep(RND(1,3))                              # Ждем
    pyautogui.click(RND(1435,1485),RND(936,974))      # Активация копательных дронов 3 нажатие