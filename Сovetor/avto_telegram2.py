 
from loguru import logger
from datetime import datetime
import os
import keyboard
import pyautogui                                      # Библиотека для работы с устройствами ввода и экраном
import random                                         # Библиотека рандома
import time                                           # Библиотека для работы с временем 
from threading import Thread, Timer                   # Врубаем мультипоточность
import functions                                      # Импорт из главной папки всех отдельных функций
RND = random.randint                                  # Сокращение рандома
dock = 0                                              # В доке или нет (0 - не в доке, 1 - в доке)
stop_timer = 0

currentDateAndTime = datetime.now()
time1 = currentDateAndTime.strftime("%Y.%m.%d_%H-%M")

logger.add("logs\\log_{}.log".format(time1), format="[{level}] [{time:HH:mm:ss}] [{thread.name}] - {message}")
logger.info("СКРИПТ ЗАПУЩЕН!")

@logger.catch
def warp1():                                          # 1 ПОТОК ОТВЕЧАЕТ ЗА ЛОКАЛ
    while pyautogui.pixel(342,465) == (26,137,25):    # равен ЗЕЛЕНОМУ
        if pyautogui.pixel(342,400) != (157,17,225):
            logger.warning("Не могу найти фиолетовый! Пролистываю.....")
            time.sleep(0.1)
            pyautogui.moveTo(342+RND(-30, 10),465+RND(-10,30))
            pyautogui.scroll(1000)
            time.sleep(RND(2,3))
            # Thread(target=1warp1).start()              # ничего не делать
    else:                                             # или
        global dock                                   # использование глобальной переменной dock
        if dock == 1:                                 # Если в доке, ничего не делаем
            Thread(target=warp1).start()              # ничего не делать
        else:                                         # Или
            logger.warning("Зеленый не найден! Перепроверяю........")
            time.sleep(0.1)
            pyautogui.moveTo(341+RND(-30, 10),465+RND(-10,30))
            pyautogui.scroll(1000)
            time.sleep(1)
            if pyautogui.pixel(341,465) == (26,137,25):
                Thread(target=warp1).start()
            else:
                global cargo
                logger.info("Перепроверка неуспешна! Выключаю таймер и выставляю статус dock = 1")
                dock = 1                                  # Выставляем статус в доке
                cargo.cancel()
                functions.teleg_message("Варп в док")
                functions.teleg_photo()
                logger.info("Запускаем функцию варпа!")
                functions.dock()                          # Док в станцию
                time.sleep(RND(62,65))                    # Ждем от 80 до 85 секунд
                logger.info("Запускаем функцию разгрузки карго!")
                functions.teleg_message("Разгружаем корабль")
                functions.teleg_photo()
                functions.cargo()                         # Разгружаем корабль
                time.sleep(RND(5,7))
                logger.info("Запускаем функцию андока!")
                
                functions.undock()                        # Андокаемся
                logger.info("Выставляем dock = 0")
                dock = 0                                  # Корабль не в доке
                logger.info("Запускаем поток заново!")
                Thread(target=warp1).start()              # Запуск многопоточности
                logger.info("Запускаем поток карго по таймеру!")
                cargo = Timer(RND(700,720), warp3)
                cargo.start()



# def warp2():                                          # 2 ПОТОК ОТВЕЧАЕТ ЗА КАРГО
#     while pyautogui.pixel(84,168) != (67,109,112):    # не равен ЗЕЛЕНОМУ
#         pass                                          # ничего не делать
#     else:                                             # или
#         global dock                                   # использование глобальной переменной dock
#         if dock == 1:                                 # Если в доке, ничего не делаем
#             pass                                      # ничего не делать
#         else:                                         # Или
#             logger.info("Выставляем dock = 1")
#             dock = 1                                  # Выставляем статус в доке
#             functions.teleg_message("Варп в док")
#             functions.teleg_photo()
#             functions.dock()                          # Док в станцию
#             time.sleep(RND(62,65))                    # Ждем от 40 до 47 секунд
#             functions.teleg_message("Разгружаем корабль")
#             functions.teleg_photo()
#             functions.cargo()                         # Разгружаем корабль
#             time.sleep(RND(5,7))
#             logger.info("Запускаем функцию андока!")
#             functions.undock()                        # Андокаемся
#             logger.info("Выставляем dock = 0")
#             dock = 0                                  # Корабль не в доке
#             Thread(target=warp2).start()              # Запуск многопоточности
@logger.catch
def warp3():
    # time.sleep(RND(12,13) * 60)
    global dock 
    if dock == 1:                                 # Если в доке, ничего не делаем
        pass
    else:
        logger.info("Таймер по заполнению карго прошел")
        global cargo
        dock = 1                                  # Выставляем статус в доке
        functions.teleg_message("Варп в док")
        functions.teleg_photo()
        logger.info("Запускаем функцию варпа!")
        functions.dock()                          # Док в станцию
        time.sleep(RND(62,65))                    # Ждем от 40 до 47 секунд
        functions.teleg_message("Разгружаем корабль")
        functions.teleg_photo()
        logger.info("Запускаем функцию разгрузки карго!")
        functions.cargo()                         # Разгружаем корабль
        time.sleep(RND(5,7))
        logger.info("Запускаем функцию андока!")
        functions.undock()                        # Андокаемся
        logger.info("Выставляем dock = 0")
        dock = 0                                  # Корабль не в доке
        logger.info("Запускаем поток карго по таймеру!")
        cargo = Timer(RND(700,720), warp3)
        cargo.start()
@logger.catch
def exit():
    while True:
        if keyboard.is_pressed("*"):
            print("Force exit!!!!")
            os._exit(1)

Thread(target=warp1).start()
# Thread(target=warp2).start()
cargo = Timer(RND(700,720), warp3)
cargo.start()
# Thread(target=warp3).start()
Thread(target=exit).start()
print(Thread(target=warp1).is_alive())



