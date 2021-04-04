import discord
from discord.ext import commands
from tarot import Deck

client = commands.Bot(command_prefix = '-')
deck = Deck()

@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_reaction_add(reaction, user):
    if reaction.emoji == '🔄' and user!=client:
        deck.shuffle()
        msg = await channel.send("Deck has been shuffled, draw a card now!")
        await msg.add_reaction('☝️')

@client.command()
async def info(ctx):
    embed = discord.Embed(title="Tarot Bot", description="Draw a card to foreseen your future")
    embed.set_author(name='Mitsukii-#8263', url='https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO')
    await ctx.send(ctx.message.channel, embed=embed)

@client.command()
async def tarot(ctx):
    
    embed = discord.Embed(title="Ask the deck a question before drawing the card :pray:", description="Click the shuffle button to shuffle the deck!")
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🔄')

    

client.run('ODI3ODE1MzczNTA4MTgyMDE2.YGghJQ.H3SLwOrGyDsBqYu_KVfC87Weuu4')