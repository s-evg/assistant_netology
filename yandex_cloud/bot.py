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
    await message.delete()


async def process_event(event, dp: Dispatcher):
    update = json.loads(event['body'])
    Bot.set_current(dp.bot)
    update = types.Update.to_object(update)
    await dp.process_update(update)


async def main(event, context):
    await process_event(event, dp)
    print(event)
    print(type(event))
    return {'statusCode': 200, 'body': 'ok'}
