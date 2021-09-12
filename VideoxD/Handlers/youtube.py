import asyncio

from pyrogram import filters

from .. import Calls, bot, chat_id
from ..functions import admin_check, user_input, video_stream, youtube_stream

que = asyncio.Queue()
number = 0
loop = asyncio.get_event_loop()

# Stream A Video From Youtube
@bot.on_message(filters.command("vplay") & filters.chat(chat_id))
async def stream(client, message):
    user_str = await user_input(message.text)
    if not user_str:
        return await message.reply(
            "Please give a youtube link/keyword to stream!"
        )
    if Calls.is_running:
        next_vid = user_str
        await que.put(next_vid)
        global number
        number += 1
        return await message.reply(
            f"Added **Video🎥** : **__{next_vid}__** To Queue!\n\n**Queued at #{number}**"
        )
    try:
        await video_stream(chat_id, user_str, client, message)
    except Exception as e:
        return await message.reply(e)


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


@bot.on_message(filters.command("vpause") & filters.chat(chat_id))
async def pause(client, message):
    if not Calls.is_running:
        return await message.reply(
            "There is Nothing Streaming, What Shall be Paused?"
        )
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "You Dont Have Sufficient Permissions!, Make Sure You Have Manage Video Chats"
        )
    await Calls.set_pause(True)
    return await message.reply("The Video Has Been Paused ⏸ Successfully!")


@bot.on_message(filters.command("vresume") & filters.chat(chat_id))
async def resume(client, message):
    if not Calls.is_running:
        return await message.reply(
            "There is Nothing Streaming, What Shall be Resumed?"
        )
    admins = await admin_check(client, message)
    if message.from_user.id not in admins:
        return await message.reply(
            "You Dont Have Sufficient Permissions!, Make Sure You Have Manage Video Chats"
        )
    await Calls.set_pause(False)
    return await message.reply("The Video Has Been Resumed ▶️ Successfully!")


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
        thumb, video, title = await loop.run_in_executor(None, youtube_stream, stuff)
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
