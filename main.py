import discord
import os


files = os.listdir('assets')



class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return  

        if message.content.lower().startswith('hello'):
            await message.channel.send(f'Hello! {message.author.mention}')

        if message.content.lower().startswith('clean'):
            await message.channel.purge(limit=100)

        if message.content.lower().startswith('pogi'):
            imagePath = 'assets/Raj.jpg'
            with open(imagePath, 'rb') as f:
                picture = discord.File(f)
                await message.channel.send(file=picture)
        
    async def on_reaction_add(self, reaction, user):
         imagePath = 'assets/RajKissy.jpg'
         with open(imagePath, 'rb') as f:
                 picture = discord.File(f)
                 await reaction.message.channel.send(f'{user.mention} I love you! {reaction.emoji}')
                 await reaction.message.channel.send(file=picture)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTQ2ODk2NzE2MjkwNjQxNTEyNQ.G9oWrn.qCboFlDq-S09wgE6ASG6ksdJBe3hyo9trcCpNQ')


   