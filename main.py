from threading import Thread
from time import sleep

from telebot import TeleBot
from telebot.apihelper import ApiTelegramException
from telebot.types import Message

from config import TOKEN
from db_utils import insert_or_ignore_user, insert_currency, get_last_currency, get_all_subscribers, delete_user
from parsing import aloqabank

bot = TeleBot(TOKEN)


def trigger_update():
    while True:
        if current := aloqabank():
            history_from_db = get_last_currency()
            if current != history_from_db:
                insert_currency(*current)
                users = get_all_subscribers()
                for user, *_ in users:
                    try:
                        bot.send_message(user,
                                         f'🔥 Курс ЦБ: {current[-1]} '
                                         f'\nAloqabank Покупка:  {current[0]} сум '
                                         f'\nAloqabank Продажа:  {current[1]} сум')
                    except ApiTelegramException:
                        delete_user(user)

        sleep(60 * 1)


thread = Thread(target=trigger_update)
thread.start()


@bot.message_handler(commands=['start', 'help', 'about'])
def command_start(message: Message):
    chat_id = message.from_user.id
    if message.text == '/start':
        if insert_or_ignore_user(chat_id):
            bot.send_message(chat_id,
                             "Добро пожаловать в бот, при изменении курса доллара в банке Aloqabank, "
                             "бот сам будет присылать обновление")
        else:
            bot.send_message(chat_id, 'Актуальный курс')
            send_currency(chat_id)

    elif message.text == '/help':
        bot.send_message(chat_id, "Отработала команда help")
    elif message.text == '/about':
        bot.send_message(chat_id, "Отработала команда about")


def send_currency(chat_id):
    """Отправка курса по команде старт"""
    if result := aloqabank():
        bot.send_message(chat_id, f'Курс ЦБ: {result[-1]} '
                                  f'\nAloqabank Покупка:  {result[0]} сум '
                                  f'\nAloqabank Продажа:  {result[1]} сум"')
        insert_currency(*result)


bot.polling(non_stop=True)