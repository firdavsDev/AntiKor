TELEGRAM_TOKEN = "1874165228:AAF109BDdLpDh_0fcUCrzhQOMJVm-55KNY0"
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
        "Toshkent",
        "Toshkent sh",
        "Samarqand",
        "Andijon",
        "Buxoro",
        "Farg'ona",
        "Jizzax",
        "Xorazm",
        "Namangan",
        "Navoiy",
        "Qashqadaryo",
        "Qoraqalpog'iston Respublikasi",
        "Sirdaryo",
        "Surxondaryo",
    },

    "ru": {
        "Ташкент",
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
