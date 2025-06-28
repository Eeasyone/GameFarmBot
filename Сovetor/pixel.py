


# -------------------------------------------------- КООРДИНАТЫ И ЦВЕТ ------------------------------------------
import pyautogui
while True:
    currentMouseX, currentMouseY = pyautogui.position()
    a = pyautogui.pixel(currentMouseX, currentMouseY)
    print("Position: " + "x: " + str(currentMouseX) + " y: " + str(currentMouseY) + " Color: " + str(a), end='\r')