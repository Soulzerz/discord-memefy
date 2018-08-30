import discord
import os
import requests
from stay_alive import staying_alive
from dotenv import load_dotenv
import factory as factory
import core

load_dotenv('./.env')

client = factory.Discord(client=discord.Client()).client

memes_requested = requests.get('https://api.imgflip.com/get_memes').json().get('data')

@client.event
async def on_ready():
    await core.greeter(client, discord.utils.get(client.get_all_channels(), name = 'general'), core.message_generator())

@client.event
async def on_message(message):
    if message.author != client.user:
        memes = filter(lambda x: x if x['name'].lower() in message.content.lower() else None, memes_requested['memes'])
        for meme in memes:
            await client.send_message(message.channel,meme['url'])


staying_alive()
discord_token = os.getenv('DISCORD_BOT_TOKEN')
client.run(discord_token)