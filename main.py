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
    bot.reply_to(message, """Наши команды: 
/go - создать покемона
/feed - покормить покемона
/info - информация о покемоне
    """)

@bot.message_handler(commands=['go'])
def go(message):
    username = message.from_user.username
    if username not in Pokemon.pokemons:
        pokemon = Pokemon(username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона!")

@bot.message_handler(commands=["feed"])
def feed_pokemon(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[username]
        YES_OR_NO = ["Да", "Нет"]
        rand_feed = random.choice(YES_OR_NO)
        if rand_feed == "Да":
            bot.send_message(message.chat.id, pokemon.feed_pokimon())
        else:
            bot.reply_to(message, "Рандомайзер запрещает кушать твоему покемону :(")
    else:
        bot.reply_to(message, "Сначала создай покемона командой /go")

@bot.message_handler(commands=["info"])
def info(message):
    username = message.from_user.username
    if username in Pokemon.pokemons:
        pokemon = Pokemon.pokemons[username]
        bot.send_message(message.chat.id, pokemon.info())
    else:
        bot.reply_to(message, "У тебя пока нет покемона. Используй /go")

if __name__ == "__main__":
    print("Работает.....")
    bot.polling()
