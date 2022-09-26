TELEGRAM_TOKEN = "5015901974:AAHOZX4uM5TizdZXsH7K_KMduO4TZg2QCcA"
OWNER_ID = 937152038  # Admin IDsi
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
        "Xorazm",
        "Toshkent"
    },
    "ru": {
        'Xorazm_ru', 
        'Toshkent_ru'
        }
}
