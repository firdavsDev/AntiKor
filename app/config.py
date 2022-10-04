TELEGRAM_TOKEN = "" #producton token
# TELEGRAM_TOKEN = "" #test token
OWNER_ID = 000000  # Admin IDsi
# OWNER_ID = 000000  # Dev IDsi
BOT_ID = TELEGRAM_TOKEN.split(':')[0]
# webhook settings
WEBHOOK_HOST = 'https://your.domain'
WEBHOOK_PATH = '/path/to/api'
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
# webserver settings
WEBAPP_HOST = 'localhost'  # or ip
WEBAPP_PORT = 3001

#regions
regions = {

    "uz": {
        "Тошкент",
        "Тошкент ш",
        "Самарқанд",
        "Андижон",
        "Бухоро",
        "Фарғона",
        "Жиззах",
        "Хоразм",
        "Наманган",
        "Навоий",
        "Қашқадарё",
        "Қорақалпоғистон Республикаси",
        "Сирдарё",
        "Сурхондарё",
    },

    "ru": {
        "Ташкент",
        "Ташкент ш",
        "Самарканд",
        "Андижан",
        "Бухара",
        "Фергана",
        "Джизак",
        "Хорезм",
        "Наманган",
        "Навои",
        "Кашкадарья",
        "Республика Каракалпакстан",
        "Сырдарья",
        "Сурхандарья",
        }
}

