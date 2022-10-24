# bot link: @t.me/blJk21_bot

import telebot
import Menu

bot = telebot.TeleBot("5606174334:AAGX9AfjeHzQmkGLmx-vUIkqAsYsSH16KrI")


# Действие на команду старт
@bot.message_handler(commands=['start'])
def start(message):
    bot_message = f'Приветствую тебя {message.from_user.first_name}!'
    Menu.main_menu(bot, message,  bot_message)

# Действия на нажате кнопок меню
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '♠️Играть в 21 ♥️':
            Menu.play_bljk_btn_event(bot, message)
        elif message.text == '💰Мои финансы':
            Menu.finance_btn_event(bot, message)
        elif message.text == '📄Информация':
            Menu.information_btn_event(bot, message)
        elif message.text == '🤝Партнёры':
            Menu.partners_btn_event(bot, message)
        elif message.text == '📈Рейтинг':
            Menu.rating_btn_event(bot, message)
        elif message.text == '📊Статистика':
            Menu.statistics_btn_event(bot, message)
        elif message.text == 'Для инвесторов':
            Menu.for_investors_btn_event(bot, message)
        elif message.text == 'Вернуться назад':
            Menu.back_menu_btn_event(bot, message)

    else:
        bot.send_message(message.chat.id, 'Такого действия не существует!!!')


bot.infinity_polling()

# я Подключился
# бот хуёт
