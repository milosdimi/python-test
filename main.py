import discord
from discord import client
from discord import channel
from dotenv import load_dotenv
import os   
from discord.ext import commands
import logging


handler = logging.FileHandler(filename="discordbot.log", mode='w', encoding='utf-8')


load_dotenv()
token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    
@bot.command()
async def hallo(ctx):
    await ctx.send(f"Grüß dich, {ctx.author.mention}! Hallo!")
    
@bot.command()
async def msg(ctx, arg):
    await ctx.send(f"Test command received with argument: {arg}")

new_role_name = "hammerTyp"

@bot.command()
async def assing(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role_name)
    if role:
        await ctx.author.add_roles(role)
        await ctx.send(f"Deine Rolle wurde erfolgreich zugewiesen, {ctx.author.mention}!")
        return
    await ctx.send(f"Die Rolle wurde nicht gefunden.")
    
@bot.command()
async def remove_role(ctx):
    role = discord.utils.get(ctx.guild.roles, name=new_role_name)
    if role:
        await ctx.author.remove_roles(role)
        await ctx.send(f"Deine Rolle wurde erfolgreich entfernt, {ctx.author.mention}!")
        return
    await ctx.send(f"Die Rolle wurde nicht gefunden.")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if 'banana' in message.content.lower():
        await message.delete()
        channel = message.channel
        await channel.send(f'Hello {message.author}, I see you mentioned banana! 🍌')
    
    await bot.process_commands(message)
        
bot.run(token, log_handler=handler, log_level=logging.DEBUG)    