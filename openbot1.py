import discord
import os
from ollama import chat

# MODELS LIST
MODELS = """
Available Models:
- deepseek-r1:8b
- gemma:2b
- gemma2
- gemma3:1b / 4b
- llama3.1
- llama3.2:3b
- llava
- phi3:3.8b
- qwen2.5:7b / 0.5b / 1.5b / 3b
- smollm2
- tinyllama
"""
#INSTALL THESE MODELS AND OLLAMA TO USE
print(MODELS)
model = input("Which model do you want to use?\n").strip()

# Discord intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Signed in as: {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    content = message.content.strip()
    print(f"{message.author}: {content}")

    if content.lower().startswith('merhaba'):
        await message.channel.send("Selam!")
        return

    if content.lower().startswith('bye'):
        await message.channel.send("\U0001f642")
        return

    try:
        response = chat(
            model=model,
            messages=[{"role": "user", "content": "Adın {client.user}. İnsanlara yardımcı olan bir neşeli botsun."}]
        )
        await message.channel.send(response["message"]["content"])
    except Exception as e:
        await message.channel.send("❌ Bir hata oluştu: " + str(e))

# Use environment variable for token (recommended)

client.run("ENTER TOKEN")
