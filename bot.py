"""
Orka Discord Bot
Copyright (c) 2017 William Bennett
"""

import discord
import random
import markovify

client = discord.Client()


def add_msg(channel, text):
	"""
	Appends a message to the end of a file.
	"""
	try:
		with open('channels/{0}.txt'.format(channel), 'a+') as file:
			file.write('{0}\n'.format(text))
	except UnicodeEncodeError:
		print('Unknown character in message.')

@client.event
async def on_ready():
	print('Logged in as {0} - {1}'.format(client.user.name, client.user.id))


@client.event
async def on_message(message):
	print('Received message..')
	content = message.content
	add_msg(message.channel, content)
	if message.content.startswith('!flip'):
		# Flips a coin on two choices. Defaults to Heads or Tails.
		print('Flipping coin...')
		if len(content.split()) == 1:
			choice_ = random.choice(['Heads', 'Tails'])
			await client.send_message(message.channel, choice_)
		elif len(content.split()) == 2:
			await client.send_message(message.channel, 'Only one option supplied. Must be two or none.')
		elif len(content.split()) == 3:
			options = content.split()[1:]
			flip = random.choice(options)
			await client.send_message(message.channel, flip)
	elif content.startswith('!roll'):
		# Rolls a dice. Defaults to a d6.
		print('Rolling die...')
		if len(content.split()) == 1:
			roll = random.randint(1, 6)
			await client.send_message(message.channel, 'You rolled a {0}.'.format(roll))
		if len(content.split()) == 2:
			input_ = content.split()[1]
			roll = random.randint(1, int(input_))
			await client.send_message(message.channel, 'You rolled a {0}.'.format(roll))

if __name__ == '__main__':
	print('Logging in...')
	client.run('Mjg2NTgzNjI3NzkyNTE1MDgz.C5i1bw.Wyh56h4hWkeg8kdS1p0sC73to7A')
