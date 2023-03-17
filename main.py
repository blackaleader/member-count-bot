import discord
from discord.ext import commands

from discord.ext import tasks, commands
from discord.ext.commands import Bot
from discord.ext.commands import Context



Token = ("your token")
server = 000000000000000

intents = discord.Intents.all()
intents.message_content = True
client = commands.Bot(command_prefix = '.', intents=intents)



@client.event
async def on_ready():
    print(f'Logged in as {client.user.name} ({client.user.id})')
    update_member_count.start()

@tasks.loop(seconds=60)
async def update_member_count():
    print("its alive")
    guild = client.get_guild(server)
    member_count = len(guild.members)
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{member_count} Members"))

@client.event
async def on_message(msg):
    if msg.author.id != 1072917702487846912 :
        if msg.channel.id == 1072641153419202560 : 
            await msg.delete()
            await msg.channel.send("SENT !")
            channel = await client.fetch_channel(1072641195693588610)
            await channel.send(msg.content)

client.run(Token)
