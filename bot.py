import os

import telebot
from jinja2 import Template
from dotenv import load_dotenv
from models import Pizza, Choice

load_dotenv()
TOKEN = os.environ.get('TELEGRAM_TOKEN')
if not TOKEN:
    raise Exception('BOT_TOKEN should be specified')
bot = telebot.TeleBot(TOKEN)

with open('templates/catalog.md', 'r') as catalog_file:
    catalog_tmpl = Template(catalog_file.read())

with open('templates/greetings.md', 'r') as greetings_file:
    greetings_tmpl = Template(greetings_file.read())

catalog = Pizza.query.join(Choice).all()

catalog = [{
            'title': product.title,
            'description': product.description,
            'choices': list({
                        'title': choice.title,
                        'price': choice.price}
                        for choice in product.choices)}
            for product in catalog]

@bot.message_handler(commands=['start'])
def greet(message):
    bot.send_message(message.chat.id, greetings_tmpl.render())

@bot.message_handler(commands=['menu'])
def show_catalog(message):
    bot.send_message(message.chat.id, catalog_tmpl.render(catalog=catalog), parse_mode='Markdown')

if __name__ == '__main__':
    bot.polling(none_stop=True)
