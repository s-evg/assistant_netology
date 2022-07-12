import logging
import os

from aiogram import Bot, Dispatcher, types

# log
logging.basicConfig(level=logging.INFO)


# Удаление сообщений о присоединении новых пользователей
async def on_user_joined(message: types.Message):
    await message.delete()


# Selectel Lambda funcs
async def register_handlers(dp: Dispatcher):

    dp.register_message_handler(on_user_joined, content_types=["new_chat_members"])


async def process_event(update, dp: Dispatcher):

    Bot.set_current(dp.bot)
    await dp.process_update(update)


# Selectel serverless entry point
async def main(**kwargs):
    bot = Bot(os.environ.get("TOKEN"))
    dp = Dispatcher(bot)
    await register_handlers(dp)
    update = types.Update.to_object(kwargs)
    await process_event(update, dp)

    return 'ok'