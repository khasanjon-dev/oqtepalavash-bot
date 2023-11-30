import ujson

from root import settings

with open(f'{settings.bot.base_path}bot/data/data.json', 'r') as file:
    data = ujson.load(file)
    start_message = data['start_message']
