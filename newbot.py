import discord

client = discord.Client()





@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("일")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!노예야"):
        await message.channel.send("네")
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")

    if message.content.startswith("/채널메세지"):
        channel = message.content[7:25]
        msg = message.content[26:]
        await client.get_channel(int(channel)).send(msg)








client.run("NjI1MjU1MDg5MDE5Mjg5NjI0.XYc4fA.1EdWa1AfpUbxLTJZE2GS7SthWBo")

