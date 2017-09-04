import discord
import asyncio
# import random
# import os

client = discord.Client()


@client.event
async def on_ready():
	print('Logged in as {0} - {1}'.format(client.user.name, client.user.id))


@client.event
async def on_message(message):
	if message.content.startswith('!test'):
		await client.send_message(message.channel, 'Hello World!')

client.run('Mjg2NTgzNjI3NzkyNTE1MDgz.C5i1bw.Wyh56h4hWkeg8kdS1p0sC73to7A')
