import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run('token')
