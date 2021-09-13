<h1 align= center>Video Stream Bot </h1>
<h3 align = center> A Video Streaming Telegram Bot written in Python using Pyrogram and PyTgcalls </h3>

<p align="center">
<a href="https://python.org"><img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python"></a>
<br>
    <img src="https://img.shields.io/github/license/VegetaxD/VideoStreamBot?style=for-the-badge" alt="LICENSE">
    <img src="https://img.shields.io/github/contributors/VegetaxD/VideoStreamBot?style=for-the-badge" alt="Contributors">
    <img src="https://img.shields.io/github/repo-size/VegetaxD/VideoStreamBot?style=for-the-badge" alt="Repository Size"> <br>
    <img src="https://img.shields.io/github/forks/VegetaxD/VideoStreamBot?style=for-the-badge" alt="Forks">
    <img src="https://img.shields.io/github/stars/VegetaxD/VideoStreamBot?style=for-the-badge" alt="Stars">
    <img src="https://img.shields.io/github/watchers/VegetaxD/VideoStreamBot?style=for-the-badge" alt="Watchers">
    <img src="https://img.shields.io/github/commit-activity/w/VegetaxD/VideoStreamBot?style=for-the-badge" alt="Commit Activity">
</p>
 
## Requirements

- Python 3.9
- Telegram API 
- Telegram Bot Token
- Pyrogram String Session

## Deployment Methods and Sessions.

### Railway 
<p><a href="https://railway.app/new/template?template=https://github.com/VegetaxD/VideoStreamBot&envs=API_ID,API_HASH,STRING_SESSION,BOT_TOKEN,VIDEO_CHAT_ID"><img src="https://img.shields.io/badge/Deploy%20To%20Railway-blueviolet?style=for-the-badge&logo=railway" width="200""/></a></p>

### Heroku 
<p><a href="https://heroku.com/deploy?template=https://github.com/VegetaxD/VideoStreamBot"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a></p>
 
### Generate String Session

<p><a href="https://replit.com/@AaravxD/VsBSession#main.py"><img src="https://img.shields.io/badge/Generate%20On%20Repl-blueviolet?style=for-the-badge&logo=appveyor" width="200""/></a></p> 
 

## Deploy Locally or Server
``` 
vegeta@arch $ git clone https://github.com/VegetaxD/VideoStreamBot
vegeta@arch $ cd VideoStreamBot
vegeta@arch $ pip3 install -U -r requirements.txt
vegeta@arch $ cp sample.env .env
#Fill .env with your values
vegeta@arch $ python3 -m VideoxD
 ```

## Config Vars
1. `API_ID` : Assistant Account Telegram API_ID, get it from my.telegram.org
2. `API_HASH` : Assistant Account Telegram API_HASH, get it from my.telegram.org
3. `BOT_TOKEN` : Your Telegram Bot Token, get it from @Botfather (Make sure Inline is turned On)
4. `SESSION_STRING` : Pyrogram Session String of Assistant Account.
5. `VIDEO_CHAT_ID` : Chat ID where you want bot to stream. (Single Chat Only)
 
### Commands
```
/vplay - To Stream a Video in Group ( Youtube Search/ Youtube Link )

/vstop - To Stop a Video Stream

/vpause - To Pause a Video Stream

/vresume - To Resume Video Stream

/vskip - To Skip The Current Playing Video

/repo - To Get The Repo

/help , /start - To Get Welcome Menu and Commands (works in private)

/alive - To Check If The Bot Is Alive
```
 
## Note
- This is a Dev branch, So you might experience bugs!
- I will try to update it regularly!
- No support Group/Channel for now.
    
### Contact
<p><a href="https://t.me/VegetaxD"><img src="https://img.shields.io/badge/Contact%20Me-blueviolet?style=for-the-badge&logo=telegram" width="80""/></a>
<a href="https://t.me/VideoStreamingxD"><img src="https://img.shields.io/badge/Telegram%20Channel-blueviolet?style=for-the-badge&logo=telegram" width="113""/></a></p> 

## Credits
- [Pyrogram](https://github.com/pyrogram/pyrogram)
- [PyTgCalls](https://github.com/MarshalX/tgcalls)
    
## License
    
```sh
MIT License
VideoStreamBot, Telegram Video Calls Bot
Copyright (c) 2021 Aarav Arora

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
 
 
 
