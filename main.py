import asyncio
from os import getenv

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from dotenv import load_dotenv

from logger import logger


load_dotenv()
TOKEN = getenv("BOT_TOKEN")
TO_SEND_CHAT_ID = getenv("TO_SEND_CHAT_ID")

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(F.content_type == "photo")
async def informer_handler(message: types.Message) -> Message:
    if not isinstance(message.caption, str):
        return await message.answer("Caption is required")
    try:
        return await message.send_copy(chat_id=TO_SEND_CHAT_ID)
    except Exception as e:
        logger.error(f"It faced an error: {str(e)}")


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
