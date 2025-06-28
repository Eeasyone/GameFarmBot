# --------------------------- ВАРП С ПРОВЕРКОЙ НА НЕЙТРАЛА ИЛИ КРАСНОГО ----------------------------------------------

from pyautogui import locateOnScreen, moveTo, scroll, click     # Библиотека для работы с устройствами ввода и экраном
import random                                                   # Библиотека рандома
import time                                                     # Библиотека для работы с временем 
RND = random.randint                                            # Сокращение рандома
go_to_dock = 0



#ПРОВЕРКА ПО ЦВЕТУ
def main():
    while locateOnScreen("Screenshot_2.jpg", confidence=.85) == None and locateOnScreen("Screenshot_3.jpg", confidence=.85) == None:                                                                                                 # ожидание 2 секунды
        pass
    else:                                                                                         # Или
        one, two, three, four = locateOnScreen("Screenshot_4.jpg", confidence=.85)                # Ищем шестеренку для нахождения локала
        time.sleep(0.1)                                                                           # Ждем 0.1 секунду
        moveTo(RND(three, three+four),one+three+RND(20, 40))                                      # Двигаем мышку ниже шестеренки
        scroll(1000)                                                                              # Листаем
        time.sleep(1)                                                                             # Ждем секунду чтобы анимация листания прошла             
        if locateOnScreen("Screenshot_2.jpg", confidence=.85) == None and locateOnScreen("Screenshot_3.jpg", confidence=.85) == None: # После скролла проверяем нет ли нейтрала или врага
            main()                                                                                # Если врага или нейтрала нет то запускаем функцию заново
        else:                                                                                     # Запускается если все же нейтрал или враг есть                                                                                              
            time.sleep(RND(1,4))                                                                  # Рандом по ожиданию
            click(RND(1530,1590),RND(932,979))                                                    # 1 ежик
            time.sleep(RND(1,2))                                                                  # Рандом по ожиданию
            click(RND(1629,1690),RND(932,979))                                                    # 2 ежик
            time.sleep(RND(1,2))                                                                  # Рандом по ожиданию
            click(RND(1730,1790),RND(932,979))                                                    # 3 ежик
            time.sleep(1)                                                                         # Ждем 1 сек
            click(RND(66,98),RND(288,326))                                                        # Варп в док

main()                                                                                            # Запускаем главную функцию