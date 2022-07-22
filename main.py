import re
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Sticker, Update
from telegram.ext import(
    CallbackContext, 
    Updater,
    PicklePersistence, 
    CommandHandler, 
    MessageHandler,
    Filters,
    CallbackQueryHandler
)
from cred import TOKEN
from menu import main_menu_keyboard, cursy_menu_keyboard
from key_bottons import tele_button, button



def start(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFToFi1aO_E2SsIF5p3SqJD90bdJPc3QACpxQAAprheUuyGE-uWLyg3ykE'
    )
    update.message.reply_text(
        "Добро пожаловать {username}".format(
            username=update.effective_user.first_name \
                if update.effective_user.first_name is not None \
                    else update.effective_user.username
        ),
        reply_markup=main_menu_keyboard()
    )


COURSE_REGEX = r"(?=("+(tele_button[1])+r"))"
ZAPIS_REGEX = r"(?=("+(tele_button[3])+r"))"
PYTHON_KEY = r"(?=("+(button[0])+r"))"
PHP_KEY = r"(?=("+(button[1])+r"))"
JS_KEY = r"(?=("+(button[2])+r"))"
BACK_KEY = r"(?=("+(button[3])+r"))"
LOCATI = r"(?=("+(tele_button[2])+r"))"
ONAS = r"(?=("+(tele_button[0])+r"))"
# MEETUP_KEY = r"(?=("+(tele_button[4])+r"))"



def zapis(update: Update, context: CallbackContext):
    z = update.message.text
    print(z[:6])
    if z[:6] == 'Запись':
        context.bot.send_message(
            chat_id = '@ogogokiwiaa',
            text = z
        )

def zapisat(update: Update, context: CallbackContext):
    info = re.match(ZAPIS_REGEX, update.message.text)
    update.message.reply_text(
        text = '''
1. Напишите сообщение с "Запись: " и ваше имя.
2. Ваш номер телефона
3. Выберите время удобный вам.
! После отправки всех заполненный бланок Админ вам позвонит.:)
        '''
    )

def resive_curse_menu(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgQAAxkBAAEFTm1i1aMu84OE8tpIE7bqRfKy6YItjQACyAkAAlpQfB3G4qX5mfzsfikE'
    )

# def resive_curse_menu(update: Update, context: CallbackContext):
    update.message.reply_text(
        'Выберите курс',
        reply_markup=cursy_menu_keyboard()
    )
def onas_curse_menu(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFToNi1aQj3sxcuBmPU-1-qsVBn6wiQgACtREAAl0XeUsYMnvZPU1DKCkE'
    )
    update.message.reply_text(
        'Программирование в Бишкеке\n'
        '\nIT курсы в столице\n'
        
        'JavaScript\n'
        'Python\n'
        'PHP'
 
        
    )


def resive_info(update: Update, context: CallbackContext):
    msg = context.bot.send_message(
        update.effective_chat.id,
        text = "Location of OGOGO"
    
    )
    update.message.reply_location(
        # 42.87397131106304, 74.61983430457343
        longitude= 74.61983430457343,
        latitude= 42.87397131106304,
        reply_to_message_id=msg.message_id
    )
def python_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Mentor', callback_data='python_mentor'),
            InlineKeyboardButton('Lesson', callback_data='python_lesson'),
        ],
        [InlineKeyboardButton('Price', callback_data='python_price')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите опцию",
        reply_markup=reply_markup
    )
    

def php_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Mentor', callback_data='php_mentor'),
            InlineKeyboardButton('Lesson', callback_data='php_lesson'),
        ],
        [InlineKeyboardButton('Price', callback_data='php_price')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите опцию",
        reply_markup=reply_markup
    )

def js_inline_menu(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton('Mentor', callback_data='js_mentor'),
            InlineKeyboardButton('Lesson', callback_data='js_lesson'),
        ],
        [InlineKeyboardButton('Price', callback_data='js_price')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        "Выберите опцию",
        reply_markup=reply_markup
    )

def back(update: Update, context: CallbackContext):
    context.bot.send_sticker(
        chat_id=update.effective_chat.id,
        sticker='CAACAgIAAxkBAAEFTnFi1aNvLSxb4otYLvQe3Zxq4R6CdgACXAADwPY0BEygC9c_qJftKQQ'
    )
    update.message.reply_text(
        'Вы вернулись назад', 
        reply_markup=main_menu_keyboard()
    )


