# import requests, random
# from bs4 import BeautifulSoup
from telebot import *

token = '7398398254:AAFa27_AjW45tXGjZbXSlMou8YH0cnsAx8I'
bot = telebot.TeleBot(token)
user_data = {}
progress_data = {}


# Сообщение
@bot.message_handler(commands=['start'])
def welcome_message(message):
    print(message.from_user.first_name)
    print(message.chat.id)
    welcome_message = (f'Здравствуйте, {message.from_user.first_name}! \n'
                       f'Приветствуем вас на платформе для обучения сотрудников в сфере онлайн-продаж')
    start_button_keyboard = types.InlineKeyboardMarkup()
    start_button = types.InlineKeyboardButton('Начать', callback_data='start')
    start_button_keyboard.add(start_button)
    bot.send_message(message.chat.id, welcome_message, reply_markup=start_button_keyboard)

def registration(message):
    user_id = message.chat.id
    user_name = message.text
    user_data[user_id] = user_name
    progress_data[user_id] = 0
    continue_keyboard = types.InlineKeyboardMarkup()
    continue_button = types.InlineKeyboardButton('Продолжить', callback_data='main')
    continue_keyboard.add(continue_button)
    bot.send_message(message.chat.id, f'Приятно познакомиться, {user_name}!', reply_markup=continue_keyboard)
    print(user_data)

