import discord
from random import choice 

async def greeter(client, channel, message):
    if(channel):
       await client.send_message(discord.Object(id=channel.id), message)


def message_generator():
    message_list = ['Oh, boi. Here we go.','Let\'s do this guys', 'INITIALIZING SAVAGE PROTOCOL', 'Did you missed me?']
    return choice(message_list)

