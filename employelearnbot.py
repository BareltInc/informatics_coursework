# import requests, random
# from bs4 import BeautifulSoup
from telebot import *

token = '7398398254:AAFa27_AjW45tXGjZbXSlMou8YH0cnsAx8I'
bot = telebot.TeleBot(token)
user_data = {}
progress_data = {}


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
    progress_data[user_id] = []
    continue_keyboard = types.InlineKeyboardMarkup()
    continue_button = types.InlineKeyboardButton('Продолжить', callback_data='main')
    continue_keyboard.add(continue_button)
    bot.send_message(message.chat.id, f'Приятно познакомиться, {user_name}!', reply_markup=continue_keyboard)
    print(user_data)

def progress_plus(message, theme):
    user_id = message.chat.id
    completed_themes = progress_data[user_id]
    completed_themes.append(theme)
    progress_data[user_id] = list(set(completed_themes))
    print(progress_data)

@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    option = call.data
    umessage = call.message
    match option:
        case 'start':
            bot.send_message(umessage.chat.id, text='Как вас зовут')
            bot.register_next_step_handler(umessage, registration)

        case 'main':
            choose_topic = types.InlineKeyboardMarkup()
            account_b = types.InlineKeyboardButton('Аккаунт', callback_data='account')
            theme_b = types.InlineKeyboardButton('Выбор темы', callback_data='course')
            progress_b = types.InlineKeyboardButton('Прогресс', callback_data='progress')
            choose_topic.row_width = 1
            choose_topic.add(account_b, theme_b, progress_b)
            message_id = bot.send_message(umessage.chat.id, 'Курс "Эффективные продажи в онлайн-магазине"', reply_markup=choose_topic).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'account':
            chatid = umessage.chat.id
            username = user_data[chatid]
            account_message = (f'{username} \n'
                               f'\n'
                               f'Курсы:\n'
                               f'  "Эффективные продажи в онлайн-магазине"')
            account_keyboard = types.InlineKeyboardMarkup()
            account_button = types.InlineKeyboardButton('Назад', callback_data='main')
            account_keyboard.add(account_button)
            message_id = bot.send_message(umessage.chat.id, account_message, reply_markup=account_keyboard).message_id
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
            bot.delete_message(umessage.chat.id, message_id - 1)

        case 'theme1a':
            image = open('difference.png', 'rb')
            text = ('Добро пожаловать в увлекательный мир онлайн-продаж! '
                    'Этот раздел заложит фундамент вашего понимания специфики этого канала. '
                    'В отличие от традиционных офлайн-магазинов, где взаимодействие происходит лицом к лицу, онлайн-продажи полагаются на цифровые инструменты и коммуникацию. '
                    'Главное преимущество — это скорость и доступность: клиенты могут совершать покупки в любое время дня и ночи, из любой точки мира, имея лишь доступ к интернету. '
                    'Также важна персонализация: онлайн позволяет собирать данные о клиентах и настраивать предложения под их конкретные потребности и предпочтения. '
                    'Это может быть история покупок, поисковые запросы или поведение на сайте. '
                    'Но, в отличие от офлайна, здесь нет прямого физического контакта. '
                    'Поэтому, мы должны уметь создавать доверительную атмосферу и эффективно общаться с клиентами в цифровом формате, используя текстовые сообщения, чаты, электронную почту и другие средства связи.')
            article_link = 'https://softservice-group.ru/online-vs-ofline/'
            video_link = 'https://www.youtube.com/watch?v=lLdMnMTYaf0'
            goback_keyboard = types.InlineKeyboardMarkup()
            goback_keyboard.row_width = 2
            article = types.InlineKeyboardButton('Статья', url=article_link)
            video = types.InlineKeyboardButton('Видео', url=video_link)
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus_1a')
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme1')
            goback_keyboard.add(article, video, complete, goback)
            message_id = bot.send_photo(umessage.chat.id, image, caption=text, reply_markup=goback_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)
        case 'progress_plus_1a':
            progress_plus(umessage, '1a')

        case 'theme1b':
            image = open('leads.jpg', 'rb')
            text = ('Давайте разберемся с основными понятиями, которые помогут нам измерять эффективность наших усилий. \n'
                    'Конверсия — это процент посетителей вашего сайта или страницы, которые совершают целевое действие, чаще всего, покупку. '
                    'Выражается в процентах и показывает, насколько хорошо ваш сайт или контент мотивирует клиентов к покупке. '
                    ''
                    'Средний чек — это средняя сумма, которую тратит один покупатель в вашем магазине за одну покупку. '
                    'Это важный показатель, влияющий на общую выручку магазина. '
                    ''
                    'Лид — это потенциальный клиент, который проявил интерес к вашему продукту или услуге, например, оставил свой контактный номер или email. '
                    'Важно понимать, что лид — это ещё не покупатель, но он демонстрирует готовность к взаимодействию, и его нужно умело «вести» к покупке.')
            article_link = 'https://www.advantshop.net/blog/analitika/kpi-v-onlain-torgovle-kak-izmerit-uspeshnost-raboty-biznesa'
            video_link = 'https://www.youtube.com/watch?v=C36kGAVloQc'
            goback_keyboard = types.InlineKeyboardMarkup()
            goback_keyboard.row_width = 2
            article = types.InlineKeyboardButton('Статья', url=article_link)
            video = types.InlineKeyboardButton('Видео', url=video_link)
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus_1b')
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme1')
            goback_keyboard.add(article, video, complete, goback)
            message_id = bot.send_photo(umessage.chat.id, image, caption=text, reply_markup=goback_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)
        case 'progress_plus_1b':
            progress_plus(umessage, '1b')

        case 'theme1c':
            text = ('Роль менеджера по продажам в онлайн-магазине выходит за рамки простого приема заказов. '
                    'Вы - ключевая фигура, которая формирует восприятие компании в цифровом пространстве. '
                    'Ваша работа включает не только помощь в выборе товара и оформление заказа, но и создание позитивного опыта для каждого клиента. '
                    'Вы должны быть не только отличными продавцами, но и экспертами в товаре, а также консультантами, способными понять потребности клиента и предложить наилучшее решение. '
                    'Важны коммуникабельность, эмпатия, умение быстро реагировать на запросы, а также техническая грамотность, поскольку вся работа происходит в цифровой среде. '
                    'Вы — лицо компании в онлайн-пространстве, и именно от вас зависит, вернется ли клиент к нам снова.')
            article_link = 'https://prime-ltd.su/blog/rol-menedzhera-v-internet-magazine/'
            video_link = 'https://www.youtube.com/watch?v=Eu9HBNh71uo'
            goback_keyboard = types.InlineKeyboardMarkup()
            goback_keyboard.row_width = 2
            article = types.InlineKeyboardButton('Статья', url=article_link)
            video = types.InlineKeyboardButton('Видео', url=video_link)
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus_1c')
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme1')
            goback_keyboard.add(article, video, complete, goback)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)
        case 'progress_plus_1c':
            progress_plus(umessage, '1c')

        case 'theme2a':
            image = open('communication.jpg', 'rb')
            text = ('Успешное установление контакта — это фундамент для продуктивного диалога и успешной продажи. '
                    'Первое сообщение должно быть вежливым, быстрым и персонализированным, насколько это возможно. '
                    'Забудьте про шаблонные фразы - старайтесь обращаться к клиенту по имени, если это возможно, и покажите, что вы готовы помочь. '
                    'Внимательно следите за временем ответа; долгие задержки могут отпугнуть клиента. '
                    'Используйте приветственные фразы, которые создают позитивный настрой и показывают вашу готовность к диалогу. '
                    'Проявите искренний интерес к запросу клиента, чтобы он почувствовал вашу заботу и вовлеченность. '
                    'Начните разговор с открытого вопроса, который поможет клиенту описать свою потребность.')
            article_link = 'https://www.kom-dir.ru/article/3580-ustanovlenie-kontakta-v-prodajah'
            video_link = 'https://www.youtube.com/watch?v=plYGH-P5QQA'
            goback_keyboard = types.InlineKeyboardMarkup()
            goback_keyboard.row_width = 2
            article = types.InlineKeyboardButton('Статья', url=article_link)
            video = types.InlineKeyboardButton('Видео', url=video_link)
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus_2a')
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme2')
            goback_keyboard.add(article, video, complete, goback)
            message_id = bot.send_photo(umessage.chat.id, image, caption=text, reply_markup=goback_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)
        case 'progress_plus_2a':
            progress_plus(umessage, '2a')

        case 'theme2b':
            image = open('needs.png', 'rb')
            text = ('Чтобы предложить клиенту именно то, что ему нужно, необходимо научиться правильно выявлять его потребности и мотивацию. '
                    'Задавайте открытые вопросы, требующие развернутого ответа, а не просто «да» или «нет». '
                    'Внимательно слушайте ответы, обращайте внимание на детали и ключевые слова, которые помогут вам понять истинные намерения клиента. '
                    'Постарайтесь понять, какую проблему клиент хочет решить с помощью вашего продукта или услуги, какие характеристики и качества для него наиболее важны. '
                    'Используйте технику «5 почему», если это необходимо, чтобы добраться до самой сути проблемы. '
                    'Важно понять не только, что клиент хочет, но и почему он этого хочет, что его мотивирует к покупке.')
            article_link = 'https://kontur.ru/articles/6237'
            video_link = 'https://www.youtube.com/watch?v=bP9niNRcycE'
            goback_keyboard = types.InlineKeyboardMarkup()
            goback_keyboard.row_width = 2
            article = types.InlineKeyboardButton('Статья', url=article_link)
            video = types.InlineKeyboardButton('Видео', url=video_link)
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus_2b')
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme2')
            goback_keyboard.add(article, video, complete, goback)
            message_id = bot.send_photo(umessage.chat.id, image, caption=text, reply_markup=goback_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)
        case 'progress_plus_2b':
            progress_plus(umessage, '2b')

        case 'theme2c':
            image = open('listening.png', 'rb')
            text = ('Активное слушание — это не просто молчание во время разговора, а сознательное усилие понять собеседника. '
                    'Оно заключается в том, чтобы внимательно слушать, что говорит клиент, не перебивая, и показывать, что вы вовлечены в разговор. '
                    'Перефразируйте слова клиента, чтобы убедиться, что вы правильно его поняли, и задавайте уточняющие вопросы, чтобы получить более точную информацию. '
                    'Используйте эмпатию, чтобы показать клиенту, что вы понимаете его чувства и переживания. '
                    'Активное слушание и правильные вопросы не только помогут вам получить необходимую информацию, но и помогут клиенту почувствовать себя ценным и важным, что увеличит его лояльность и готовность к покупке.')
            article_link = 'https://kontur.ru/talk/spravka/52358-aktivnoe_slushanie_v_kakih_situaciyah_prigoditsya'
            video_link = 'https://www.youtube.com/watch?v=GHAg1AXPZx8'
            goback_keyboard = types.InlineKeyboardMarkup()
            goback_keyboard.row_width = 2
            article = types.InlineKeyboardButton('Статья', url=article_link)
            video = types.InlineKeyboardButton('Видео', url=video_link)
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus_2c')
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme2')
            goback_keyboard.add(article, video, complete, goback)
            message_id = bot.send_photo(umessage.chat.id, image, caption=text, reply_markup=goback_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)
        case 'progress_plus_2c':
            progress_plus(umessage, '2c')

        case 'theme3a':
            image = open('AIDA.png', 'rb')
            text = ('Презентация товара в онлайн-магазине должна быть максимально привлекательной и информативной. '
                    'Используйте качественные фотографии и видео, которые показывают товар с разных ракурсов и в разных ситуациях использования. '
                    'Подробное и точное описание характеристик и особенностей товара — обязательное условие. '
                    'Выделите ключевые преимущества и покажите, как они могут решить проблемы клиента или улучшить его жизнь. '
                    'Не забудьте про призыв к действию, например, "Добавить в корзину", "Купить сейчас" или "Узнать больше". '
                    'Важно не просто перечислить характеристики, а показать выгоды для клиента, используя эмоциональные описания, которые вызывают интерес и желание приобрести товар. '
                    'Создайте такое впечатление, что товар уже находится в руках у клиента.')
            article_link = 'https://www.advantshop.net/blog/start/kak-effektivno-prezentovat-tovar-v-internet-magazine'
            video_link = 'https://www.youtube.com/watch?v=SDdmX9tEjX4'
            goback_keyboard = types.InlineKeyboardMarkup()
            goback_keyboard.row_width = 2
            article = types.InlineKeyboardButton('Статья', url=article_link)
            video = types.InlineKeyboardButton('Видео', url=video_link)
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus_3a')
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme3')
            goback_keyboard.add(article, video, complete, goback)
            message_id = bot.send_photo(umessage.chat.id, image, caption=text, reply_markup=goback_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)
        case 'progress_plus_3a':
            progress_plus(umessage, '3a')

        case 'theme3b':
            image = open('advantages.jpg', 'rb')
            text = ('Ключ к успешной презентации — это умение трансформировать характеристики товара в конкретные выгоды для клиента. '
                    'Не зацикливайтесь на технических деталях, покажите, как эти детали улучшают жизнь клиента. '
                    'Например, если у телефона есть мощный аккумулятор, не просто скажите, что он "мощный", а объясните, что это означает, что клиенту не придется постоянно беспокоиться о зарядке в течение дня. '
                    'Используйте язык выгод, который понятен и близок клиенту. '
                    'Старайтесь понять, что именно для него важно, и подчеркивайте именно эти аспекты. '
                    'Не забывайте, что клиенты покупают не товары, а решения своих проблем и удовлетворение своих потребностей.')
            article_link = 'https://www.calltouch.ru/blog/hpv-v-prodazhah-kak-ispolzovat-tehniku-harakteristika-preimushhestvo-vygoda-dlya-uvelicheniya-prodazh/'
            video_link = 'https://www.youtube.com/watch?v=CHxNjex9x2M'
            goback_keyboard = types.InlineKeyboardMarkup()
            goback_keyboard.row_width = 2
            article = types.InlineKeyboardButton('Статья', url=article_link)
            video = types.InlineKeyboardButton('Видео', url=video_link)
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus_3b')
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme3')
            goback_keyboard.add(article, video, complete, goback)
            message_id = bot.send_photo(umessage.chat.id, image, caption=text, reply_markup=goback_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)
        case 'progress_plus_3b':
            progress_plus(umessage, '3b')

        case 'theme3c':
            image = open('objection.webp', 'rb')
            text = ('Возражения клиентов — это неотъемлемая часть процесса продаж. '
                    'Не стоит их бояться, скорее, наоборот, рассматривать как возможность убедить клиента в ценности вашего товара и отработать его сомнения. '
                    'Типичные возражения, такие как «дорого» или «я подумаю», должны быть отработаны с уверенностью и профессионализмом. '
                    'Вместо того, чтобы спорить с клиентом, используйте эмпатию, чтобы понять его точку зрения. '
                    'Предлагайте альтернативные варианты, если цена вызывает вопросы, или дайте клиенту время подумать, но обязательно предложите вашу помощь в случае возникновения вопросов. '
                    'Главное — оставаться позитивным и уверенным, не теряя настойчивости.')
            article_link = 'https://www.insales.ru/blogs/university/kak-rabotat-s-vozrazheniyami'
            video_link = 'https://www.youtube.com/watch?v=il54IlwQBKQ'
            goback_keyboard = types.InlineKeyboardMarkup()
            goback_keyboard.row_width = 2
            article = types.InlineKeyboardButton('Статья', url=article_link)
            video = types.InlineKeyboardButton('Видео', url=video_link)
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus_3c')
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme3')
            goback_keyboard.add(article, video, complete, goback)
            message_id = bot.send_photo(umessage.chat.id, image, caption=text, reply_markup=goback_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)
        case 'progress_plus_3c':
            progress_plus(umessage, '3c')

        case 'theme4a':
            image = open('finish.jpg', 'rb')
            text = ('Завершение сделки — это момент, когда вы мягко, но уверенно подталкиваете клиента к покупке. '
                    'Используйте техники, которые помогут вам перейти от диалога к действию. \n'
                    'Техника "альтернативный выбор" — это предложение клиенту выбора между несколькими вариантами товара, что помогает принять решение. \n'
                    'Техника "резюме" — это краткое повторение всех преимуществ и выгод выбранного товара, чтобы клиент еще раз убедился в своем выборе. \n'
                    'Техника "ограниченное предложение" — это создание срочности, например, через скидки или акции, которые действуют только ограниченное время. \n'
                    'Важно не давить на клиента, а мягко подвести его к завершению сделки, показав, что вы готовы помочь ему сделать правильный выбор.')
            article_link = 'https://aspro.cloud/crm/docs/zavershenie-sdelki/'
            video_link = 'https://www.youtube.com/watch?v=nSFwoiNuXfk'
            goback_keyboard = types.InlineKeyboardMarkup()
            goback_keyboard.row_width = 2
            article = types.InlineKeyboardButton('Статья', url=article_link)
            video = types.InlineKeyboardButton('Видео', url=video_link)
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus_4a')
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme4')
            goback_keyboard.add(article, video, complete, goback)
            message_id = bot.send_photo(umessage.chat.id, image, caption=text, reply_markup=goback_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)
        case 'progress_plus_4a':
            progress_plus(umessage, '4a')

        case 'theme4b':
            text = ('Сопровождение клиента после покупки — это не менее важный этап, чем сама продажа. '
                    'Не забывайте о клиенте после того, как он совершил покупку. '
                    'Отправьте ему благодарственное письмо или сообщение, предложите свою помощь в случае возникновения вопросов или проблем. '
                    'Поддерживайте связь с клиентом, узнавайте его впечатления от товара, предлагайте специальные условия для повторных покупок. '
                    'Положительный опыт после покупки повышает лояльность клиентов и увеличивает вероятность того, что он вернется к вам снова и посоветует ваш магазин своим друзьям. '
                    'Важно показать клиенту, что вы цените его доверие и готовы поддержать его на всех этапах взаимодействия.')
            article_link = 'https://www.mango-office.ru/journal/for-marketing/prodazhi/posleprodazhnoe-obsluzhivanie/'
            goback_keyboard = types.InlineKeyboardMarkup()
            goback_keyboard.row_width = 2
            article = types.InlineKeyboardButton('Статья', url=article_link)
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus_4b')
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme4')
            goback_keyboard.add(article, complete, goback)
            message_id = bot.send_message(umessage.chat.id, text, reply_markup=goback_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)
        case 'progress_plus_4b':
            progress_plus(umessage, '4b')

        case 'theme4c':
            image = open('feedback.jpeg', 'rb')
            text = ('Сбор обратной связи — это не просто возможность услышать мнение клиентов, но и мощный инструмент для улучшения вашей работы. '
                    'Предлагайте клиентам оставлять отзывы о товарах и о качестве обслуживания. '
                    'Прислушивайтесь к их мнению, анализируйте их замечания и используйте эту информацию для оптимизации процессов. '
                    'Важно не только собирать обратную связь, но и активно реагировать на нее, отвечая на вопросы и решая проблемы клиентов. '
                    'Своевременная реакция на обратную связь показывает, что вы заботитесь о клиентах и делаете все возможное, чтобы обеспечить их удовлетворенность. '
                    'Это один из лучших способов повысить лояльность клиентов и построить с ними долгосрочные отношения.')
            article_link = 'https://habr.com/ru/companies/planado/articles/311482/'
            video_link = 'https://www.youtube.com/watch?v=fCZFTI6hpmw'
            goback_keyboard = types.InlineKeyboardMarkup()
            goback_keyboard.row_width = 2
            article = types.InlineKeyboardButton('Статья', url=article_link)
            video = types.InlineKeyboardButton('Видео', url=video_link)
            complete = types.InlineKeyboardButton('Просмотрено', callback_data='progress_plus_4c')
            goback = types.InlineKeyboardButton('Выйти', callback_data='theme4')
            goback_keyboard.add(article, video, complete, goback)
            message_id = bot.send_photo(umessage.chat.id, image, caption=text, reply_markup=goback_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)
        case 'progress_plus_4c':
            progress_plus(umessage, '4c')

        case 'progress':
            progress_id = umessage.chat.id
            completed_lessons = progress_data[progress_id]
            persents = round(len(completed_lessons)/12, 2)*100
            progress_message = (f'Ваш прогресс\n'
                               f'\n'
                               f'Курсы:\n'
                               f'"Эффективные продажи в онлайн-магазине"\n'
                                f'{len(completed_lessons)}/12 ({persents}%)')
            progress_keyboard = types.InlineKeyboardMarkup()
            goback = types.InlineKeyboardButton('Назад', callback_data='main')
            progress_keyboard.add(goback)
            message_id = bot.send_message(umessage.chat.id, progress_message, reply_markup=progress_keyboard).message_id
            bot.delete_message(umessage.chat.id, message_id - 1)

# @bot.message_handler(commands=['pc_action'])
# def pc_action(message):
#     response = requests.get('https://www.igromania.ru/games/pc/action/')
#     html = BeautifulSoup(response.content, 'lxml')
#     pca = random.choice(html.find_all(class_='game-card'))
#     bot.send_message(message.chat.id, pca.find(class_='name').text)

@bot.message_handler(commands=['end'])
def send_welcome_message(message):
    print(message.from_user.first_name)
    print(message.chat.id)
    bb_message = f'Пока, {message.from_user.first_name}, возвращайся ещё!'
    bot.send_message(message.chat.id, bb_message)

bot.polling()