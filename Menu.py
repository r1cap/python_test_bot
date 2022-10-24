from telebot import types

BALANCE = 100


def main_menu(bot, message, bot_message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    play_btn = types.KeyboardButton('♠️Играть в 21 ♥️')
    finance_btn = types.KeyboardButton('💰Мои финансы')
    inform_btn = types.KeyboardButton('📄Информация')
    partners_btn = types.KeyboardButton('🤝Партнёры')
    rating_btn = types.KeyboardButton('📈Рейтинг')
    statistics_btn = types.KeyboardButton('📊Статистика')
    for_investors_btn = types.KeyboardButton('Для инвесторов')

    markup.add(play_btn, finance_btn, inform_btn, partners_btn, rating_btn, statistics_btn, for_investors_btn)

    bot.send_message(message.chat.id, bot_message, reply_markup=markup)


def play_bljk_btn_event(bot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    play_with_bot_btn = types.KeyboardButton('Играть с ботом')
    online_game_btn = types.KeyboardButton('Онлайн игра')
    back_btn = types.KeyboardButton('Вернуться назад')

    markup.add(play_with_bot_btn, online_game_btn, back_btn)

    bot.send_message(message.chat.id, f'♠️Играть в 21 ♥️', reply_markup=markup)


def finance_btn_event(bot, message):
    bot.send_message(message.chat.id, f"Баланс: {BALANCE} ")


def partners_btn_event(bot, message):
    pass


def rating_btn_event(bot, message):
    pass


def statistics_btn_event(bot, message):
    pass


def for_investors_btn_event(bot, message):
    pass


def information_btn_event(bot, message):
    pass


def back_menu_btn_event(bot, message):
    bot_message = 'Вернуться назад!'
    main_menu(bot, message, bot_message)
