"""
Orka Discord Bot
Copyright (c) 2017 William Bennett
"""

###########
# IMPORTS #
###########

import discord
import random
import markovify
from os import path, makedirs

from scripts import *


###################
# OTHER FUNCTIONS #
###################


def add_msg(channel, text, mode='a+'):
    """
    Appends a message to the end of a file.
    """
    with open('channels/{0}.txt'.format(channel), '{0}'.format(mode), encoding="utf_8") as file:
        file.write('{0}\n'.format(text))


def make_markov_model(channel):
    with open('channels/{0}.txt'.format(channel), 'r', encoding="utf_8") as file:
        model = markovify.NewlineText(file)
    global model


#######
# BOT #
#######

class Orka(discord.Client):

    async def on_ready(self):
        print('Logging in...')
        print('Logged in as {0}; ID #{1}'.format(client.user.name, client.user.id))
        print('Setting status...')
        await client.change_presence(game=discord.Game(name='https://github.com/rivermont/orka'))
        print('Gathering available text channels...')
        for server in client.servers:
            for channel in server.channels:
                if channel.type == discord.ChannelType.text:
                    if channel.permissions_for(server.me).read_messages:
                        print('Read access in: ' + server.name + '/' + channel.name)
                        read.append(channel)
        print('Downloading logs from readable text channels...')
        for channel in read:
            add_msg(channel, '', mode='w+')
            async for message in client.logs_from(channel, limit=1000):
                add_msg(channel, message.content, mode='a')
        print('Ready.')

    async def on_member_join(self, member):
        general = self.get_server("256600580837998592").get_channel("256600580837998592")
        await client.send_message(
            general,
            'Welcome, @{0}! Please familiarize yourself with our #rules, then go wild!'.format(member.name)
        )

    async def on_message(self, message):
        print('Received message..')
        content = message.content
        channel = message.channel
        add_msg(channel, content)

        # General commands
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

        elif content.startswith('!convert'):
            # Converts Kelvin/Celsius/Fahrenheit
            input_ = content.split()
            try:
                amount = int(input_[1][:-1])
                unit_from = input_[1][-1]
                unit_to = input_[2]
                result = convert(amount, unit_from, unit_to)
                if result == "Error":
                    raise IndexError
                else:
                    await client.send_message(channel, 'Converted {0}{1} to {2}{3}.'.format(amount, unit_from, result, unit_to))
            except IndexError:
                print('Invalid input.')
                await client.send_message(channel, 'Invalid input. Must be in format `!convert 23U U`.')

        # Moderation commands
        elif content.startswith('@stop'):
            print('Stopping bot...')
            await client.logout()

        elif content.startswith('@logs'):
            async for m in client.logs_from(channel):
                add_msg(channel, m.content)

        elif content.startswith('@generate'):
            print('Generating markov model for channel {0}'.format(channel))
            make_markov_model(channel)
            await client.send_message(channel, 'Successfully generated markov model.')

        elif content.startswith('!sentence'):
            # Generates a single line from the current markov model
            # Under moderation b/c that's where @generate is
            sentence = ''
            try:
                sentence = model.make_sentence(tries=1000)
            except NameError:
                print('No available markov model.')
                await client.send_message(channel, 'No available markov model.')
            if not bool(sentence):
                await client.send_message(channel, 'No sentence generated.')
            else:
                await client.send_message(channel, sentence)

        elif content.startswith('@save'):
            with open('model.json', 'w+') as f:
                f.write(model.to_json())

        elif content.startswith('@test'):
            # Generic testing function
            pass


#######
# RUN #
#######

client = Orka()

read = []


if __name__ == '__main__':
    if not path.exists('channels\\'):
        makedirs('channels\\')

    client.run()
