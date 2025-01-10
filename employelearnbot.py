import requests, random
# from bs4 import BeautifulSoup
from telebot import *

token = '7398398254:AAFa27_AjW45tXGjZbXSlMou8YH0cnsAx8I'
bot = telebot.TeleBot(token)

# Сообщение
@bot.message_handler(commands=['start'])
def welcome_message(message):
    print(message.from_user.first_name)
    print(message.chat.id)
    welcome_message = f'Здравствуйте, {message.from_user.first_name}! Приветствуем вас на платформе для обучения сотрудников в сфере онлайн-продаж'
    start_button_keyboard = types.InlineKeyboardMarkup()
    start_button = types.InlineKeyboardButton('Начать', callback_data='start')
    start_button_keyboard.add(start_button)
    bot.send_message(message.chat.id, welcome_message, reply_markup=start_button_keyboard)

# @bot.message_handler(content_types='text')
# def registration(message):
#     bot.send_message(message.chat.id, f'You wrote {message.text}')

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    option = call.data
    umessage = call.message
    match option:
        case 'start':
            bot.send_message(umessage.chat.id, text='Введите своё имя и фамилию')

            @bot.message_handler(content_types='text')
            def registration(message):
                user = message.text
                bot.send_message(message.chat.id, user)
                print(user)
                return user

            bot.register_message_handler(umessage, registration(umessage))


        case 'main':
            choose_topic = types.InlineKeyboardMarkup()
            account_b = types.InlineKeyboardButton("Аккаунт", callback_data='account')
            theme_b = types.InlineKeyboardButton("Выбор темы", callback_data='course')
            progress_b = types.InlineKeyboardButton("Прогресс", callback_data='progress')
            choose_topic.row_width = 1
            choose_topic.add(account_b, theme_b, progress_b)
            bot.send_message(umessage.chat.id, text='Курс "Эффективные продажи в онлайн-магазине"',
                             reply_markup=choose_topic)
        case 'account':
            account_message = (f'*** Ваше имя и фамилия *** \n'
                               f'\n'
                               f'Курсы:\n'
                               f'"Эффективные продажи в онлайн-магазине"')
            account_keyboard = types.InlineKeyboardMarkup()
            account_button = types.InlineKeyboardButton('Назад', callback_data='main')
            account_keyboard.add(account_button)
            bot.send_message(umessage.chat.id, account_message, reply_markup=account_keyboard)
        case 'course':
            themes_list = types.InlineKeyboardMarkup()
            themes_list.row_width = 1
            theme1 = types.InlineKeyboardButton('1 | Введение в онлайн-продажи', callback_data='theme1')
            theme2 = types.InlineKeyboardButton('2 | Работа с клиентами', callback_data='theme2')
            theme3 = types.InlineKeyboardButton('3 | Презентация товара и работа с возражениями', callback_data='theme3')
            theme4 = types.InlineKeyboardButton('4 | Завершение сделки и постпродажное обслуживание', callback_data='theme4')
            goback = types.InlineKeyboardButton('Выйти', callback_data='main')
            themes_list.add(theme1, theme2, theme3, theme4, goback)
            bot.send_message(umessage.chat.id, 'Выберите тему:', reply_markup=themes_list)

        case 'progress':
            completed_lessons = 2
            persents = round(completed_lessons/12, 2)*100
            progress_message = (f'Ваш прогресс\n'
                               f'\n'
                               f'Курсы:\n'
                               f'"Эффективные продажи в онлайн-магазине"\n'
                                f'{completed_lessons}/12 ({persents}%)')
            progress_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Назад', callback_data='main')
            progress_keyboard.add(goback)
            bot.send_message(umessage.chat.id, progress_message, reply_markup=progress_keyboard)


# Кнопка
@bot.message_handler(commands=['button'])
def button_message(message):
    choose_topic = types.InlineKeyboardMarkup()
    account_b = types.InlineKeyboardButton("Аккаунт", callback_data='account')
    theme_b = types.InlineKeyboardButton("Выбор темы", callback_data='course')
    progress_b = types.InlineKeyboardButton("Прогресс", callback_data='progress')
    choose_topic.row_width = 1
    choose_topic.add(account_b, theme_b, progress_b)
    bot.send_message(message.chat.id, text='Курс "Эффективные продажи в онлайн-магазине"', reply_markup=choose_topic)

@bot.inline_handler(lambda query: query.query == 'Аккаунт')
def query_text(inline_query):
    welcome_message()

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