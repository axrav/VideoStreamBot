from pytgcalls import GroupCallFactory as gcf
from pyrogram import Client, filters, idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
import config
from misc import youtube, user_input, HELP
import asyncio
# PYROGRAM CLIENT

app = Client(config.STRING_SESSION, api_id = config.API_ID, api_hash = config.API_HASH)
bot = Client("bot", api_id = config.API_ID, api_hash = config.API_HASH, bot_token = config.BOT_TOKEN)
que = asyncio.Queue()
# PYTGCALLS CLIENT
number = 0
Calls = gcf(app).get_group_call()

loop = asyncio.get_event_loop()

@bot.on_message(filters.command("alive"))
async def startxd(client, message):
    await message.reply("Yes I am Alive!,Who Cares About Someone Else!")
@bot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(client, message):
    sender_mention = message.from_user.mention
    await message.reply(f"Hi! {sender_mention}, This is a video streaming bot. Here is a link to my source code!", reply_markup = InlineKeyboardMarkup(
        [
            [
            InlineKeyboardButton(
                    text = "Repository",
                    url = "https://github.com/VegetaxD/VideoStreamBot"                  
                )                
            ],
            [
            InlineKeyboardButton(
                    text = "Commands",
                    callback_data = "commands"                  
                )                
            ]
        ]
                )
                        )
@bot.on_message(filters.command("vplay") & filters.chat(config.VIDEO_CHAT_ID)) 
async def stream(client, message):
    user_str = await user_input(message.text)
    if not user_str:
        return await message.reply("Please give a youtube link/keyword to stream!")
    if Calls.is_running:
        next_vid = (user_str)
        await que.put(next_vid)
        global number
        number += 1
        return await message.reply(f"Added **Video🎥** : **__{next_vid}__** To Queue!\n\n**Queued at #{number}**")
    process = await message.reply("Processing!")    
    try:
        YouTube = await loop.run_in_executor(None, youtube, user_str)
        video = YouTube[1]
        thumb = YouTube[0]
        title = YouTube[2]
        await process.edit("Starting Streaming!")        
        await process.delete()
        await Calls.join(message.chat.id)
        playout = await Calls.start_video(video, repeat=False)
        return await message.reply_photo(thumb, caption = f"Started Streaming!\n\n**Video🎥** : **__{title}__**\n**Chat : {message.chat.title}**\n**Requested By : {message.from_user.mention}**")
    except Exception as e:
        return await message.reply(e)
@Calls.on_video_playout_ended
async def media_ended(_, __):
    if que.empty():
        await bot.send_message(config.VIDEO_CHAT_ID, "No More Videos In Queue!\n\nLeaving Video Chat! xD")
        return await Calls.stop()
    else:
        process = await bot.send_message(config.VIDEO_CHAT_ID,"Processing!")
        stuff = await que.get()
    try:
        YouTube = await loop.run_in_executor(None, youtube, stuff)
        video = YouTube[1]
        thumb = YouTube[0]
        title = YouTube[2]
        await process.delete()
        await Calls.start_video(video, repeat=False)
        global number
        number -= 1
        ctitle = ((await bot.get_chat(config.VIDEO_CHAT_ID)).title)
        return await bot.send_photo(config.VIDEO_CHAT_ID, photo = thumb, caption = f"Started Streaming!\n\n**Video🎥** : **__{title}__**\n**Chat : {ctitle}**")
    except Exception as e:
        return await bot.send_message(config.VIDEO_CHAT_ID, e)   
        
@bot.on_message(filters.command("repo") ) 
async def repo(client, message):
    return await message.reply("Here is the Repository!", reply_markup = InlineKeyboardMarkup(
        [
            [
            InlineKeyboardButton(
                    text = "Repository",
                    url = "https://github.com/VegetaxD/VideoStreamBot"
                )                
            ]
        ]
                )
                        )
    
@bot.on_message(filters.command("vstop") & filters.chat(config.VIDEO_CHAT_ID) ) 
async def pause(client, message):
    if not Calls.is_running:
        return await message.reply("No Stream Going On!")
    global number
    x = (await bot.get_chat_members(chat_id = message.chat.id, filter = "administrators"))
    admins = []
    for y in x:
        if y.can_manage_voice_chats:
            admins.append(y.user.id)
    if message.from_user.id not in admins:
        return await message.reply("You Dont Have Sufficient Permissions!, Make Sure You Have Manage Video Chats")
    await Calls.stop()
    number = 0
    que._queue.clear()
    return await message.reply("The Video Has Been Stopped Successfully!")
    
@bot.on_message(filters.command("vpause") & filters.chat(config.VIDEO_CHAT_ID) ) 
async def pause(client, message):
    x = (await bot.get_chat_members(chat_id = message.chat.id, filter = "administrators"))
    admins = []
    for y in x:
        if y.can_manage_voice_chats:
            admins.append(y.user.id)
    if message.from_user.id not in admins:
        return await message.reply("You Dont Have Sufficient Permissions!, Make Sure You Have Manage Video Chats")
    await Calls.set_pause(True)
    return await message.reply("The Video Has Been Paused ⏸ Successfully!")
    
@bot.on_message(filters.command("vresume") & filters.chat(config.VIDEO_CHAT_ID)) 
async def resume(client, message):
    x = (await bot.get_chat_members(chat_id = message.chat.id, filter = "administrators"))
    admins = []
    for y in x:
        if y.can_manage_voice_chats:
            admins.append(y.user.id)
    if message.from_user.id not in admins:
        return await message.reply("You Dont Have Sufficient Permissions!, Make Sure You Have Manage Video Chats")
    await Calls.set_pause(False)
    return await message.reply("The Video Has Been Resumed ▶️ Successfully!")

@bot.on_message(filters.command("vskip") & filters.chat(config.VIDEO_CHAT_ID)) 
async def skip(client, message):
    global number
    x = (await bot.get_chat_members(chat_id = message.chat.id, filter = "administrators"))
    admins = []
    for y in x:
        if y.can_manage_voice_chats:
            admins.append(y.user.id)
    if message.from_user.id not in admins:
        return await message.reply("You Dont Have Sufficient Permissions!, Make Sure You Have Manage Video Chats")
    if que.empty():
        await message.reply("No More Videos In Queue!\n\nLeaving Video Chat! xD")
        return await Calls.stop()
    else:
        process = await message.reply("Processing!")
        stuff = await que.get()
    try:
        YouTube = await loop.run_in_executor(None, youtube, stuff)
        video = YouTube[1]
        thumb = YouTube[0]
        title = YouTube[2]
        await process.delete()
        await Calls.start_video(video, repeat=False)
        number -= 1
        return await message.reply_photo(photo = thumb, caption = f"Started Streaming!\n\n**Video🎥** : **__{title}__**\n**Chat : {message.chat.title}**\n**Requested By : {message.from_user.mention}**")
    except Exception as e:
        return await message.reply(e)
@bot.on_callback_query(filters.regex("commands"))
async def command_(_, cb):
    await bot.send_message(cb.message.chat.id, text= HELP)
    await cb.message.delete()    
# Startup    
async def init():
    
    await app.start()
    print("User Client Started!")
    await bot.start()
    print("Bot Client Started!")
    await idle()
if __name__ == '__main__':
    loop.run_until_complete(init())

# To Do
# Multiple Chats (Needs High Specs)
# Add Local Telegram Video Play
# Interactive UI
# current/Queue 
