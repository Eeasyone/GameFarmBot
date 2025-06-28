

from threading import Thread 
import telebot
import pyautogui
import undock1
import undock2
import warp1
import warp2
import cargo
bot = telebot.TeleBot("6082492296:AAFmjDU9mnXME-LQsMU72eP8SJ0Lc_VVbZY")


#ОПОВЕЩЕНИЕ,ЧТО КОРАБЛЬ ЗАШЕЛ В ДОК
def in_dock():
    while True:
        if pyautogui.locateOnScreen("Screenshot_2.png", confidence=.95) != None:
            if warp1.go_to_dock == 1:
                bot.send_message(979854146, "Корабль зашел в док ✔️")
                warp1.go_to_dock = 0
            elif warp2.go_to_dock == 1:
                bot.send_message(979854146, "Корабль зашел в док ✔️")
                warp2.go_to_dock = 0
            else:
                pass
            
Thread(target=in_dock).start()







@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.chat.id == 979854146 or message.chat.id == 5126587781:
        if message.text == "Локал📸":
            start_btn = telebot.types.KeyboardButton("Меню⚙️")
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(start_btn)
            bot.send_photo(photo=pyautogui.screenshot(region=(35,336,350,700)), chat_id=message.chat.id, reply_markup=menu)

        elif message.text == "Меню⚙️" or message.text == "/start":
            screen_btn = telebot.types.KeyboardButton("Локал📸")
            undock1_btn = telebot.types.KeyboardButton("Андок с 🔎")
            undock2_btn = telebot.types.KeyboardButton("Андок без 🔎")
            warp1_btn = telebot.types.KeyboardButton("Варп с 🔎")                                  
            warp2_btn = telebot.types.KeyboardButton("Варп без 🔎")
            cargo_btn = telebot.types.KeyboardButton("Разгрузка📦")  
            
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(screen_btn)
            menu.row(undock1_btn, undock2_btn)
            menu.row(warp1_btn, warp2_btn)
            menu.add(cargo_btn)
            bot.send_message(message.chat.id, "Добро пожаловать в меню управления ботом. \n \nВыберите функцию которую хотите выполнить", reply_markup = menu)
        

        elif message.text == "Андок с 🔎":
            start_btn = telebot.types.KeyboardButton("Меню⚙️")
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(start_btn)
            bot.send_message(message.chat.id, "Корабль покидает станцию 🔁", reply_markup=menu)
            bot.send_photo(photo=pyautogui.screenshot(), chat_id=message.chat.id, reply_markup=menu)
            undock1.main()
            bot.send_message(message.chat.id, "Корабль приступил к добыче руды ✔️")    


        elif message.text == "Андок без 🔎":
            start_btn = telebot.types.KeyboardButton("Меню⚙️")
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(start_btn)
            bot.send_message(message.chat.id, "Корабль покидает станцию 🔁", reply_markup=menu)
            undock2.main()
            bot.send_message(message.chat.id, "Корабль приступил к добыче руды ✔️")


        elif message.text == "Варп с 🔎":
            start_btn = telebot.types.KeyboardButton("Меню⚙️")
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(start_btn)
            bot.send_message(message.chat.id, "Включена система слежения за локалом 👀", reply_markup=menu)
            warp1.main()
            bot.send_message(message.chat.id, "Корабль летит в док (враги) 🛑")
            bot.send_photo(photo=pyautogui.screenshot(), chat_id=message.chat.id, reply_markup=menu)


        elif message.text == "Варп без 🔎":
            start_btn = telebot.types.KeyboardButton("Меню⚙️")
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(start_btn)
            bot.send_message(message.chat.id, "Варпаем в док 🔁", reply_markup=menu)
            warp2.main()


        elif message.text == "Разгрузка📦":
            start_btn = telebot.types.KeyboardButton("Меню⚙️")
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(start_btn)
            bot.send_message(message.chat.id, "Разгрузка корабля 🔁", reply_markup=menu)
            cargo.main()
            bot.send_message(message.chat.id, "Корабль разгружен ✔️") 


        else:
            start_btn = telebot.types.KeyboardButton("Меню⚙️")
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(start_btn)
            bot.send_message(message.chat.id, "Команда не распознана. \n \nНажмите на кнопку Меню⚙️ чтобы увидеть все существующие функции.", reply_markup=menu)
bot.infinity_polling()

