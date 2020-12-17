import telebot
from telebot import types
bot = telebot.TeleBot('1466063796:AAFbZhgHkj0rLqhFqWSuzi5hQrjTDmhxjVU')

chat_id = ''

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "Итак, чем могу быть тебе полезен?")
    global chat_id
    chat_id = message.from_user.id
    bot.register_next_step_handler(message, main_menu())


def main_menu():
    keyboard = types.InlineKeyboardMarkup()  # наша клавиатура
    key_PAV = types.InlineKeyboardButton(text='Узнать про ПАВы',
                                         url="https://ru.wikipedia.org/wiki/%D0%9F%D0%BE%D0%B2%D0%B5%D1%80%D1%85%D0%BD%D0%BE%D1%81%D1%82%D0%BD%D0%BE-%D0%B0%D0%BA%D1%82%D0%B8%D0%B2%D0%BD%D1%8B%D0%B5_%D0%B2%D0%B5%D1%89%D0%B5%D1%81%D1%82%D0%B2%D0%B0")
    keyboard.add(key_PAV)
    key_Hangover = types.InlineKeyboardButton(text='Передозировка', callback_data='hangover')
    keyboard.add(key_Hangover)
    key_kapel = types.InlineKeyboardButton(text='Капельница',
                                           url='https://www.polismed.com/articles-narkolog.html')
    keyboard.add(key_kapel)
    key_reability = types.InlineKeyboardButton(text='Реабилитация',
                                               url='https://ктотут.рф/')
    keyboard.add(key_reability)
    bot.send_message(chat_id, text='Меню:', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "hangover":
        keyboard = types.InlineKeyboardMarkup()
        hangover = types.InlineKeyboardButton(text='Симптомы', url='https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%D0%BE%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0')
        medic = types.InlineKeyboardButton(text='Врач', url='https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%D0%BE%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0')
        rules = types.InlineKeyboardButton(text='Как себя вести?', url='https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%80%D0%B5%D0%B4%D0%BE%D0%B7%D0%B8%D1%80%D0%BE%D0%B2%D0%BA%D0%B0')
        main = types.InlineKeyboardButton(text='Главное меню', callback_data='main')
        keyboard.add(hangover)
        keyboard.add(medic)
        keyboard.add(rules)
        keyboard.add(main)
        bot.send_message(call.message.chat.id, text='Если вы наблюдаете у себя или у другого человека, употреблявшего ПАВы, данные симптомы, необходимо срочное оказание медицинской помощи. Помните, речь идет о жизни!', reply_markup=keyboard)
    elif call.data == "main":
        bot.answer_callback_query(call.id, main_menu())

bot.polling(none_stop=True, interval=0)


#bot.send_message(message.chat.id, '[StackOverflow на русском](https://ru.stackoverflow.com/)', parse_mode='Markdown')
