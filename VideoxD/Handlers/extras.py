from pyrogram import filters

from .. import Calls, bot, chat_id
from ..functions import admin_check


@bot.on_message(filters.command("vpause") & filters.chat(chat_id))
async def pause(client, message):
    if not Calls.is_running:
        return await message.reply(
            "There is Nothing Streaming, What Shall be Paused?"
        )
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "You Dont Have Sufficient Permissions!,(Manage Video Chats)"
        )
    if Calls.is_paused:
        return await message.reply("The Video is already paused!")
    await Calls.set_pause(True)
    return await message.reply("The Video Has Been Paused ⏸ Successfully!")


@bot.on_message(filters.command("vresume") & filters.chat(chat_id))
async def resume(client, message):
    if not Calls.is_running:
        return await message.reply("There is Nothing Streaming!")
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "You Dont Have Sufficient Permissions,(Manage Video Chat)"
        )
    if not Calls.is_paused:
        return await message.reply("The Video is already playing!")
    await Calls.set_pause(False)
    return await message.reply("The Video Has Been Resumed ▶️ Successfully!")
