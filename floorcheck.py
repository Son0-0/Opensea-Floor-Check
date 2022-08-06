import requests
import json
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from bs4 import BeautifulSoup as soup
import module.discord_webhook as discord_webhook, module.bithumb as bithumb, module.opensea_add as opensea_add

load_dotenv()

Client = discord.Client()
bot_prefix = "!"
client = commands.Bot(command_prefix=bot_prefix)
footer_img = "https://storage.googleapis.com/opensea-static/Logomark/Logomark-White.png"

TOKEN = os.environ.get('TOKEN')

@client.event
async def on_ready():
    global TOKEN

@client.event
async def on_message(message):      
    if message.content.startswith('!floor'):
      messageSplit = message.content.split(' ')
      nft_name = str(messageSplit[1])
      channel = message.channel
      
      eth, klay = bithumb.extract()
      
      with open('opensea.json', 'r') as f:
        site = json.load(f)
      
      try:  
        embed = discord_webhook.parseEmbed(site[nft_name], eth, klay)
        await channel.send(embed=embed)
      except:
        embed = discord.Embed(title="**등록되지 않은 사이트입니다.**", description="", color=0x000000)
        embed.set_thumbnail(url=footer_img)
        embed.set_footer(text="Powered By Son0-0", icon_url=footer_img)
        await channel.send(embed=embed)
    
    if message.content.startswith('!fadd'):
      messageSplit = message.content.split(' ')
      nickname = str(messageSplit[1])
      url = str(messageSplit[2])
      channel = message.channel
      
      tf = opensea_add.addSite(nickname, url)
      
      if tf == True:
        embed = discord.Embed(title="**사이트가 등록되었습니다.**", description="", color=0x000000)
        embed.set_thumbnail(url=footer_img)
        embed.set_footer(text="Powered By Son0-0", icon_url=footer_img)
        await channel.send(embed=embed)
      else:
        embed = discord.Embed(title="**사이트 등록에 실패하였습니다!**", description="", color=0x000000)
        embed.set_thumbnail(url=footer_img)
        embed.set_footer(text="Powered By Son0-0", icon_url=footer_img)
        await channel.send(embed=embed)

if __name__ == '__main__':
  while True:
    if len(TOKEN) == 0:
      TOKEN = input("Type your discord bot token: ")
    else:
      print("[OPENSEA FLOOR BOT RUNNING...]")
      break
    
  client.run(TOKEN)