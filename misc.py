from youtubesearchpython import VideosSearch
import pafy

#Pafy

def url_stream(url: str):
    video = pafy.new(url)
    videos = video.getbest().url
    return videos
# Youtube

def youtube(query: str):
    search = VideosSearch(query, limit = 1).result()
    thumb = search["result"][0]["thumbnails"][0]["url"].split("?")[0]
    link = search["result"][0]["link"]
    title = search["result"][0]["title"]
    video = url_stream(link)
    return thumb, video, title
#User Input

async def user_input(input):
    """ retrieve user input """
    if ' ' in input or '\n' in input:
       return str(input.split(maxsplit=1)[1].strip())
    return ''

# Help

HELP = """** Here is a list of commands for Video Streaming Bot**
/vplay - To Stream a Video in Group
/vstop - To Stop a Video Stream
/vpause - To Pause a Video Stream
/vresume - To Resume Video Stream
/vskip - To Skip The Current Playing Video
/repo - To Get The Repo
/help , /start - To Get Welcome Menu and Commands (works in private)
/alive - To Check If The Bot Is Alive"""