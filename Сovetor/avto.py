

import pyautogui                                      # Библиотека для работы с устройствами ввода и экраном
import random                                         # Библиотека рандома
import time                                           # Библиотека для работы с временем 
from threading import Thread                          # Врубаем мультипоточность
import functions                                      # Импорт из главной папки всех отдельных функций
RND = random.randint                                  # Сокращение рандома
dock = 0                                              # В доке или нет (0 - не в доке, 1 - в доке)



def warp_red():                                          # 1 ПОТОК ОТВЕЧАЕТ ЗА ЛОКАЛ
    while pyautogui.pixel(343,614) == (26,137,25):    # равен ЗЕЛЕНОМУ
        pass                                          # ничего не делать
    else:                                             # или
        global dock                                   # использование глобальной переменной dock
        if dock == 1:                                 # Если в доке, ничего не делаем
            Thread(target=warp_red).start()              # ничего не делать
        else:                                         # Или
            time.sleep(0.1)
            pyautogui.moveTo(343+RND(-30, 10),614+RND(-10,30))
            pyautogui.scroll(1000)
            time.sleep(1)
            if pyautogui.pixel(343,614) == (26,137,25):
                Thread(target=warp_red).start()
            else:
                dock = 1                                  # Выставляем статус в доке
                functions.dock()                          # Док в станцию
                time.sleep(RND(80,85))                    # Ждем от 80 до 85 секунд
                functions.cargo()                         # Разгружаем корабль
                functions.undock()                        # Андокаемся
                dock = 0                                  # Корабль не в доке
                Thread(target=warp_red).start()              # Запуск многопоточности



def warp_nocheck():                                          # 2 ПОТОК ОТВЕЧАЕТ ЗА КАРГО
    while pyautogui.pixel(88,168) != (66,108,111):    # не равен ЗЕЛЕНОМУ
        pass                                          # ничего не делать
    else:                                             # или
        global dock                                   # использование глобальной переменной dock
        if dock == 1:                                 # Если в доке, ничего не делаем
            pass                                      # ничего не делать
        else:                                         # Или
            dock = 1                                  # Выставляем статус в доке
            functions.dock()                          # Док в станцию
            time.sleep(RND(80,85))                    # Ждем от 80 до 85 секунд
            functions.cargo()                         # Разгружаем корабль
            functions.undock()                        # Андокаемся
            dock = 0                                  # Корабль не в доке
            Thread(target=warp_nocheck).start()              # Запуск многопоточности


Thread(target=warp_red).start()
Thread(target=warp_nocheck).start()
print(Thread(target=warp_red).is_alive())



