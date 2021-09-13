import asyncio

from pyrogram import idle

from misc import Calls, app, bot


async def init():
    await app.start()
    print("User account Initialized!")
    await bot.start()
    print("Bot Initialized!")
    print("You Might see No Plugins Loaded Thats A Bug By latest version of Pyrogram, Plugins have Been Loaded Successfully!")
    await idle()
    

loop = asyncio.get_event_loop()
if __name__ == "__main__":
    loop.run_until_complete(init())
