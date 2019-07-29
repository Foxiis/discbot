import discord
import time
import asyncio

#id = 605159798908125199
messages = joined = 0

def read_token():
    with open ("token.txt","r") as f:
        lines = f.readlines()
        return lines[0].strip()

token = read_token()

client = discord.Client()



async def update_stats():
    await client.wait_until_ready()
    global messages, joined

    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time: {int(time.time())}, Messages: {messages}, Members Joined: {joined}\n")

                messages = 0
                joined = 0

                await asyncio.sleep(5)
        except Exception as e:
            print(e)
            await asyncio.sleep(5)


@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.guild.channels:
        if str(channel) == "general":
            await channel.send(f"""Heey! Welcome, {member.mention}! Glad you could make it!~""")

@client.event
async def on_message(message):
    global messages
    messages += 1

    id = client.get_guild(605159798908125199)
    channels = ["general"]

    if str(message.channel) in channels:
        if message.content.find("-hello") != -1:
            await message.channel.send("Hey!")
        elif message.content.find("-help") != -1:
            await message.channel.send("Hm? Sure, I can do *lots* of things!\n\n- hello\n- help\n- users")
        elif message.content == "-users":
            await message.channel.send(f"""I did the math and there are {id.member_count} members in this server! Heheh~""")


@client.event
async def on_message(message):
    ...
    bad_words = ["fuck", "shit", "crap", "piss", "sou is a bad character"]

    for word in bad_words:
        if message.content.count(word) > 0:
            print("A no-no word was said.")
            await message.channel.purge(limit=1)
    ...


client.loop.create_task(update_stats())
client.run(token)
