import discord
from discord.ext import commands
from os import system

class Mod:
    def __init__(self, client):
        self.client = client

# ------------------------------- COMMANDS ------------------------------- #
# Commands need to have the @commands.command decorator

    @commands.command(hidden=True, pass_context=True)
    async def stop(self, ctx):
        channel = ctx.message.channel

        async for message in self.client.logs_from(channel, 1):
            pass
        await self.client.delete_message(message)
        await self.client.logout()


    @commands.command(hidden=True)
    async def load(self, ext):
        try:
            self.client.load_extension(ext)
            print(f'{ext} loaded successfully.')
        except Exception as e:
            print(f'{ext} cannot be loaded. [{e}]')


    @commands.command(hidden=True)
    async def unload(selc, ext):
        try:
            self.client.unload_extension(ext)
            print(f'{ext} unloaded successfully.')
        except Exception as e:
            print(f'{ext} cannot be unloaded. [{e}]')

    @commands.command(hidden=True, pass_context=True)
    async def clear(self, ctx, amount):
        """Clears an amount of messages"""
        channel = ctx.message.channel

        # for i in range(int(amount) + 1):
        #     try:
        messages = []
        async for message in self.client.logs_from(channel, int(amount) + 1):
            messages.append(message)
        for i in range(len(messages)):
            await self.client.delete_message(messages[i])

# -------------------------------- EVENTS -------------------------------- #
# Events do not need a decorator in cogs
    async def on_message_delete(self, msg):
        author = msg.author
        content = msg.content
        channel = msg.channel

        print(f'{author} removed: "{content}" from {channel}')


def setup(client):
    client.add_cog(Mod(client))


#
#
# @client.command(pass_context=True)
# async def clear_all(ctx):
#     channel = ctx.message.channel
#     count = 0
#
#     while True:
#         messages = []
#         async for message in client.logs_from(channel, 100):
#             messages.append(message)
#         length = len(messages)
#
#         if length == 1:
#             await client.delete_message(messages[0])
#         elif length > 100:
#             print(f'ERROR: Messages had {length} messages which is over the 100 limit')
#             messages = messages[:100]
#         await client.delete_messages(messages)
#
#         if length == 0:
#             break
#         else:
#             print(length, 'messages being deleted')
#             count += length
#     print('Total messages deleted:', count)
#
#
# @client.command()
# async def spam(*args):
#     amount = int(args[0])
#     if len(args) > 1:
#         time = float(args[1])
#     else:
#         time = 1
#     for i in range(int(amount)):
#         await client.say('Spam!')
#         await asyncio.sleep(float(time))
#
#
# @client.command()
# async def list_ch():
#     s = '\n'.join([ch for ch in all_channels])
#     await client.say(s)
#
#
# @client.command()
# async def tell(*args):
#         room = args[0]
#         text = ' '.join(args[1:])
#
#         await client.send_message(all_channels[room], text)
#
#
# @client.command()
# async def bot_game(*args):
#     game = discord.Game(name=' '.join(args))
#     await client.change_presence(game=game)



# class Fun:
#     def __init__(self, client):
#         self.client = client
#
#     @commands.commands()
#     async def
