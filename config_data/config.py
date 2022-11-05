import os
from dotenv import load_dotenv, find_dotenv

if not find_dotenv():
    exit('Переменные окружения не загружены т.к отсутствует файл .env')
else:
    load_dotenv()

# BOT_TOKEN = os.getenv('BOT_TOKEN')
# RAPID_API_KEY = os.getenv('RAPID_API_KEY')
BOT_TOKEN = os.getenv('5746583328:AAGWbrwSkrNRO7RKhPaJ3rmCKuxxCa7chIw')
RAPID_API_KEY = os.getenv('4be51f1e2cmsh6a32f721a78b683p1b0045jsn3beeed16815c')

DEFAULT_COMMANDS = (
    ('start', "Запустить бота"),
    ('help', "Вывести справку")
)
