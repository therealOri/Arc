import discord
from discord.utils import get
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style
import datetime
import asyncio


BOT_Prefix=("a.", "A.")
client = commands.Bot(command_prefix=BOT_Prefix)
client.remove_command("help")


@client.command()
async def help(ctx):
    author = ctx.message.author


    helpembed = discord.Embed(
        colour=discord.Color.blue(),
        timestamp=datetime.datetime.utcnow()
    )
    helpembed.set_author(name="Help")
    helpembed.add_field(name="a.ping", value = "Standard ping pong command", inline=False)
    helpembed.add_field(name="a.create <channel-name>", value = "Creates a private channel for you.", inline=False)
    helpembed.add_field(name="a.del_chanl <channel-name>", value = "Deletes a channel with the specified name.", inline=False)
    helpembed.add_field(name="a.invite", value = "Gives you my invite link so you can add me to your server.", inline=False)
    helpembed.add_field(name="a.info", value = "Gives you some info about the bots developer.", inline=False)
    await ctx.send(embed=helpembed)


print(
    Fore.WHITE + "[" + Fore.BLUE + '+' + Fore.WHITE + "]" + Fore.BLUE + " attempting to establish connection to the client")


@client.event
async def on_ready():
    watching = discord.Streaming(type=1, url="https://twitch.tv/Monstercat",
                                 name=f"a.help | in {len(client.guilds)} guilds!")
    await client.change_presence(status=discord.Status.online, activity=watching)
    print(
        Fore.WHITE + "[" + Fore.GREEN + '+' + Fore.WHITE + "]" + Fore.GREEN + " connection established, logged in as: " + client.user.name)


@client.event
async def on_guild_join(guild):
    print(f"I was invited to and have joined {guild}!")


@client.command()
async def ping(ctx):
    await ctx.send(f"pong! connection speed is {round(client.latency * 1000)}ms")


@client.command()
async def info(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour=discord.Color.blue(),
        timestamp=datetime.datetime.utcnow()
    )
    embed.set_author(name="Info")
    embed.add_field(name="Creator/Developer:", value='Ori#6338', inline=True)
    embed.add_field(name="Website:", value='[omintyd.tk](https://omintyd.tk/)', inline=True)
    embed.add_field(name="Coding Language:", value='Python3', inline=False)
    embed.add_field(name="Version:", value='1.0.3', inline=True)
    await ctx.send(embed=embed)



#https://discordapp.com/oauth2/authorize?client_id=771097019397701632&scope=bot&permissions=8"
@client.command()
async def invite(ctx):
    author = ctx.message.author


    invembed = discord.Embed(
        colour=discord.Color.blue(),
        timestamp=datetime.datetime.utcnow()
    )
    invembed.set_author(name="Add me")
    invembed.add_field(name="My Invite Link", value = "[Invite](https://discordapp.com/oauth2/authorize?client_id=771097019397701632&scope=bot&permissions=8)", inline=False)
    await ctx.send(embed=invembed)
        
        
        
        
@client.command()
async def create(ctx, *, arg, ):
    if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.manage_channels: #perms can be changed
        guild = ctx.guild
        member = ctx.author
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True),
            member: discord.PermissionOverwrite(read_messages=True, send_messages=True, manage_permissions=True)
            }
        channel = await guild.create_text_channel(arg, overwrites=overwrites)
        embed = discord.Embed(title="Success!", description=f"The channel `{arg}` has been succesfully created! Go check it out!", color=discord.Color.green())
        await ctx.send(embed=embed)
        await asyncio.sleep(20)
        await ctx.message.delete()
    else:
        embed = discord.Embed(title="Permission Denied.", description="You don't have permission to use this command.", color=discord.Color.red())
        await ctx.send(embed=embed)


@client.command()
async def del_chanl(ctx, channel_name):
    guild = ctx.guild

    if ctx.message.author.guild_permissions.administrator or ctx.message.author.guild_permissions.manage_channels: #perms can be changed
        existing_channel = discord.utils.get(guild.channels, name=channel_name)
        if existing_channel is not None:
            await existing_channel.delete()
            embed = discord.Embed(title="Success.", description=f"The channel `{channel_name}` has been succesfully deleted!", color=discord.Color.green())
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="Error!.", description=f"The channel `{channel_name}` could not be found or doesn't exist.", color=discord.Color.red())
            await ctx.send(embed=embed)
        await asyncio.sleep(20)
        await ctx.message.delete()

        
        
client.run('BotTokenHere')
