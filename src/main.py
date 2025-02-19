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
async def admin(ctx, nickname):
    t = discord.utils.get(ctx.guild.roles, name="admin")
    if t == None:
        await ctx.guild.create_role(name="admin")
    # Admin permissions  
    role = discord.utils.get(ctx.guild.roles, name="admin")
    perms = discord.Permissions(manage_channels=True, kick_members=True, ban_members=True)    
    await role.edit(reason = None, colour = discord.Colour.red(), permissions=perms)
    user = discord.utils.get(ctx.guild.members, nick=nickname)
    if (user != None):
        await user.add_roles(role)

@bot.command(name="ban")
async def ban(ctx, nickname):
    user = discord.utils.get(ctx.guild.members, nick=nickname)
    reason = "Ban via le bot. Paf !"
    await user.ban(user, reason=reason)

@bot.command(name="count")
async def count(ctx):
    online = []
    idle = []
    dnd = []
    offline = []
    invisible = []
    for member in ctx.guild.members:
        
        if member.status == discord.Status.online:
            online.append(member)
        if member.status == discord.Status.idle:
            idle.append(member)
        if member.status == discord.Status.dnd:
            dnd.append(member)
        if member.status == discord.Status.offline:
            offline.append(member)
        if member.status == discord.Status.invisible:
            invisible.append(member)
    
    await ctx.send("Members online : " + str(len(online)))
    for user in online:
        await ctx.send(user)
    await ctx.send("Members idle : "  + str(len(idle)))
    for user in idle:
        await ctx.send(user)
    await ctx.send("Members do not disturb : "  + str(len(dnd)))
    for user in idle:
        await ctx.send(user)
    await ctx.send("Members offline : "  + str(len(offline)))
    for user in offline:
        await ctx.send(user)
    await ctx.send("Members invisible : "  + str(len(invisible)))
    for user in invisible:
        await ctx.send(user)

token = ""
bot.run(token)  # Starts the bot