def progress_plus(message):
    user_id = message.chat.id
    progress_data[user_id] = progress_data[user_id] + 1

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    option = call.data
    umessage = call.message
    match option:
        case 'start':
            bot.send_message(umessage.chat.id, text='Введите своё имя и фамилию')
            bot.register_next_step_handler(umessage, registration)

        case 'main':
            choose_topic = types.InlineKeyboardMarkup()
            account_b = types.InlineKeyboardButton("Аккаунт", callback_data='account')
            theme_b = types.InlineKeyboardButton("Выбор темы", callback_data='course')
            progress_b = types.InlineKeyboardButton("Прогресс", callback_data='progress')
            choose_topic.row_width = 1
            choose_topic.add(account_b, theme_b, progress_b)
            message_id = bot.send_message(umessage.chat.id, 'Курс "Эффективные продажи в онлайн-магазине"', reply_markup=choose_topic).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'account':
            chatid = umessage.chat.id
            username = user_data[chatid]
            account_message = (f'{username} \n'
                               f'\n'
                               f'Курсы:\n'
                               f'"Эффективные продажи в онлайн-магазине"')
            account_keyboard = types.InlineKeyboardMarkup()
            account_button = types.InlineKeyboardButton('Назад', callback_data='main')
            account_keyboard.add(account_button)
            message_id = bot.send_message(umessage.chat.id, account_message, reply_markup=account_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'course':
            themes_list = types.InlineKeyboardMarkup()
            themes_list.row_width = 1
            theme1 = types.InlineKeyboardButton('1 | Введение в онлайн-продажи', callback_data='theme1')
            theme2 = types.InlineKeyboardButton('2 | Работа с клиентами', callback_data='theme2')
            theme3 = types.InlineKeyboardButton('3 | Презентация товара и работа с возражениями', callback_data='theme3')
            theme4 = types.InlineKeyboardButton('4 | Завершение сделки и постпродажное обслуживание', callback_data='theme4')
            goback = types.InlineKeyboardButton('Выйти', callback_data='main')
            themes_list.add(theme1, theme2, theme3, theme4, goback)
            message_id = bot.send_message(umessage.chat.id, 'Выберите тему:', reply_markup=themes_list).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id-1)

        case 'theme1':
            themes_list = types.InlineKeyboardMarkup()
            themes_list.row_width = 1
            theme_a = types.InlineKeyboardButton('Особенности онлайн-продаж и их отличие от офлайн-продаж', callback_data='theme1a')
            theme_b = types.InlineKeyboardButton('Основные понятия: конверсия, средний чек, лиды', callback_data='theme1b')
            theme_c = types.InlineKeyboardButton('Роль менеджера по продажам в онлайн-магазине', callback_data='theme1c')
            goback = types.InlineKeyboardButton('Назад', callback_data='course')
            themes_list.add(theme_a, theme_b, theme_c, goback)
            message_id = bot.send_message(umessage.chat.id, 'Выберите урок:', reply_markup=themes_list).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme2':
            themes_list = types.InlineKeyboardMarkup()
            themes_list.row_width = 1
            theme_a = types.InlineKeyboardButton('Техники установления контакта с клиентом в чате', callback_data='theme2a')
            theme_b = types.InlineKeyboardButton('Выявление потребностей и мотивации покупателя', callback_data='theme2b')
            theme_c = types.InlineKeyboardButton('Активное слушание и умение задавать вопросы.', callback_data='theme2c')
            goback = types.InlineKeyboardButton('Назад', callback_data='course')
            themes_list.add(theme_a, theme_b, theme_c, goback)
            message_id = bot.send_message(umessage.chat.id, 'Выберите урок:', reply_markup=themes_list).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme3':
            themes_list = types.InlineKeyboardMarkup()
            themes_list.row_width = 1
            theme_a = types.InlineKeyboardButton('Как эффективно презентовать товар онлайн', callback_data='theme3a')
            theme_b = types.InlineKeyboardButton('Описание преимуществ и выгод для клиента', callback_data='theme3b')
            theme_c = types.InlineKeyboardButton('Работа с распространенными возражениями клиентов', callback_data='theme3c')
            goback = types.InlineKeyboardButton('Назад', callback_data='course')
            themes_list.add(theme_a, theme_b, theme_c, goback)
            message_id = bot.send_message(umessage.chat.id, 'Выберите урок:', reply_markup=themes_list).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme4':
            themes_list = types.InlineKeyboardMarkup()
            themes_list.row_width = 1
            theme_a = types.InlineKeyboardButton('Техники завершения сделки', callback_data='theme4a')
            theme_b = types.InlineKeyboardButton('Сопровождение клиента после покупки', callback_data='theme4b')
            theme_c = types.InlineKeyboardButton('Сбор обратной связи и повышение лояльности', callback_data='theme4c')
            goback = types.InlineKeyboardButton('Назад', callback_data='course')
            themes_list.add(theme_a, theme_b, theme_c, goback)
            message_id = bot.send_message(umessage.chat.id, 'Выберите урок:', reply_markup=themes_list).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme1a':
            text = ('Добро пожаловать в мир онлайн-продаж! '
                    'Этот раздел поможет вам понять ключевые отличия онлайн-продаж от традиционных офлайн-магазинов. '
                    'Главное отличие — это скорость и доступность: покупатели могут совершать покупки в любое время и в любом месте. '
                    'Также важна персонализация: мы можем настраивать предложения под конкретного клиента. '
                    'Но, в отличие от офлайна, нет личного контакта. Поэтому, нужно уметь создавать его онлайн.')
            goback_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme1')
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus')
            goback_keyboard.add(goback, complete)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme1b':
            text = ('Давайте разберемся с ключевыми понятиями: \n'
                    'Конверсия - это процент посетителей, которые совершают покупку. \n'
                    'Средний чек - это сумма, которую в среднем тратит один покупатель. \n'
                    'Лид - это потенциальный клиент, проявивший интерес к вашему товару. \n')
            goback_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme1')
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus')
            goback_keyboard.add(goback, complete)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme1c':
            text = ('Менеджер по продажам в онлайн-магазине — это ключевая фигура. '
                    'Он не только продает, но и создает позитивный опыт для клиента. '
                    'Он должен уметь общаться, выявлять потребности и решать проблемы. '
                    'Он является лицом компании в онлайне.')
            goback_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme1')
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus')
            goback_keyboard.add(goback, complete)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme2a':
            text = ('Успешное начало диалога — залог успешной продажи. '
                    'Приветствие должно быть вежливым, быстрым и персонализированным. \n'
                    'Примеры приветствий: \n'
                    ' - Добрый день! Рады видеть вас в нашем магазине. Чем могу помочь?\n'
                    ' - Здравствуйте, (имя клиента)! Что вас интересует сегодня?\n'
                    ' - Приветствуем! Если у вас возникли вопросы, не стесняйтесь спрашивать.')
            goback_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme2')
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus')
            goback_keyboard.add(goback, complete)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme2b':
            text = ('Чтобы предложить клиенту то, что ему нужно, необходимо правильно выявить его потребности. '
                    'Задавайте открытые вопросы, внимательно слушайте ответы. \n'
                    'Список открытых вопросов: \n'
                    ' - Какую проблему вы хотите решить с помощью нашего продукта? \n'
                    ' - Какие характеристики товара для вас наиболее важны? \n'
                    ' - Какой у вас бюджет? \n'
                    ' - Что вам особенно понравилось в нашем магазине? \n'
                    ' - Что вас заставляет искать этот товар?')
            goback_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme2')
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus')
            goback_keyboard.add(goback, complete)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme2c':
            text = ('Активное слушание — это умение не только слышать, но и понимать клиента. '
                    'Перефразируйте его слова, задавайте уточняющие вопросы')
            goback_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme2')
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus')
            goback_keyboard.add(goback, complete)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme3a':
            text = ('Презентация товара в онлайне должна быть привлекательной и информативной. '
                    'Используйте качественные фото, видео, подробные описания')
            goback_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme3')
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus')
            goback_keyboard.add(goback, complete)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme3b':
            text = ('Не просто говорите о характеристиках товара, покажите, какие выгоды получит клиент. '
                    'Например: Этот телефон имеет мощную батарею, что позволит вам целый день не думать о зарядке.')
            goback_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme3')
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus')
            goback_keyboard.add(goback, complete)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme3c':
            text = ('Возражения — это нормально. '
                    'Они показывают, что клиент заинтересован. '
                    'Ваша задача — правильно отработать их.')
            goback_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme3')
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus')
            goback_keyboard.add(goback, complete)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme4a':
            text = ('Не бойтесь завершать сделку. Используйте техники, чтобы мягко подтолкнуть клиента к покупке. \n'
                    'Описание техник: \n'
                    'Альтернативный выбор: "Вы хотели бы заказать в синем или красном цвете?" \n'
                    'Резюме: "Итак, мы обсудили все детали, вы выбрали этот товар. Могу ли я оформить заказ?" \n'
                    'Ограниченное предложение: "Только сегодня действует скидка 10% на этот товар." \n')
            goback_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme4')
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus')
            goback_keyboard.add(goback, complete)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme4b':
            text = ('Не забывайте о клиенте после покупки. Поддерживайте связь, спрашивайте о впечатлениях, предлагайте помощь. \n'
                    'Шаблоны сообщений: \n'
                    ' - Спасибо за покупку! Если у вас возникнут вопросы, не стесняйтесь обращаться. \n'
                    ' - Надеемся, вам понравится товар! Мы будем рады, если вы оставите отзыв.')
            goback_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme4')
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus')
            goback_keyboard.add(goback, complete)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme4c':
            text = ('Обратная связь помогает нам стать лучше. Просите клиентов оставлять отзывы, прислушивайтесь к их мнению. \n'
                    'Методы сбора обратной связи: \n'
                    'Опросы после покупки \n'
                    'Формы для обратной связи на сайте \n'
                    'Общение в чате \n')
            goback_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme4')
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus')
            goback_keyboard.add(goback, complete)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'progress_plus':
            progress_plus(umessage)

        case 'progress':
            progress_id = umessage.chat.id
            completed_lessons = progress_data[progress_id]
            persents = round(completed_lessons/12, 2)*100
            progress_message = (f'Ваш прогресс\n'
                               f'\n'
                               f'Курсы:\n'
                               f'"Эффективные продажи в онлайн-магазине"\n'
                                f'{completed_lessons}/12 ({persents}%)')
            progress_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Назад', callback_data='main')
            progress_keyboard.add(goback)
            message_id = bot.send_message(umessage.chat.id, progress_message, reply_markup=progress_keyboard).message_id
            print(message_id)
            bot.delete_message(umessage.chat.id, message_id - 1)

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