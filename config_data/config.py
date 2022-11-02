import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

BOT_TOKEN = os.getenv('5746583328:AAFDFaFJ8slUTdRV1UlH_hZIWbbiyyo9W1c')
RAPID_API_KEY = os.getenv('4be51f1e2cmsh6a32f721a78b683p1b0045jsn3beeed16815c')
DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку")
)
