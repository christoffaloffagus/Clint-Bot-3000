import discord
from discord.ext import commands
from os import system
from random import choice

class Fun:
    def __init__(self, client):
        self.client = client
        self.sermons = ['And yay Sam did telleth me, thy marking be to harsh.\nAnd to he I doth say, fuck off.']

# ------------------------------- COMMANDS ------------------------------- #
# Commands need to have the @commands.command decorator

    @commands.command()
    async def preach(self):
        """\tQuotes scripture from the holy book of the Clint"""
        await self.client.say(choice(self.sermons))


def setup(client):
    client.add_cog(Fun(client))
