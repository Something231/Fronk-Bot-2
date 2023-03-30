import os
import discord
from discord.ext import commands
from Keep_Alive import keep_alive
import json
import requests

API_TOKEN = os.getenv('HUGGINGTOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="%", intents=intents)
API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
  
    return json.loads(response.content.decode("utf-8"))
@bot.event
async def on_ready():
  game = discord.Game("Nationstates")
  await bot.change_presence(status=discord.Status.online, activity=game)
  print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
  await ctx.send("Pong")

@bot.command()
async def chat(ctx, *, msg):
  data = query({"inputs": msg})
  generated_text = data[0]['generated_text']
  await ctx.send(generated_text)

@bot.command()
async def trump(ctx):
  response = requests.get('https://api.tronalddump.io/random/quote')
  data = response.json()
  quote = data['value']
  await ctx.send(quote)

keep_alive()
bot.run(os.getenv('TOKEN'))
