from pyrogram import Client
from pytgcalls import GroupCallFactory as gcf

import config

# Plugins
vsb = dict(root="VideoxD/Handlers")

# Pyro Client
app = Client(
    config.STRING_SESSION,
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    plugins=vsb,
)
bot = Client(
    "bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    plugins=vsb,
)


# pytgcalls

Calls = gcf(app).get_group_call()


# Help Text

HELP = """** Here is a list of commands for Video Streaming Bot**
/vplay - To Stream a Video in Group ( Youtube Search, Youtube Link)
/vstop - To Stop a Video Stream
/vpause - To Pause a Video Stream
/vresume - To Resume Video Stream
/vskip - To Skip The Current Playing Video
/repo - To Get The Repo
/help , /start - To Get Welcome Menu and Commands (works in private)
/alive - To Check If The Bot Is Alive"""
