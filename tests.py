import pytest

from aiogram import types
from aiogram.methods import SendMessage
from aiogram.types import Chat, Update


@pytest.mark.asyncio
async def test_informer_handler(disp, bot):
    chat = Chat(chat_id=1, type="public", id=1)
    message = types.Message(
        message_id=1,
        from_user=None,
        date=1698668950,
        chat=chat,
        content_type=types.ContentType.PHOTO,
        caption="This is caption",
        photo=[types.PhotoSize(
                file_id="my_file_id",
                file_unique_id='photo_file_unique_id',
                width=640,
                height=480,
                file_size=12345,
            )]
    )

    prepare_result = bot.add_result_for(
        SendMessage,
        ok=True,
        result=message,
    )
    update = Update(update_id=1, message=message)
    res = await disp.feed_update(bot=bot, update=update)

    assert prepare_result.result == res
    assert prepare_result.result.photo == res.photo


@pytest.mark.asyncio
async def test_informer_handler_caption_reqired(disp, bot):
    chat = Chat(chat_id=1, type="public", id=2)
    message = types.Message(
        message_id=2,
        from_user=None,
        date=1698768950,
        chat=chat,
        content_type=types.ContentType.PHOTO,
    )

    res = types.Message(
        message_id=3,
        from_user=None,
        date=1698768950,
        chat=chat,
        text='Caption is required',
        content_type=types.ContentType.TEXT,
    )

    prepare_result = bot.add_result_for(
        SendMessage,
        ok=True,
        result=res,
    )
    update = Update(update_id=1, message=message)
    res = await disp.feed_update(bot=bot, update=update)

    assert prepare_result.result == res
    assert prepare_result.result.text == res.text
