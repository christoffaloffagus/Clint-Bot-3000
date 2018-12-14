import discord
from discord.ext import commands
from os import system
from random import randint, choice

class Game:
    def __init__(self, client):
        self.client = client
        self.draw = []

# ------------------------------- COMMANDS ------------------------------- #
# Commands need to have the @commands.command decorator

    @commands.command()
    async def roll(self, dice):
        """\tRoll 100 will roll 1-100, roll 3d10 will roll 1-10 3 times etc..."""
        if 'd' in dice:
            die, value = dice.split('d')
            rolls = []
            for i in range(int(die)):
                rolls.append(f'Dice {i}: {randint(1, int(value))}')
            s = '\n'.join(rolls)
        else:
            s = str(randint(1, int(dice)))

        await self.client.say(s)

    @commands.command(pass_context=True)
    async def enter(self, ctx):
        """\tEnter your name into the draw for things like roulette"""
        author = ctx.message.author

        if author not in self.draw:
            self.draw.append(author)

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        """\tRemove your name from the draw for things like roulette"""
        author = ctx.message.author

        if author in self.draw:
            self.draw.remove(author)

    @commands.command()
    async def clear_draw(self):
        """\t Removes all names from the draw"""
        self.draw = []

    @commands.command()
    async def roulette(self):
        """\tPicks a random name from the draw"""
        person = choice(self.draw)
        if person.nick == None:
            name = person.name
        else:
            name = person.nick

        await self.client.say(name)


def setup(client):
    client.add_cog(Game(client))
