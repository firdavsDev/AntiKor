TELEGRAM_TOKEN = "5015901974:AAHOZX4uM5TizdZXsH7K_KMduO4TZg2QCcA" #producton token
# TELEGRAM_TOKEN = "1874165228:AAF109BDdLpDh_0fcUCrzhQOMJVm-55KNY0" #test token
OWNER_ID = 5119886926  # Admin IDsi
# OWNER_ID = 937152038  # Dev IDsi
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

