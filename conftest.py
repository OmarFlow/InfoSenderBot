import pytest
import pytest_asyncio
from aiogram import Dispatcher, Router

from main import informer_handler
from mocked_bot import MockedBot


@pytest.fixture()
def bot():
    return MockedBot()


@pytest_asyncio.fixture()
async def disp(bot):
    dp = Dispatcher()
    r = Router()
    r.message.register(informer_handler)
    dp.include_routers(r)

    await dp.emit_startup(bot)
    try:
        yield dp
    finally:
        await dp.emit_shutdown()