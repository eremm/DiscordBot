import discord
import asyncio
import bot_command as botcmd

if not discord.opus.is_loaded():
    # the 'opus' library here is opus.dll on windows
    # or libopus.so on linux in the current directory
    # you should replace this with the location the
    # opus library is located in and with the proper filename.
    # note that on windows this DLL is automatically provided for you
    discord.opus.load_opus('opus')

client = discord.Client()
client.cmd_list = botcmd.init_commands()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    #we don't want to act on other bots
    if message.author.bot:
        return
    msgCmd = botcmd.find_command(message, client)
    if msgCmd:
        await msgCmd.execute(message, '', message.author, client)

with open('token.txt', 'r') as f:
    token = f.read()

client.run(token)
