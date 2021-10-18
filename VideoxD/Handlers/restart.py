import os
from pyrogram import filters
from .. import Calls, bot, chat_id
from ..functions import admin_check

@bot.on_message(filters.command("restart") & filters.chat(chat_id))
async def restart(client, message):
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply("You Dont Have Sufficient Permissions!(Manage Video Chats)")
    await message.reply("Bot Restarted!")
    os.system(f"kill -9 {os.getpid()} && python3 -m VideoxD")

