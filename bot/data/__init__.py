import ujson

with open('/home/khasanjon/projects/telegram-bot/oqtepalavash-bot/bot/data/data.json', 'r') as file:
    data = ujson.load(file)
    start_message = data['start_message']
