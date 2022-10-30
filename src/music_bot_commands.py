import discord
import youtube_dl


def bot_commands(bot):
    @bot.command()
    async def play(ctx, url):
        ctx.voice_client.stop()

        FFMPEG_OPTIONS = {
            "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5",
            "options": "-vn",
        }
        YDL_OPTIONS = {"format": "bestaudio"}

        vc = ctx.voice_client

        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
            url2 = info["formats"][0]["url"]
            source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            vc.play(source)

    @bot.command()
    async def join(ctx):
        channel = ctx.author.voice.channel
        await channel.connect()

    @bot.command()
    async def disconnect(ctx):
        await ctx.voice_client.disconnect()

    @bot.command()
    async def pause(ctx):
        await ctx.voice_client.pause()
        await ctx.send("paused ⏸︎")

    @bot.command()
    async def resume(ctx):
        await ctx.voice_client.resume()
        await ctx.send("resume ⏵︎")
