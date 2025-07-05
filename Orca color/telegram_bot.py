from threading import Thread 
import telebot
import pyautogui
import undock_red
import undock_nocheck
import warp_red
import warp_nocheck
import cargo
bot = telebot.TeleBot("6082492296:AAFmjDU9mnXME-LQsMU72eP8SJ0Lc_VVbZY")


# Оповещение, что корабль вошел в док
def in_dock():
    while True:
        if pyautogui.locateOnScreen("Screenshot_2.png", confidence=.95) != None:
            if warp_red.go_to_dock == 1:
                bot.send_message(979854146, "Корабль зашел в док ✔️")
                warp_red.go_to_dock = 0
            elif warp_nocheck.go_to_dock == 1:
                bot.send_message(979854146, "Корабль зашел в док ✔️")
                warp_nocheck.go_to_dock = 0
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
            undock_red_btn = telebot.types.KeyboardButton("Андок с 🔎")
            undock_nocheck_btn = telebot.types.KeyboardButton("Андок без 🔎")
            warp_red_btn = telebot.types.KeyboardButton("Варп с 🔎")                                  
            warp_nocheck_btn = telebot.types.KeyboardButton("Варп без 🔎")
            cargo_btn = telebot.types.KeyboardButton("Разгрузка📦")  
            
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(screen_btn)
            menu.row(undock_red_btn, undock_nocheck_btn)
            menu.row(warp_red_btn, warp_nocheck_btn)
            menu.add(cargo_btn)
            bot.send_message(message.chat.id, "Добро пожаловать в меню управления ботом. \n \nВыберите функцию которую хотите выполнить", reply_markup = menu)
        
        elif message.text == "Андок с 🔎":
            start_btn = telebot.types.KeyboardButton("Меню⚙️")
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(start_btn)
            bot.send_message(message.chat.id, "Корабль покидает станцию 🔁", reply_markup=menu)
            bot.send_photo(photo=pyautogui.screenshot(), chat_id=message.chat.id, reply_markup=menu)
            undock_red.main()
            bot.send_message(message.chat.id, "Корабль приступил к добыче руды ✔️")    

        elif message.text == "Андок без 🔎":
            start_btn = telebot.types.KeyboardButton("Меню⚙️")
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(start_btn)
            bot.send_message(message.chat.id, "Корабль покидает станцию 🔁", reply_markup=menu)
            undock_nocheck.main()
            bot.send_message(message.chat.id, "Корабль приступил к добыче руды ✔️")

        elif message.text == "Варп с 🔎":
            start_btn = telebot.types.KeyboardButton("Меню⚙️")
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(start_btn)
            bot.send_message(message.chat.id, "Включена система слежения за локалом 👀", reply_markup=menu)
            warp_red.main()
            bot.send_message(message.chat.id, "Корабль летит в док (враги) 🛑")
            bot.send_photo(photo=pyautogui.screenshot(), chat_id=message.chat.id, reply_markup=menu)

        elif message.text == "Варп без 🔎":
            start_btn = telebot.types.KeyboardButton("Меню⚙️")
            menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            menu.add(start_btn)
            bot.send_message(message.chat.id, "Варпаем в док 🔁", reply_markup=menu)
            warp_nocheck.main()

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

