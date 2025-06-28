import pyautogui                                          # Библиотека для работы с устройствами ввода и экраном
import time                                               # Библиотека для работы с временем
import random                                             # Библиотека рандома 
import requests
import configparser
import telebot
import mss
import PIL

def teleg_message(text: str):
    token = "5632127059:AAEQiCBHXBYZkRbRmT7q_DeknNXTvgHiMww"
    url = "https://api.telegram.org/bot"
    channel_id = "@wixiorbot"
    url += token
    method = url + "/sendMessage"

    r = requests.post(method, data={"chat_id": channel_id,"text": text})

    if r.status_code != 200:
        raise Exception("post_text error")

def teleg_photo():

    bot = telebot.TeleBot("5632127059:AAEQiCBHXBYZkRbRmT7q_DeknNXTvgHiMww", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN
    with mss.mss() as mss_instance:
        monitor = mss_instance.monitors[0]
        screenshot = mss_instance.grab(monitor)

        img = PIL.Image.frombytes("RGB", screenshot.size, screenshot.bgra, "raw", "BGRX")  # Convert to PIL.Image
    bot.send_photo("@wixiorbot", img)

# РАЗГРУЗКА ШИПА В ДОКЕ
def cargo():
    while True:
        RND = random.randint                              # Сокращение функции рандома
        time.sleep(RND(3,5))                              # Рандом по ожиданию
        pyautogui.click(RND(65,100),RND(180,210))         # Кнопка инвентаря (самое левое положение)
        time.sleep(RND(4,6))                              # Рандом по ожиданию
        pyautogui.click(RND(155,385),RND(770,835))        # Нажимаем на отсек для руды
        time.sleep(RND(4,6))                              # Рандом по ожиданию
        pyautogui.click(RND(1360,1480),RND(900,1000))     # Нажимаем "Выбрать все" (Выбирает всю руду)
        time.sleep(RND(4,6))                              # Рандом по ожиданию
        pyautogui.click(RND(170,332),RND(208,270))        # Переместить в (кнопка) 
        time.sleep(RND(4,6))                              # Рандом по ожиданию
        pyautogui.click(RND(586,1000),RND(220,300))       # Кнопка склад 
        time.sleep(RND(4,6))                              # Рандом по ожиданию
        pyautogui.click(RND(1748,1778),RND(74,100))       # Закрыть инвентарь
        time.sleep(RND(4,6))
        
        # if pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95) != None:   #Сравнивает скрин, двигаеи локал в угол
        #     left, right, top, pog = pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95)
        #     print(left,right)
        #     pyautogui.moveTo(left, right)
        #     pyautogui.dragTo(0, 1000, 2, button='left')
        break                                             # Стоп цикла




# ВХОД В ДОК
def dock():
    RND = random.randint                                  # Сокращение функции рандома
    time.sleep(1)                                         # Ждем 1 сек
    pyautogui.click(RND(66,70),RND(288,326))              # Варп
    time.sleep(RND(1,3))                                  # Рандом по ожиданию
    pyautogui.click(RND(1530,1590),RND(932,979))          # 1 ежик
    time.sleep(RND(1,2))                                  # Рандом по ожиданию
    pyautogui.click(RND(1629,1690),RND(932,979))          # 2 ежик
    time.sleep(RND(1,3))                                  # Рандом по ожиданию                 
    pyautogui.click(RND(1730,1790),RND(932,979))          # 3 ежик




# ВЫХОД КОРАБЛЯ ИЗ ДОКА
def undock():
    while pyautogui.pixel(342,465) != (26,137,25):       # Не равен зеленому
        if pyautogui.pixel(340,400) != (157,17,225):
            RND = random.randint                                  # Сокращение функции рандома
            time.sleep(0.1)
            pyautogui.moveTo(342+RND(-30, 10),465+RND(-10,30))
            pyautogui.scroll(1000)
            time.sleep(RND(2,3))                                          # Ничего не делать 
    else:                                                 # Или
        RND = random.randint                              # Сокращение функции рандома
        time.sleep(RND(1,2))                              # Рандом по ожиданию
        pyautogui.click(RND(1670,1800),RND(350,375))      # Кнопка выхода из дока (ангар)
        teleg_message("Андокаемся")
        teleg_photo()
        time.sleep(RND(15,17))                            # Рандом по ожиданию
        pyautogui.click(RND(1745,1780),RND(575,612))      # Кнопка глазика (список белтов)
        time.sleep(RND(3,4))                              # Рандом по ожиданию
        # pyautogui.click(RND(1418,1718),RND(327,400))      # Выбор белта 3 белта
        # time.sleep(1)                                     # Ждем 1 сек
        # pyautogui.click(RND(1168,1370),RND(438,514))      # Кнопка варп режима
        RND = random.randint                          # Создаем переменную для более легкой работой с рандомом

        config = configparser.ConfigParser()          # Создаём переменную парсера
        config.read("button_mapping.ini")             # Читаем конфиг
        amount_buttons = config["Main"]["amwarpbutt"] # Читаем из конфига количество кнопок на которые можно нажимать
        selected_button = RND(1, int(amount_buttons))      # Рандомизируем с какой кнопкой будем работать
        print(selected_button)
        x_m_left = int(config["Main"]["x_left"])
        x_m_right = int(config["Main"]["x_right"])
        x_s_right = int(config["Main"]["x_left2"])
        x_s_left = int(config["Main"]["x_right2"])
        y_top = int(config["Warp.button." + str(selected_button)]["y_top"])
        y_bottom = int(config["Warp.button." + str(selected_button)]["y_bottom"])
        y_top2 = int(config["Warp.button." + str(selected_button)]["y_top2"])
        y_bottom2 = int(config["Warp.button." + str(selected_button)]["y_bottom2"])

        pyautogui.click(RND(x_m_left, x_m_right), RND(y_top, y_bottom))
        time.sleep(RND(3,4))
        pyautogui.click(RND(x_s_right, x_s_left), RND(y_top2, y_bottom2))

        # if pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95) != None:
        #     left, right, top, pog = pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95)
        #     print(left,right)
        #     pyautogui.moveTo(left, right)
        #     pyautogui.dragTo(0, 1000, 2, button='left')
        time.sleep(RND(2,3))                        
        set_coords()
        time.sleep(RND(42,44))                            # Ждем пока долетит до белтов
        pyautogui.click(RND(1230,1280),RND(936,974))      # Активация копательных дронов 1 нажатие

        time.sleep(RND(1,3))                              # Ждем
        pyautogui.click(RND(1355,1380),RND(936,974))      # Активация копательных дронов 2 нажатие

        time.sleep(RND(1,3))                              # Ждем
        pyautogui.click(RND(1435,1485),RND(936,974))      # Активация копательного импланта



# ДВИГАЕМ ЛОКАЛ В УГОЛ
def move_local():                                         # Двигаем локал в угол
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
    pyautogui.click(RND(102,320),RND(426,480))            # Кнопка дока
    time.sleep(RND(1,2))                                  # Рандом по ожиданию
    pyautogui.click(RND(480, 742), RND(360, 410))         # Какая-то кнопка
    time.sleep(RND(3,4))                                  # Рандом по ожиданию
    pyautogui.click(RND(357,424), RND(363, 407))          # Какая-то кнопка



    