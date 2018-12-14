import discord
from discord.ext import commands
import asyncio
from itertools import cycle
import os

client = commands.Bot(command_prefix='++')
extensions = ['Mod', 'Game', 'Fun']

all_channels = None
statuses = ['you', 'with his penis', 'with mind powers', 'with 3 dead prostitutes']
STATUS_CHANGE_FREQUENCY = 300 # time in seconds between status changes

# -------------------------------- EVENTS -------------------------------- #
@client.event
async def on_ready():
    global all_channels
    print('Bot is ready.')
    all_channels = dict(map(lambda c: (c.name.replace(' ', '-'), c), client.get_all_channels()))

@client.event
async def on_message(msg):
    author = msg.author
    channel = msg.channel
    content = msg.content

    print(f'{author}: {content}')
    await client.process_commands(msg)

# --------------------------- ASYNCIO FUNCTIONS --------------------------- #
async def change_status():
    await client.wait_until_ready()
    msgs = cycle(statuses)

    while not client.is_closed:
        current_status = next(msgs)
        await client.change_presence(game=discord.Game(name=current_status))
        await asyncio.sleep(STATUS_CHANGE_FREQUENCY)


if __name__ == '__main__':
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'{extension} cannot be loaded: {e}')

    client.loop.create_task(change_status())
    client.run(os.getenv('TOKEN-Clint'))
