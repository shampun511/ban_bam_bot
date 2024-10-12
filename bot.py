import config
from random import choice

import Telebot
import asyncio

from Telebot.async_telebot import AsyncTeleBot

bot = AsyncTeleBot(config.token)

banned_users = set()
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

@bot.message_handler(user_id=banned_users)
async def handle_banned(msg: Message):
    print(f"{msg.from_user.full_name} пишет, но мы ему не ответим!")
    return True


@bot.message_handler()
async def handle_all(msg: Message):
    await msg.reply(f"Добрый день, {msg.from_user.full_name} :)")


@bot.message_handler(commands=['ban'], user_id=12312312312312) # здесь укажи свой ID
async def handle_ban_command(msg: Message):
    # проверяем, что ID передан правильно
    try:
        abuser_id = int(msg.get_args())
    except (ValueError, TypeError):
        return await msg.reply("Укажи ID пользователя.")
    
    banned_users.add(abuser_id)
    await msg.reply(f"Пользователь {abuser_id} заблокирован.")

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)


asyncio.run(bot.polling())