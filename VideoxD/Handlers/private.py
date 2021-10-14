from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .. import HELP, bot

# basic commands


@bot.on_message(filters.command("alive"))
async def startxd(client, message):
    return await message.reply(
        "Yes I am Alive!,Who Cares About Someone Else!"
    )


@bot.on_message(filters.command(["start", "help"]))
async def start(client, message):
    if message.chat.type == "supergroup":
        return await message.reply("DM me to Know about my commands!")
    sender_mention = message.from_user.mention
    return await message.reply(
        f"Hi! {sender_mention}, This is a Video Streaming Bot. Here is the link to my source code!",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Repository",
                        url="https://github.com/VegetaxD/VideoStreamBot",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Commands", callback_data="commands"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Support Chat/Demo",
                        url="https://t.me/VideoStreamSupport",
                    )
                ],
            ]
        ),
    )


@bot.on_message(filters.command("repo"))
async def repo(client, message):
    return await message.reply(
        "Here is the Repository!",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Repository",
                        url="https://github.com/VegetaxD/VideoStreamBot",
                    )
                ]
            ]
        ),
    )


@bot.on_callback_query(filters.regex("commands"))
async def command_(_, cb):
    await bot.send_message(cb.message.chat.id, text=HELP)
    return await cb.message.delete()
