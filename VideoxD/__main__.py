import asyncio

from pyrogram import idle

from misc import Calls, app, bot


async def init():
    await app.start()
    print("User account Initialized!")
    await bot.start()
    print("Bot Initialized!")
    await idle()


loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(init())
