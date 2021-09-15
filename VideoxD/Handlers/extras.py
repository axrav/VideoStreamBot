from pyrogram import filters

from .. import Calls, bot, chat_id
from ..functions import admin_check


@bot.on_message(filters.command("vpause") & filters.chat(chat_id))
async def pause(client, message):
    if not Calls.is_running:
        return await message.reply(
            "𝗧𝗵𝗲𝗿𝗲 𝗜𝘀 𝗡𝗼𝘁𝗵𝗶𝗻𝗴 𝗦𝘁𝗿𝗲𝗮𝗺𝗶𝗻𝗴✨"
        )
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "𝗬𝗼𝘂 𝗗𝗼𝗻𝘁 𝗛𝗮𝘃𝗲 𝗣𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻✨"
        )
    if Calls.is_paused:
        return await message.reply(
            "𝗧𝗵𝗲 𝗩𝗶𝗱𝗲𝗼 𝗜𝘀 𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗣𝗮𝘂𝘀𝗲✨"
        )
    await Calls.set_pause(True)
    return await message.reply("𝗧𝗵𝗲 𝗩𝗶𝗱𝗲𝗼 𝗛𝗮𝘀 𝗕𝗲𝗲𝗻 𝗣𝗮𝘂𝘀𝗲 𝗦𝘂𝗰𝘀𝗲𝘀𝗳𝘂𝗹𝗹𝘆✨")


@bot.on_message(filters.command("vresume") & filters.chat(chat_id))
async def resume(client, message):
    if not Calls.is_running:
        return await message.reply(
            "𝗧𝗵𝗲𝗿𝗲 𝗜𝘀 𝗡𝗼𝘁𝗵𝗶𝗻𝗴 𝗦𝘁𝗿𝗲𝗮𝗺𝗶𝗻𝗴✨"
        )
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "𝗬𝗼𝘂 𝗗𝗼𝗻𝘁 𝗛𝗮𝘃𝗲 𝗣𝗲𝗿𝗺𝗶𝘀𝘀𝗶𝗼𝗻✨"
        )
    if not Calls.is_paused:
        return await message.reply(
            "𝗧𝗵𝗲 𝗩𝗶𝗱𝗲𝗼 𝗜𝘀 𝗔𝗹𝗿𝗲𝗮𝗱𝘆 𝗣𝗹𝗮𝘆𝗶𝗻𝗴✨"
        )
    await Calls.set_pause(False)
    return await message.reply("𝗧𝗵𝗲 𝗩𝗶𝗱𝗲𝗼 𝗛𝗮𝘀 𝗕𝗲𝗲𝗻 𝗥𝗲𝘀𝘂𝗺𝗲 𝗦𝘂𝗰𝗰𝗲𝘀𝘀𝗳𝘂𝗹𝗹𝘆✨")
