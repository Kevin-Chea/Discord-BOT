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

@bot.command()
async def pong(ctx):
    await ctx.send('pong')

token = "MTAyMjE5Mjk5MDkwNDY0NzY5MQ.GuFQr-.VTAOJYsZcSQRjsPP4hkOC08Nhagzl_0ZJ95-Ys"
bot.run(token)  # Starts the bot