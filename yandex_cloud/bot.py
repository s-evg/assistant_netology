#-*- coding:utf-8 -*-


import os
import json
import logging
from aiogram import Bot, Dispatcher, types


logging.basicConfig(level=logging.INFO)


TOKEN = os.getenv("TOKEN")


bot = Bot(TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)


# Удаление сообщений о присоединении новых пользователей
@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joined(message: types.Message):
    print(f"NEW_MEMBERS ===>>> {message}")
    await message.delete()


# Удаление случайных комманд /add /show /print
@dp.message_handler(commands=["add", "show", "print", "start"])
async def on_user_joined(message: types.Message):
    print(f"COOMMANDS ===>>> {message.text}")
    command = message.text.split()
    if len(command) == 1:
        await message.delete()


async def process_event(event, dp: Dispatcher):
    update = json.loads(event['body'])
    print(f"UPDATE ===>>> {update}")
    Bot.set_current(dp.bot)
    update = types.Update.to_object(update)
    await dp.process_update(update)


async def main(event, context):
    # print(f"EVENT ===>>> {event}")
    await process_event(event, dp)
    return {'statusCode': 200, 'body': 'ok'}
