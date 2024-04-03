import discord
from discord import app_commands
from discord.ext import commands
import responses

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
TOKEN = ''

async def send_message(message, user_message, is_private):
    try:
        response = responses.hans(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    username = str(message.author)
    user_message = str(message.content)
    channel = str(message.channel)
    if user_message[0] == "?":
        user_message = user_message[1:]
        await send_message(message, user_message, is_private=True)
    else:
        await send_message(message, user_message, is_private=False)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print("bot is up and running")

@bot.tree.command(name="hello", description="something")
async def hello(interaction: discord.Interaction):
    bot_latency = round(bot.latency * 1000)
    await interaction.response.send_message("hello man!")

@bot.tree.command(name="ask", description="ask")
async def hello(interaction: discord.Interaction):
    bot_latency = round(bot.latency * 1000)
    await interaction.response.send_message("whats your question?")

@bot.tree.command(name="help", description="all commands and explanations")
async def hello(interaction: discord.Interaction):
    bot_latency = round(bot.latency * 1000)
    await interaction.response.send_message("type this '?' in front of any command for personal messaging")

bot.run(TOKEN)