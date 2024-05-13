import os
from emoji import emojize

TOKEN = '7108971240:AAG23VQEO6u9RU1TZUHj5Is2ZR6g8xelaRs'
NAME_DB = 'products.db'

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join('sqlite:///'+BASE_DIR, NAME_DB)

COUNT = 0

# кнопки управления
KEYBOARD = {
    'CHOOSE_GOODS': emojize('🛒 Выбрать товар'),
    'INFO': emojize(':speech_balloon: О магазине'),
    'SETTINGS': emojize('⚙️ Настройки'),
    'PHONES': emojize('📱 Телефоны'),
    'LAPTOP': emojize('💻 Ноутбуки'),
    'HEADPHONES': emojize('🎧 Наушники'),
    '<<': emojize('⏪'),
    '>>': emojize('⏩'),
    'BACK_STEP': emojize('◀️'),
    'NEXT_STEP': emojize('▶️'),
    'ORDER': emojize('🛒 Заказ'),
    'X': emojize('❌'),
    'DOUWN': emojize('🔽'),
    'AMOUNT_PRODUCT': COUNT,
    'AMOUNT_ORDERS': COUNT,
    'UP': emojize('🔼'),
    'APPLAY': '✅ Оформить заказ',
}

# id категорий продуктов
CATEGORY = {
    'PHONES': 1,
    'LAPTOP': 2,
    'HEADPHONES': 3,
}

# названия команд
COMMANDS = {
    'START': "start",
    'HELP': "help",
}