def button(update: Update, context: CallbackContext):
    query = update.callback_query
    if query.data == 'python_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/Janelya.jpg', 'rb'),
            caption="""
Имя: Жанеля
Возраст: 21
Опыт работы: 5 лет
Место работы: IT academy,Makers, Ogogo_academy          
            """
        )
    
    if query.data == 'python_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
    
Курс Backend разработки Python
Длительность курса: 4 месяца 5 раз в неделю по 3 часа
+ 80 видеоуроков для закрепления

Программа курса:
- Введение
- Основы программирования
- Обьектно-ориентированное программирование
- Базы данных
- Тестирование
- GIT
- Django, HTML-CSS
- Restful API, Django Rest framework
- Docker, Deploy


График обучения с понедельника по пятницу.
С 15:30 до 18:30


Вам удобно в это время?



            """

        )
 
    if query.data == 'python_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
 Стоимость обучения 16000 сом за месяц.


 За это время вы защитите 4 проекта, примете участие в нескольких хакатонах, посетите
 мотивационные встречи с основателями
 IT компаний и получите сертификат гос.образца.


 А также, лучший студент группы получит новый ноутбук Acer Gateway
            """
        )
    if query.data == 'php_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/z.webp', 'rb'),
            caption="""
Имя: Зухра
Возраст: 20
Опыт работы: 4 лет
Место работы: IT academy, Ogogo academy, Makers

            """
        )
    
    if query.data == 'php_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = """

Курс Backend разработки PHP
Длительносты курса: 9 месяцев 5 раз в неделю по 2 часа + 80 видеоуроков для закрепления.



Программа курса:

- Основы языка: синтаксис, типы данных, переменные, функции, константы, массивы, объекты, выражения;
- Основы HTML, CSS и веб-дизайна;
- Реляционные БД;
- Linux, HTTP, Nginx, Apache;
- FTP, Git и другие инструменты;
- Шаблоны проектирования;
- Object-relational mapping (ORM);
- Model-View-Controller (MVC);
- Фреймворки и микрофреймворки;
- Тестирование;
- Средства виртуализации: Vagrant, Docker.

            """

        )
    if query.data == 'php_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
Стоимость обучения 10.000 сом за месяц.

График обучения с понедельника по пятницу.
С 19:00 до 21:00.

Вам удобно в это время?
            """
        )
    if query.data == 'js_mentor':
        context.bot.sendPhoto(
            update.effective_chat.id,
            photo =open('img/a.webp', 'rb'),
            caption="""
Имя: Aider
Возраст: 25
Опыт работы: 7 лет
Место работы: Tesla, Google, Apple          
            """
        )
    
    if query.data == 'js_lesson':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
    
Курсы по JS

Длительность курса: 9 месяцев 5 раз в недею по 2 часа + 80 видеоуроков для закрепления

Программа курса:
- Подключение сценариев к html-документу
- Типы данных и переменные в JavaScript
- Переменные в JavaScript
- Типы данных переменных
- Глобальные и локальные переменные
- Ключевые слова JavaScript
- Оформление имен переменных и функций в коде JavaScript


            """

        )
    if query.data == 'js_price':
        context.bot.send_message(
            update.effective_chat.id,
            text = """
Стоимость обучения 10.000 сом за месяц.


График обучения с понедельника по пятницу.
С 14:00 до 16:00.

Вам удобно в это время?
            """
        )


    
updater = Updater(TOKEN,persistence=PicklePersistence(filename='bot_data') )
updater.dispatcher.add_handler(CommandHandler('start',start))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(COURSE_REGEX), 
    resive_curse_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PYTHON_KEY), 
    python_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(LOCATI), 
    resive_info
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(PHP_KEY), 
    php_inline_menu
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(JS_KEY), 
    js_inline_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(BACK_KEY), 
    back
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ONAS), 
    onas_curse_menu
))
updater.dispatcher.add_handler(MessageHandler(
    Filters.text,
    zapisat
))

updater.dispatcher.add_handler(MessageHandler(
    Filters.regex(ZAPIS_REGEX),
    zapis
))


updater.dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()

