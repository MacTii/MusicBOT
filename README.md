# Discord music-bot

A simple discord bot that handles messages from the client. The client sends command and the bot find url of music and starts it.

## Important python packages

- discord
- dotenv
- youtube_dl
- ffmpeg-python
- PyNaCl

## How to setup Discord Music Bot

1. Copy paste this link [Discord Developer Portal](https://discord.com/developers/applications) (it will direct you to create new application in this case bot)
    - click *New Application*
    - setup your music bot
    - **copy bot token** (important in next steps)
    - add bot to your server
2. Download project from repository:
    - copy repo using git commands **git clone https://github.com/MacTii/music-bot.git**
    - download it as a ZIP
3. Create virtual environment in your project, use command e.g. *python -m venv venv*
4. Install all packages using command **pip** e.g. *pip install discord*
5. Create **.env** file in HOME_PROJECT directory e.g. *HOME_PROJECT/.env*
    - setup your token for bot and channel id
6. Start script *main.py*
    - if it's not working try to install *https://ffmpeg.org/download.html*
    - get **ffmpeg.exe** file and put it in *HOME_PROJECT/venv/Scripts*
7. Join voice channel
8. Write the necessary commands to communicate with the bot
    - type in discord channel **$join** (bot will join your voice channel)
    - type $play MUSIC_URL e.g. *$play https://www.youtube.com/watch?v=UT8cmozrUFw* (bot will play music)
    - u can pause or resume music bot if u want typing **resume** or **pause**
    - u can disconnect bot typing **disconnect**
