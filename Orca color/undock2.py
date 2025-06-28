


# ------------------------- ВЫЛЕТ ИЗ ДОКА БЕЗ ПРОВЕРКИ --------------------------

import pyautogui                                                                        # Библиотека для работы с устройствами ввода и экраном
import random                                                                           # Библиотека рандома
import time                                                                             # Библиотека для работы с временем 
import configparser                                                                     # Добавление библиотеки парсера
RND = random.randint                                                                    # Сокращение функции рандома


#ПЕРЕТАГИВАНИЕ ЛОКАЛА В УГОЛ 
def main():
    if pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95) != None:
        left, right, top, pog = pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95)
        print(left,right)
        pyautogui.moveTo(left, right)
        pyautogui.dragTo(0, 1000, 1, button='left')
    

#ПЕРЕМЕННАЯ ПАРСЕРА        
        config = configparser.ConfigParser()                                            # Создаём переменную парсера
        config.read("button_mapping.ini")                                               # Читаем конфиг
        amount_buttons = config["Main"]["amwarpbutt"]                                   # Читаем из конфига количество кнопок на которые можно нажимать
        selected_button = RND(1, int(amount_buttons))                                   # Рандомизируем с какой кнопкой будем работать
        print(selected_button)                                                          # рандом по кнопке???
        x_m_left = int(config["Main"]["x_left"])                                        # ?
        x_m_right = int(config["Main"]["x_right"])                                      # ?
        x_s_right = int(config["Main"]["x_left2"])                                      # ?
        x_s_left = int(config["Main"]["x_right2"])                                      # ?
        y_top = int(config["Warp.button." + str(selected_button)]["y_top"])             # ?
        y_bottom = int(config["Warp.button." + str(selected_button)]["y_bottom"])       # ?
        y_top2 = int(config["Warp.button." + str(selected_button)]["y_top2"])           # ?
        y_bottom2 = int(config["Warp.button." + str(selected_button)]["y_bottom2"])     # ?


#ВЫХОД ИЗ ДОКА
        time.sleep(RND(1,2))                                                            # Рандом по ожиданию
        pyautogui.click(RND(1670,1800),RND(350,375))                                    # Кнопка выхода из дока (ангар)
        time.sleep(RND(12,15))                                                          # Рандом по ожиданию
        pyautogui.click(RND(1745,1780),RND(575,612))                                    # Кнопка глазика (список белтов)
        time.sleep(RND(1,2))                                                            # Рандом по ожиданию


#ПРОЖАТИЕ КНОПКИ ВАРП РЕЖИМА
        pyautogui.click(RND(x_m_left, x_m_right), RND(y_top, y_bottom))
        time.sleep(RND(2,3))
        pyautogui.click(RND(x_s_right, x_s_left), RND(y_top2, y_bottom2))
        time.sleep(1)                                                                             # Ждем 1 сек
        pyautogui.click(RND(1168,1370),RND(438,514))                                              # Кнопка варп режима
        

#ПЕРЕТАГИВАНИЕ ЛОКАЛА В УГОЛ 
        if pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95) != None:                   # Ориентир на скрин
            left, right, top, pog = pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95)   #?
            print(left,right)                                                                      #? 
            pyautogui.moveTo(left, right)                                                          # Координаты движения
            pyautogui.dragTo(0, 1000, 5, button='left')                                            # Скорость переноса

        
#НАСТРОЙКА НАВИГАТОРА (СОЗДАНИЕ ТОЧКИ ВАРПА)
        pyautogui.click(RND(67,104),RND(289,321))           # Навигатор (1 положение)
        time.sleep(RND(1,2))                                # Ждем
        pyautogui.click(RND(77,343),RND(430,482))           # Кнопка   
        time.sleep(RND(1,2))                                # Ждем
        pyautogui.click(RND(462,750),RND(362,410))          # Кнопка
        time.sleep(RND(1,2))                                # Ждем
        pyautogui.click(RND(355,426),RND(357,401))          # Кнопка

        
#ДОБАВИТЬ ПРОКРУТКУ ЛОКАЛА


#АКТИВАЦИЯ ДОБЫВАЮЩИХ ДРОНОВ И ИМПЛАНТА
        time.sleep(RND(79,83))                              # Ждем пока долетит до белтов
        pyautogui.click(RND(1230,1280),RND(936,974))        # Активация копательных дронов 1 нажатие
        time.sleep(RND(4,6))                                # Ждем
        pyautogui.click(RND(1230,1280),RND(936,974))        # Активация копательных дронов 2 нажатие
        time.sleep(RND(1,3))                                # Ждем
        pyautogui.click(RND(1090,1126),RND(835,875))        # Активация копательного импланта