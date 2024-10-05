import config

import config

import asyncio

from telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(config.token)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    await bot.reply_to(message, text)

@bot.message_handler(commands=['hi'])
async def send_hello(message):
    await bot.reply_to(message, 'Салам алекум небеса высокиееее')

@bot.message_handler(commands=['joke'])
async def send_joke(message):
    anekdot = choice(['колобок повесился', "русалка села на шпагат"])
    bot.reply_to(message, anekdot)

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


asyncio.run(bot.polling())