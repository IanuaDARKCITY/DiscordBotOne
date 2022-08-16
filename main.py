import discord
import os
from dotenv import load_dotenv
from neuralintents import GenericAssistant

import nltk
nltk.download('omw-1.4')

# Creating the chatbot here
chatbot = GenericAssistant('discordIntents.json')
chatbot.train_model()
chatbot.save_model()

print("Client is now running")

#Getting the token and setting it all up

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('TOKEN')

# Message function

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$ianua"):
        response = chatbot.request(message.content[7:])
        await message.channel.send(response)


client.run(TOKEN) #Insert token here, allows it to run in the end

