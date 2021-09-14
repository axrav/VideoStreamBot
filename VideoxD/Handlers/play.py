import asyncio

from pyrogram import filters

from .. import Calls, bot, chat_id
from ..functions import admin_check, user_input, video_stream, youtube_stream

que = asyncio.Queue()
number = 0
loop = asyncio.get_event_loop()


# Stream A Video From Youtube/Telegram


@bot.on_message(
    filters.command(["vplay", "vtelegram"]) & filters.chat(chat_id)
)
async def stream(client, message):
    reply = message.reply_to_message
    user_str = await user_input(message.text)
    if message.command[0][1] == "p" and not user_str:
        return await message.reply(
            "Please give a youtube link/keyword or reply /vtelegram to a valid video to stream!"
        )
    if message.command[0][1] == "t":
        if not (reply and reply.video):
            return await message.reply(
                "Please give a youtube link/keyword or reply /vtelegram to a valid video to stream!"
            )
        download_ = await message.reply("Downloading The Replied Video!")
        video = await reply.download(file_name="DOWNLOADS/")
        await download_.delete()
    if Calls.is_running:
        if user_str:
            next_vid = user_str
        else:
            next_vid = video
        await que.put(next_vid)
        global number
        number += 1
        content = user_str if user_str else "Telegram Video"
        return await message.reply(
            f"Added **Video🎥** : **__{content}__** To Queue!\n\n**Queued at #{number}**"
        )
    try:
        invideo = user_str if user_str else video
        await video_stream(chat_id, invideo, client, message)
    except Exception as e:
        return await message.reply(e)


# Stop Video Chat


@bot.on_message(filters.command("vstop") & filters.chat(chat_id))
async def stop(client, message):
    if not Calls.is_running:
        return await message.reply("No Stream Going On!")
    global number
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "You Dont Have Sufficient Permissions!, Make Sure You Have Manage Video Chats"
        )
    await Calls.stop()
    number = 0
    que._queue.clear()
    return await message.reply("The Video Has Been Stopped Successfully!")


# Skip Video Stream


@bot.on_message(filters.command("vskip") & filters.chat(chat_id))
async def skip(client, message):
    global number
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "You Dont Have Sufficient Permissions!, Make Sure You Have Manage Video Chats"
        )
    if que.empty():
        await message.reply(
            "No More Videos In Queue!\n\nLeaving Video Chat! xD"
        )
        return await Calls.stop()
    else:
        stuff = await que.get()
        number -= 1
    try:
        await video_stream(chat_id, stuff, client, message)
    except Exception as e:
        return await message.reply(e)


# Playout Ended
@Calls.on_video_playout_ended
async def media_ended(_, __):
    if que.empty():
        await bot.send_message(
            chat_id, "No More Videos In Queue!\n\nLeaving Video Chat! xD"
        )
        return await Calls.stop()
    else:
        process = await bot.send_message(chat_id, "Processing!")
        stuff = await que.get()
    try:
        if "DOWNLOADS" in stuff:
            thumb, video, title = "./img.jpg", stuff, "Telegram Audio"
            await Calls.start_video(video, repeat=False)
        else:
            thumb, video, title = await loop.run_in_executor(
                None, youtube_stream, stuff
            )
        await process.delete()
        await Calls.start_video(video, repeat=False)
        global number
        number -= 1
        ctitle = (await bot.get_chat(chat_id)).title
        return await bot.send_photo(
            chat_id,
            photo=thumb,
            caption=f"Started Streaming!\n\n**Video🎥** : **__{title}__**\n**Chat : {ctitle}**",
        )
    except Exception as e:
        return await bot.send_message(chat_id, e)
