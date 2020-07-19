import discord
import asyncio
from os import system
import time
import os

client = discord.Client()

@client.event
async def on_ready():
    print("파이브엠 서버 리붓봇이 가동되었습니다!")
    @client.event
    async def on_message(message):리붓중. . . . 
        channel = message.channel.id
        id = message.author.id
        if message.content.startswith("/리붓"):
                await message.channel.send("리붓을 시작합니다. . .")
                system("taskkill /f /im cmd.exe")
                system("taskkill /f /im FXServer.exe")
                time.sleep(1)
                system("start Start_Server.cmd")
                time.sleep(20)
                await message.channel.send("엘로스서버의 리붓이 완료되었습니다!")
access_token = os.environ["BOT_TOKEN"]
client.run("access_token")
