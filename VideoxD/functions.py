import asyncio

import pafy
from youtubesearchpython import VideosSearch

from misc import Calls, bot

loop = asyncio.get_event_loop()

# pafy


def url_stream(url: str):
    video = pafy.new(url)
    videos = video.getbest().url
    return videos


# Youtube


def youtube_stream(query: str):
    search = VideosSearch(query, limit=1).result()
    thumb = search["result"][0]["thumbnails"][0]["url"].split("?")[0]
    link = search["result"][0]["link"]
    title = search["result"][0]["title"]
    video = url_stream(link)
    return thumb, video, title


# User Input


async def user_input(input):
    if " " in input or "\n" in input:
        return str(input.split(maxsplit=1)[1].strip())
    return ""


# admin check
async def admin_check(client, message):
    x = await bot.get_chat_members(
        chat_id=message.chat.id, filter="administrators"
    )
    admins = []
    for y in x:
        if y.can_manage_voice_chats:
            admins.append(y.user.id)
    return admins


# Video_Stream
async def video_stream(chat_id: int, query, client, message):
    process = await message.reply("Processing!")
    thumb, video, title = await loop.run_in_executor(
        None, youtube_stream, query
    )
    await process.edit("Starting Streaming!")
    await process.delete()
    await Calls.join(chat_id)
    playout = await Calls.start_video(video, repeat=False)
    return await message.reply_photo(
        thumb,
        caption=f"Started Streaming!\n\n**Video🎥** : **__{title}__**\n**Chat : {message.chat.title}**\n**Requested By : {message.from_user.mention}**",
    )
