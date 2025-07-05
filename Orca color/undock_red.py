import pyautogui
import random
import time
import configparser

RND = random.randint

# Перетягивание локала в угол 
def main():
    if pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95) is not None:
        left, right, top, pog = pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95)
        print(left, right)
        pyautogui.moveTo(left, right)
        pyautogui.dragTo(0, 1000, 1, button='left')

    # Проверка по цвету    
    while pyautogui.pixel(360, 611) != (26, 137, 25):
        pass
    else:
        time.sleep(RND(1, 2))
        pyautogui.click(RND(1670, 1800), RND(350, 375))
        time.sleep(RND(12, 15))
        pyautogui.click(RND(1745, 1780), RND(575, 612))
        time.sleep(RND(1, 2))

        # Переменная парсера        
        config = configparser.ConfigParser()
        config.read("button_mapping.ini")
        amount_buttons = config["Main"]["amwarpbutt"]
        selected_button = RND(1, int(amount_buttons))
        print(selected_button)
        x_m_left = int(config["Main"]["x_left"])
        x_m_right = int(config["Main"]["x_right"])
        x_s_right = int(config["Main"]["x_left2"])
        x_s_left = int(config["Main"]["x_right2"])
        y_top = int(config["Warp.button." + str(selected_button)]["y_top"])
        y_bottom = int(config["Warp.button." + str(selected_button)]["y_bottom"])
        y_top2 = int(config["Warp.button." + str(selected_button)]["y_top2"])
        y_bottom2 = int(config["Warp.button." + str(selected_button)]["y_bottom2"])

        # Прожатие кнопки варп режима
        pyautogui.click(RND(x_m_left, x_m_right), RND(y_top, y_bottom))
        time.sleep(RND(2, 3))
        pyautogui.click(RND(x_s_right, x_s_left), RND(y_top2, y_bottom2))
        time.sleep(1)
        pyautogui.click(RND(1168, 1370), RND(438, 514))

        # Перетягивание локала в угол 
        if pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95) is not None:
            left, right, top, pog = pyautogui.locateOnScreen("Screenshot_1.png", confidence=.95)
            print(left, right)
            pyautogui.moveTo(left, right)
            pyautogui.dragTo(0, 1000, 5, button='left')

        # Настройка навигатора (создание точки варпа)
        pyautogui.click(RND(67, 104), RND(289, 321))
        time.sleep(RND(1, 2))
        pyautogui.click(RND(77, 343), RND(430, 482))
        time.sleep(RND(1, 2))
        pyautogui.click(RND(462, 750), RND(362, 410))
        time.sleep(RND(1, 2))
        pyautogui.click(RND(355, 426), RND(357, 401))

        # Активация добывающих дронов и импланта
        time.s
