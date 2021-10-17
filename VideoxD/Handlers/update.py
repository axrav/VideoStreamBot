import os
from pyrogram import filters
from .. import bot, chat_id
from .. import admin_check

@bot.on_message(filters.command("update") & filters.chat(chat_id))
async def update(client, message):
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply("You Dont Have Sufficient Permissions!(Manage Video Chats)")
    else:
        return await message.reply("Updated and Restarted!")
        os.system(f"git pull;kill -9 {os.getpid()} && python3 -m VideoxD")

