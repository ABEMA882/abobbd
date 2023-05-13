import discord
import random

intents = discord.Intents().all()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("hello")
    elif message.content.startswith('bye'):
        await message.channel.send("Ты как бы чел...")
    elif message.content.startswith('Тупой Бот'):
        await message.channel.send("а ты лох")
    elif message.content.startswith('Подбрось монетку'):
        rand_num = random.randint(0, 1)
        result = "Орел" if rand_num == 0 else "Решка"
        await message.channel.send(f"Результат: {result}")
    elif message.content.startswith('Hi!'):
        await message.channel.send("Сюда ботов")
    else:
        await message.channel.send(message.content)

client.run("MTEwNDQwNTk2NDgwNDg1Mzg4MQ.G5pEIZ.z0leWcCNqGRKp2u56PAWcgr8SoFJsEmqmjgrMA")
