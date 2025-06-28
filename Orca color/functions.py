import pyautogui                                          # Библиотека для работы с устройствами ввода и экраном
import time                                               # Библиотека для работы с временем
import random                                             # Библиотека рандома 
import requests

def teleg_message(text: str):
    token = "6082492296:AAFmjDU9mnXME-LQsMU72eP8SJ0Lc_VVbZY"
    url = "https://api.telegram.org/bot"
    channel_id = "@eeasyevebot"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={"chat_id": channel_id,"text": text})

    if r.status_code != 200:
        raise Exception("post_text error")






# РАЗГРУЗКА ШИПА В ДОКЕ
def cargo():
    while True:
        RND = random.randint                              # Сокращение функции рандома
        time.sleep(RND(2,3))                              # Рандом по ожиданию
        pyautogui.click(RND(65,100),RND(180,210))         # Кнопка инвентаря (самое левое положение)
        time.sleep(RND(2,3))                              # Рандом по ожиданию
        pyautogui.click(RND(155,385),RND(770,835))        # Нажимаем на отсек для руды
        time.sleep(RND(2,3))                              # Рандом по ожиданию
        pyautogui.click(RND(1360,1480),RND(900,1000))     # Нажимаем "Выбрать все" (Выбирает всю руду)
        time.sleep(RND(2,3))                              # Рандом по ожиданию
        pyautogui.click(RND(170,332),RND(208,270))        # Переместить в (кнопка) 
        time.sleep(RND(2,3))                              # Рандом по ожиданию
        pyautogui.click(RND(586,1000),RND(220,300))       # Кнопка склад 
        time.sleep(RND(3,5))                              # Рандом по ожиданию
        pyautogui.click(RND(1748,1778),RND(74,100))       # Закрыть инвентарь
        time.sleep(RND(2,3))

# ДВИГАЕМ ЛОКАЛ В УГОЛ        
        if pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95) != None:                  
            left, right, top, pog = pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95)
            print(left,right)
            pyautogui.moveTo(left, right)
            pyautogui.dragTo(0, 1000, 2, button='left')
        break                                             # Стоп цикла










# ВХОД В ДОК
def dock():
    RND = random.randint                                  # Сокращение функции рандома
    time.sleep(1)                                         # Ждем 1 сек
    pyautogui.click(RND(66,98),RND(288,326))              # Варп
    time.sleep(RND(1,4))                                  # Рандом по ожиданию
    pyautogui.click(RND(1530,1590),RND(932,979))          # 1 ежик
    time.sleep(RND(1,2))                                  # Рандом по ожиданию
    pyautogui.click(RND(1629,1690),RND(932,979))          # 2 ежик
    time.sleep(RND(1,2))                                  # Рандом по ожиданию                 
    pyautogui.click(RND(1730,1790),RND(932,979))          # 3 ежик







# ВЫХОД КОРАБЛЯ ИЗ ДОКА
def undock():
    while pyautogui.pixel(360,611) != (1,44,166):         # Не равен синему
            pass                                          # Ничего не делать 
    else:                                                 # Или
        RND = random.randint                              # Сокращение функции рандома
        time.sleep(RND(1,2))                              # Рандом по ожиданию
        pyautogui.click(RND(1670,1800),RND(350,375))      # Кнопка выхода из дока (ангар)
        time.sleep(RND(12,15))                            # Рандом по ожиданию
        pyautogui.click(RND(1745,1780),RND(575,612))      # Кнопка глазика (список белтов)
        time.sleep(RND(1,2))                              # Рандом по ожиданию
        pyautogui.click(RND(1418,1718),RND(327,400))      # Выбор белта 3 белта
        time.sleep(1)                                     # Ждем 1 сек
        pyautogui.click(RND(1168,1370),RND(438,514))      # Кнопка варп режима

        if pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95) != None:
            left, right, top, pog = pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95)
            print(left,right)
            pyautogui.moveTo(left, right)
            pyautogui.dragTo(0, 1000, 2, button='left')
        
        time.sleep(RND(2,3))                        
        set_coords()
        time.sleep(RND(79,83))                            # Ждем пока долетит до белтов
        pyautogui.click(RND(1230,1280),RND(936,974))      # Активация копательных дронов 1 нажатие
        time.sleep(RND(4,6))                              # Ждем
        pyautogui.click(RND(1230,1280),RND(936,974))      # Активация копательных дронов 2 нажатие
        time.sleep(RND(1,3))                              # Ждем
        pyautogui.click(RND(1090,1126),RND(835,875))      # Активация копательного импланта








# ДВИГАЕМ ЛОКАЛ В УГОЛ
def move_local():                                       
    if pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95) != None:
        left, right, top, pog = pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95)
        print(left,right)
        pyautogui.moveTo(left, right)
        pyautogui.dragTo(0, 1000, 2, button='left')











# УСТАНОВКА НАВИГАЦИИ
def set_coords():                                         # Установка навигации в автопилоте
    RND = random.randint                                  # Сокращение функции рандома
    pyautogui.click(RND(66,98),RND(288,326))              # Открытие меню выбора варпа
    time.sleep(RND(2,3))                                  # Рандом по ожиданию
    pyautogui.click(RND(109,356),RND(816,840))            # Кнопка дока
    time.sleep(RND(1,2))                                  # Рандом по ожиданию
    pyautogui.click(RND(480, 742), RND(360, 410))         # Какая-то кнопка
    time.sleep(RND(3,4))                                  # Рандом по ожиданию
    pyautogui.click(RND(357,424), RND(363, 407))          # Какая-то кнопка



    