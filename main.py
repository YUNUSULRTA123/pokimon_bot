import telebot 
import sys
import os
import random
sys.path.append(os.getcwd())
from config import token

from logic import Pokemon

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['start','help'])
def start(message):
    bot.reply_to(message, """Наши команды: /go ,/start ,/help ,/feed, /info, /battle""")

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        pokemon = Pokemon(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=["feed"])
def feed_pokimon(message):
    pokemon = Pokemon(message.from_user.username)
    YES_OR_NO = ["Да","Нет"]
    rand_feed = random.choice(YES_OR_NO)
    if rand_feed == "Да":
        bot.send_message(message.chat.id, pokemon.feed_pokimon())
    else:
        bot.reply_to(message, "Рандомайзер запрещает кушать твоему покимону :(")

@bot.message_handler(commands=['info'])
def info(message):
    bot.send_message(message.chat.id, Pokemon(message.from_user.username).info())

@bot.message_handler(commands=['battle'])
def battle(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        opponent = random.choice(list(Pokemon.pokemons.keys()))
        if opponent != message.from_user.username:
            result = Pokemon.battle(message.from_user.username, opponent)
            bot.send_message(message.chat.id, result)
        else:
            bot.reply_to(message, "Не удалось найти противника для битвы.")
    else:
        bot.reply_to(message, "Сначала создай покемона с помощью команды /go")
if __name__ == "__main__":
    print("Работает.....")
    bot.polling()
