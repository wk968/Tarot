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

@client.command(pass_context = True)
async def tarot(ctx):
    
    embed = discord.Embed(title="Ask the deck a question before drawing the card :pray:", description="Click the shuffle button to shuffle the deck!")   
    msg = await ctx.send(embed=embed)
    await msg.add_reaction('🔄')
    await ctx.message.delete()
    def check(reaction, user):
        return user == ctx.author
    try:
        
        await client.wait_for('reaction_add', timeout = 30.0, check = check)
        deck.shuffle()
        await msg.delete()
        embed = discord.Embed(title="Deck has been shuffled", description="Draw a card now!")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('☝️')
        try:
            await client.wait_for('reaction_add', timeout = 30.0, check = check)
            embed = discord.Embed(title="This is your card", description=)
            await ctx.send(embed=embed)
        except:
            await msg.delete()
    except:
        await msg.delete()

    

    

client.run('')