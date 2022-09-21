from random import randrange
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    intents = intents # Set up basic permissions
)

bot.author_id = 688419703495983145  # Change to your discord id

@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier

@bot.event
async def on_message(message):
    if message.content == "Salut tout le monde" :
        channel = message.channel
        user = message.author
        returnMessage = "Salut tout seul"
        await channel.send(returnMessage)
        await channel.send(message.author.mention)
    await bot.process_commands(message)

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

# Send back the username
@bot.command(name="name")
async def name(ctx):
    await ctx.send(ctx.author)

# Send back a random number between 1 & 6
@bot.command(name="d6")
async def d6(ctx):
    n = randrange(1, 7, 1)
    await ctx.send(n)

@bot.command(name="admin")
async def admin(ctx):
    t = discord.utils.get(ctx.guild.roles.name, name="admin")
    await ctx.send(t)

token = "MTAyMjE5Mjk5MDkwNDY0NzY5MQ.GrhVxn.52M0h6YOiJasJVC3Dpuv2-7cLkJMqySCS_k-jw"
bot.run(token)  # Starts the bot