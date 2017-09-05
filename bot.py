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
	with open('channels/{0}.txt'.format(channel), 'a+', encoding="utf_8") as file:
		file.write('{0}\n'.format(text))


def make_markov_model(channel):
	with open('channels/{0}.txt'.format(channel), 'r', encoding="utf_8") as file:
		model = markovify.NewlineText(file)
	global model


@client.event
async def on_ready():
	print('Logging in...')
	print('Logged in as {0}; ID #{1}'.format(client.user.name, client.user.id))
	print('Setting status...')
	await client.change_presence(game=discord.Game(name='https://github.com/rivermont/orka'))
	# for server in client.servers:
	# 	for channel in server.channels:
	# 		if channel.type == 'text':
	# 			print(channel.permissions_for(client))


@client.event
async def on_message(message):
	print('Received message..')
	content = message.content
	channel = message.channel
	add_msg(channel, content)

	if message.content.startswith('!flip'):
		# Flips a coin on two choices. Defaults to Heads or Tails.
		print('Flipping coin...')
		if len(content.split()) == 1:
			choice_ = random.choice(['Heads', 'Tails'])
			await client.send_message(channel, choice_)
		elif len(content.split()) == 2:
			await client.send_message(channel, 'Only one option supplied. Must be two or none.')
		elif len(content.split()) == 3:
			options = content.split()[1:]
			flip = random.choice(options)
			await client.send_message(channel, flip)
		elif len(content.split()) > 3:
			await client.send_message(channel, 'Too many options supplied. Must be two or none.')

	elif content.startswith('!roll'):
		# Rolls a dice. Defaults to a d6.
		print('Rolling die...')
		if len(content.split()) == 1:
			roll = random.randint(1, 6)
			await client.send_message(channel, 'You rolled a {0}.'.format(roll))
		if len(content.split()) == 2:
			input_ = content.split()[1]
			roll = random.randint(1, int(input_))
			await client.send_message(channel, 'You rolled a {0}.'.format(roll))

	elif content.startswith('!sentence'):
		sentence = model.make_sentence(tries=250)
		try:
			await client.send_message(channel, sentence)
		except discord.errors.HTTPException as e:
			if '(status code: 400)' in str(e):
				print('Failed to create sentence.')

	# elif content.startswith('@logs'):
	# 	async for m in client.logs_from(channel):
	# 		add_msg(channel, m.content)

	elif content.startswith('@generate'):
		print('Generating markov model for channel {0}'.format(channel))
		make_markov_model(channel)
		await client.send_message(channel, 'Successfully generated markov model.')

	elif content.startswith('$4'):
		await client.send_message(channel, '!sentence')


if __name__ == '__main__':
	client.run('Mjg2NTgzNjI3NzkyNTE1MDgz.C5i1bw.Wyh56h4hWkeg8kdS1p0sC73to7A')
