import discord
from discord.ext import commands
from tarot import Deck

client = commands.Bot(command_prefix = '-')
deck = Deck()

@client.event
async def on_ready():
    print('Bot is ready')
    
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
    def check(reaction, user):
        return user == ctx.author
    try:
        deck.shuffle()
        await client.wait_for('reaction_add', timeout = 30.0, check = check)
        await msg.delete()
        msg = await ctx.send("Deck has been shuffled, draw a card now!")
        await msg.add_reaction('☝️')
        try:
            await client.wait_for('reaction_add', timeout = 30.0, check = check)
            await ctx.send('This is your card: ' + deck.draw())
        except:
            await msg.delete()
    except:
        await msg.delete()

    

    

client.run('ODI3ODE1MzczNTA4MTgyMDE2.YGghJQ.y7b2pC2sT5FXL6IKHQeB4Y8ZpqQ')