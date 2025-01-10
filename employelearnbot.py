import requests, random
# from bs4 import BeautifulSoup
from telebot import *

token = '7398398254:AAFa27_AjW45tXGjZbXSlMou8YH0cnsAx8I'
bot = telebot.TeleBot(token)

# Сообщение
@bot.message_handler(commands=['start'])
def send_welcome_message(message):
    print(message.from_user.first_name)
    print(message.chat.id)
    welcome_message = f'Здравствуйте, {message.from_user.first_name}! Приветствуем вас на платформе обучения сотрудников в сфере онлайн-продаж!'
    bot.send_message(message.chat.id, welcome_message)

# Кнопка
@bot.message_handler(commands=['button'])
def button_message(message):
    choose_topic = types.InlineKeyboardMarkup()
    account_b = types.InlineKeyboardButton("Аккаунт", callback_data='account')
    theme_b = types.InlineKeyboardButton("Выбор темы", callback_data='course')
    progress_b = types.InlineKeyboardButton("Прогресс", callback_data='progress')
    choose_topic.add(account_b, theme_b, progress_b)
    bot.send_message(message.chat.id, text='Курс "Эффективные продажи в онлайн-магазине"', reply_markup=choose_topic)

# @bot.message_handler(commands=['pc_action'])
# def pc_action(message):
#     response = requests.get('https://www.igromania.ru/games/pc/action/')
#     html = BeautifulSoup(response.content, 'lxml')
#     pca = random.choice(html.find_all(class_='game-card'))
#     bot.send_message(message.chat.id, pca.find(class_='name').text)


# Завершение работы
@bot.message_handler(commands=['end'])
def send_welcome_message(message):
    print(message.from_user.first_name)
    print(message.chat.id)
    bb_message = f'Пока, {message.from_user.first_name}, возвращайся ещё!'
    bot.send_message(message.chat.id, bb_message)


bot.polling()