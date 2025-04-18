import discord
import asyncio
import threading

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
message_queue = asyncio.Queue()
target_channel = None

@client.event
async def on_ready():
    print(f"Giriş yapıldı: {client.user}")
    print("Mesaj göndermek için yaz:")

    # Terminalden giriş için ayrı thread
    threading.Thread(target=read_terminal_input, daemon=True).start()

    # Kullanıcının mesaj gönderebileceği ilk metin kanalını al
    global target_channel
    for guild in client.guilds:
        for channel in guild.text_channels:
            if channel.permissions_for(guild.me).send_messages:
                target_channel = channel
                break
        if target_channel:
            break

    if target_channel is None:
        print("Mesaj gönderebileceğim bir kanal bulunamadı.")
        await client.close()
        return

    # Kuyruğu dinle ve mesajları kanala gönder
    await send_messages_from_queue()

def read_terminal_input():
    while True:
        msg = input("> ")
        asyncio.run_coroutine_threadsafe(message_queue.put(msg), client.loop)

async def send_messages_from_queue():
    while True:
        msg = await message_queue.get()
        if msg.lower() == "exit":
            await client.close()
            break
        if target_channel:
            await target_channel.send(msg)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    print(f"{message.author}: {message.content}")



client.run("ENTER TOKEN")

