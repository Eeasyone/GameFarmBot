import cv2                                                               # Импорт библиотеки компьютерного зрения
import pytesseract                                                       # Добавление библиотеки ИИ чтения текста
from PIL import ImageGrab, Image                                         # Для работы со скриншотами
pytesseract.pytesseract.tesseract_cmd = r'D:\Tesseract\tesseract'        # Путь к файлу запуска ИИ



#КРАСНЫЙ МИНУС
image  = ImageGrab.grab(bbox=(197,986,220,1016))                 # Выбор области экрана  (x, y, x2, y2) [197,986,220,1016 - минус] [314,987,338,1016 - серый]
image.save(fp="loc1.png")                                       # Сохраняем скриншот в файл
img = cv2.imread('loc1.png')                                    # Читаем созданный до этого скриншоти ка
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                     # Повышаем точность распознавания
custom_config = r'--oem 3 --psm 13'                              # Повышаем точность распознавания
text = pytesseract.image_to_string(gray, config=custom_config)   # Кастом конфиг
print(text)                                                      # Печать полученного текста в консоль


#СЕРЫЙ НЕЙТРАЛ
image1  = ImageGrab.grab(bbox=(314,987,338,1016))                # Выбор области экрана  (x, y, x2, y2) [197,986,220,1016 - минус] [314,987,338,1016 - серый]
image1.save(fp="loc2.png")                                      # Сохраняем скриншот в файл
img = Image.open('loc2.png')
thresh = 60
fn = lambda x : 255 if x > thresh else 0
r = img.convert('L').point(fn, mode='1')
r.save('loc2.png')
text1 = pytesseract.image_to_string(r, config=custom_config)     # Кастом конфиг
print(text1)                                                     # Печать полученного текста в консоль

if text1 != int:
    text1 = 0

index = int(text)  
index1 = int(text1)
if index >= 2 or index1 >= 2:                                     
    print("Враги или нейтралы в локале!")
else: 
    print("Врагов или нейтралов не видно!")














# ПО LD ПЛЕЕРУ:
# локал в нижнем левом углу экрана
# разрешение экрана - 100%
# размер элементов управления - 110%



