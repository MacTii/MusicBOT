import discord, os
from discord.ext import commands
import music_bot_commands

def run_music_bot():
    bot = commands.Bot(command_prefix="$", intents=discord.Intents().all())

    @bot.event
    async def on_ready():
        channel = bot.get_channel(int(os.getenv("CHANNEL_ID")))

        await channel.send("Bot is online...")
        print("Logged into server {0.user}".format(bot))
    
    music_bot_commands.bot_commands(bot=bot)

    # Bot run
    bot.run(os.getenv("TOKEN"))
