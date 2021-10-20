#inline search (pyrogram)
from .. import bot
from pyrogram import Client, errors
from youtubesearchpython import VideosSearch
from pyrogram.handlers import InlineQueryHandler
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent
@bot.on_inline_query()
async def search(client, query):
    vegetaxd = []
    string = query.query.lower().strip().rstrip()
    if string == "":
        await client.answer_inline_query(
            query.id,
            results=vegetaxd,
            switch_pm_text=("Search a youtube video"),
            switch_pm_parameter="start",
            cache_time=0
        )
    else:
        videosSearch = VideosSearch(string.lower(), limit=25)
        for xd in videosSearch.result()["result"]:
            vegetaxd.append(
                InlineQueryResultArticle(
                    title=xd["title"],
                    description=("Duration: {} Views: {}").format(
                        xd["duration"],
                        xd["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "https://www.youtube.com/watch?v={}".format(
                            xd["id"]
                        )
                    ),
                    thumb_url=xd["thumbnails"][0]["url"]
                )
            )
        try:
            await query.answer(
                results=vegetaxd,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=vegetaxd,
                cache_time=0,
                switch_pm_text=("No Results"),
                switch_pm_parameter="",
            )


__handlers__ = [
    [
        InlineQueryHandler(search)
    ]
]
