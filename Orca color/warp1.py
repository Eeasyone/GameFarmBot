


# --------------------------- ВАРП С ПРОВЕРКОЙ НА НЕЙТРАЛА ИЛИ КРАСНОГО ----------------------------------------------

import pyautogui                                            # Библиотека для работы с устройствами ввода и экраном
import random                                               # Библиотека рандома
import time                                                 # Библиотека для работы с временем 
RND = random.randint                                        # Сокращение рандома
go_to_dock = 0



#ПЕРЕТАГИВАНИЕ ЛОКАЛА В УГОЛ 
def main():
    if pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95) != None:
        left, right, top, pog = pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95)
        print(left,right)
        pyautogui.moveTo(left, right)
        pyautogui.dragTo(0, 1000, 5, button='left')



#ПРОВЕРКА ПО ЦВЕТУ    
    while pyautogui.pixel(360,611) == (26,137,25) or pyautogui.pixel(360,611) == (26,137,25):           # Не равен синему   (26,137,25 - зеленый   1,44,166 - синий)
        pass                                                                                            # Ничего не делать
    else:                                                                                               # Или      
        global go_to_dock
        time.sleep(RND(1,4))                                                                            # Рандом по ожиданию
        pyautogui.click(RND(1530,1590),RND(932,979))                                                    # 1 ежик
        time.sleep(RND(1,2))                                                                            # Рандом по ожиданию
        pyautogui.click(RND(1629,1690),RND(932,979))                                                    # 2 ежик
        time.sleep(RND(1,2))                                                                            # Рандом по ожиданию
        pyautogui.click(RND(1730,1790),RND(932,979))                                                    # 3 ежик
        time.sleep(1)                                                                                   # Ждем 1 сек
        pyautogui.click(RND(66,98),RND(288,326))                                                        # Варп в док
        go_to_dock = 1                                                                                  # Корабль в доке (переменная =1)


