import telebot 
import sys
import os
import random
sys.path.append(os.getcwd())
from config import token
from logic import Pokemon, Wizard, Fighter

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['start','help'])
def start(message):
    bot.reply_to(message, """**⭐Наши команды:** 
/start или /help – 📖 помощь и начало
/go или /pokimon – 🐣 создать покемона
/feed – 🍎 покормить покемона
/info – ℹ️ информация о покемоне
/battle – ⚔️ сражение с другим покемоном
""", parse_mode="Markdown")

@bot.message_handler(commands=['go','pokimon'])
def start(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = random.randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

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
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[username]
        bot.send_message(message.chat.id, pok.info())
    else:
        bot.reply_to(message, "У тебя пока нет покемона. Используй /go")


@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
            
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")
if __name__ == "__main__":
    print("Работает.....")
    bot.polling()
