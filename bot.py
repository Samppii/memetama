import discord
import requests
import json
import os 
from dotenv import load_dotenv

load_dotenv() #This is to load the .env file that we created in the root directory of the project

Discord_Token = os.getenv("DISCORD_TOKEN") #This is the token of the bot that we created in the discord developer portal


def get_meme(): #This function will return a random meme from the meme-api
    response = requests.get("https://meme-api.com/gimme")
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client): #Creating this class by extending from the base class discord.Client so it already has multiple that we can use for example: on_ready and on_message
  async def on_ready(self): #This function is called when the bot is ready to start being used
    print('Logged on as {0}!'.format(self.user))

  async def on_message(self, message): #This function is called when the bot receives a message in any of the servers it is in
    if message.author == self.user: #This is to make sure the bot doesn't respond to itself and create an infinite loop
        return
    if message.content.startswith('$meme'): #This is the command that the bot will respond to when it is
        await message.channel.send(get_meme())
    

intents = discord.Intents.default() #This is to enable the message_content intent by default
intents.message_content = True #This is to enable the message_content intent by default

client = MyClient(intents=intents) #Creating an instance of the MyClient class that we created above
client.run(Discord_Token) #This is the token of the bot that we created in the discord developer portal
