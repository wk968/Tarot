import discord
from discord.ext import commands
from tarot import Deck,Card

client = commands.Bot(command_prefix = '-')


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
    deck = Deck()
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
        embed.set_thumbnail(url="https://i0.wp.com/www.quickcardreading.com/wp-content/uploads/2013/03/card-back.jpg")
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('☝️')
        try:
            await client.wait_for('reaction_add', timeout = 30.0, check = check)
            
            await msg.delete()
            card = str(deck.draw())
            embed = discord.Embed(title="You got " + card)
            embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")

            await ctx.send(embed=embed)
        except:
            await msg.delete()
    except:
        await msg.delete()

client.run('')