#-*- coding:utf-8 -*-


import os
import json
import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from contextlib import suppress
from aiogram.utils.exceptions import (
    MessageCantBeDeleted,
    MessageToDeleteNotFound
    )


logging.basicConfig(level=logging.INFO)


TOKEN = os.getenv("TOKEN")


bot = Bot(TOKEN, parse_mode=types.ParseMode.MARKDOWN)
dp = Dispatcher(bot)


# Таймер для удаления сообщений
async def delete_message(message: types.Message, sleep_time: int = 0):
    print("Попали в таймер")
    await asyncio.sleep(sleep_time)
    print(f"Спим {sleep_time}")
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        print(f"Удаляяю сообщения ===>>> {message}")
        await message.delete()
        print(f"Сообщение удалено")


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


# Удалялка голосовых сообщений
@dp.message_handler(content_types=types.ContentTypes.VOICE)
async def del_voice(message: types.Message):
    print(f"VOICE ===>>> {message}")
    msg = await message.answer(f"{message.from_user.first_name}!\nПожалуйста, пишите сообщение текстом.\nСпасибо!")
    await message.delete()
    asyncio.create_task(delete_message(msg))
    # await message.delete()


# Проверка логики тестовых команд
@dp.message_handler(commands=['test'])
async def start(message: types.message):
    msg = await message.answer('Тестовое сообщение')
    asyncio.create_task(delete_message(msg))



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
