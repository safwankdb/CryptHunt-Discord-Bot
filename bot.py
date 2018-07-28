import discord
from random import choice
import pickle
import os
TOKEN = 'NDcyNjg5OTM5MDIxMjk5NzEy.Dj3DfA.95HY36FT7mWpC9gBfWqgvzSAJ_U'
# Client ID = 472689939021299712
client = discord.Client()
players = {}
rules = '0.You can win with no programming experience at all\n1. Answers are case insensitive.\n2. Answer may contain spaces, numbers and special characters.\n3. Say rules to read them again.\n4. Say ready for recieving next question.\n5. Your messages on main channel will be instantly deleted. Don\'t even try.\n6. Even the smallest attempt to cheat/hint will be an instant ban. :)\n'
answers = ['linux1', 'wiki2', '20313', 'google4', 'wncc5']
ANS = ['wiki', 'wncc wiki', 'wncc', 'google',
       '2031', 'base', 'ubuntu', 'linux', 'unix', 'os'
       'search engine']
whitelist = ['safwankdb', 'Abeen', 'ydidwania', 'starlord1311', 'arpit1110']
names = {}
def_channel = None
idk = ['Nibba Wut?', 'U wot m8?', 'Pardon', 'Come again', 'Sorry, dint getcha']
if 'names.pkl' in os.listdir():
    with open('names.pkl', 'rb') as f:
        names = pickle.load(f)
if 'players.pkl' in os.listdir():
    with open('players.pkl', 'rb') as f:
        players = pickle.load(f)
del players['safwankdb']
del names['safwankdb']


async def startQuiz(user):
    await client.send_message(user, 'Welcome to WnCC Crypt Hunt v1.0')
    await client.send_message(user, rules)
    await client.send_message(user, 'Ready whenever you are :p')


def named(user):
    return user.name in names.keys()


def playersDB(key):
    if key in players.keys():
        return players[key]
    else:
        return '0'


def logMessage(message):
    messageLog = open('log.txt', 'a+')
    messageLog.write(str(message.timestamp) + '\n')
    messageLog.write(message.author.name + ' | ' +
                     str(playersDB(message.author.name)) + '\n')
    messageLog.write(message.content + '\n')
    messageLog.write('-----\n')
    messageLog.close()
    print(message.author.name, 'level', playersDB(
        message.author.name), message.channel)
    print(message.content)
    print()


async def sendQuestion(user, channel):
    if playersDB(user.name) == 0 and not named(user):
        await client.send_message(user, 'Enter your real name in a single line. It should be same as your ID card')
        msg = await client.wait_for_message(author=user, channel=channel)
        names[user.name] = msg.content
        await client.send_message(user, 'You name has been recorded. Ready whenever you are')
        print(user.name + '\'s name is', names[user.name], '\n')
        logMessage(msg)
        return
    if int(playersDB(user.name)) > 5:
        await client.send_message(user, 'Nice try but you\'ve solved all questions :p')
        return
    await client.send_message(user, 'Question ' + str(players[user.name]))
    await client.send_file(user, 'q' + str(players[user.name]) + '.png')


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    global def_channel
    global players
    if message.author == client.user:
        return
    else:
        logMessage(message)
    if message.channel.name == 'general':
        def_channel = message.channel
    if 'rules' in message.content.lower():
        if message.channel.name == 'general':
            msg = '{0.author.mention} PMing you the rules'.format(message)
            await client.send_message(message.channel, msg)
        await client.send_message(message.author, rules)

    elif message.content.lower() == ('hello world'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        if message.author.name not in players.keys():
            await client.send_message(message.channel, 'You\'ve been registered as a player :), check PM')
            players[message.author.name] = 0
            await startQuiz(message.author)

        else:
            await client.send_message(message.channel, 'You\'ve already registered as a player.')
            await client.send_message(message.author, 'You have solved ' + str(max(0, players[message.author.name] - 1)) + ' question/s. Type ready for next.')

    elif 'ready' in message.content.lower():
        await sendQuestion(message.author, message.channel)

    elif message.content.lower() + str(playersDB(message.author.name)) in answers:
        players[message.author.name] += 1
        await client.send_message(message.author, 'Correct Answer.')
        #players = sorted(players.items(), key=lambda x: x[1])
        with open('players.pkl', 'wb') as f:
            pickle.dump(players, f)
        with open('names.pkl', 'wb') as f:
            pickle.dump(names, f)
        if players[message.author.name] == 6:
            await client.send_message(message.author, 'Congratulations. You have completed the Crypt Hunt. Do come at tech orientation.')
            await client.send_message(message.author, 'Questions created by: Mohd Safwan and Arpit Aggrawal\nBot created by: Mohd Safwan\nTesting and Troubleshooting: WnCC tty11\n')
            # if def_channel:
            # await client.send_message(def_channel, '{0.author.mention} has completed the hunt.'.format(message))
        else:
            await client.send_message(message.author, 'Next question whenever you are ready.')
    elif 'chuda' in message.content.lower():
        await client.send_message(message.author, 'Wow, are we really going there?')
    elif 'correct' in message.content.lower() and 'answer' in message.content.lower():
        await client.send_message(message.author, 'You won\'t get it.')
    elif 'clue' in message.content.lower():
        await client.send_message(message.author, 'Are you too dumb for this?')
    elif 'sup?' in message.content.lower() or 'whats up' in message.content.lower():
        await client.send_message(message.author, 'your lack of creativity')
    elif 'marry' in message.content.lower():
        await client.send_message(message.author, 'You\'ll die single')
    elif 'help' in message.content.lower():
        await client.send_message(message.author, 'get a shrink')
    elif 'love' in message.content.lower():
        await client.send_message(message.author, 'i have a boyfriend')

    elif message.channel.name != 'general' and int(playersDB(message.author.name)) >= 0:

        if playersDB(message.author.name) == 1:
            if message.content.lower() == 'ubuntu':
                await client.send_message(message.author, 'You\'ve almost cracked it. Focus on the penguin')
            elif message.content.lower() == 'unix':
                await client.send_message(message.author, 'Who knew, the younger bother had the answer')

        elif playersDB(message.author.name) == 2:
            if 'grundy' in message.content.lower():
                await client.send_message(message.author, 'Good job till here, try realting it to our precious insti')
            elif 'wikipedia' in message.content.lower():
                await client.send_message(message.author, 'Close enough. Truncate you thoughts')
            elif 'randi' in message.content.lower():
                await client.send_message(message.author, 'Teri Maa')

        elif playersDB(message.author.name) == 3:
            if message.content == '1431':
                await client.send_message(message.author, 'Do you really think that is the answer? I mean really?')
            elif message.content == '11111':
                await client.send_message(message.author, 'Congratulations, you got to base 2')
            elif message.content == '2201':
                await client.send_message(message.author, 'Few people get to base 3. Lucky you. Focus on the text in image')

        elif playersDB(message.author.name) == 4:
            if message.content == '10^100':
                await client.send_message(message.author, 'Some numbers are special, like you. Lol, kidding, about the 2nd part.')
            elif message.content.lower() == 'googol':
                await client.send_message(message.author, 'Really dude? You\'re this close, and you can\'t get the answer. Tsk Tsk')

        elif playersDB(message.author.name) == 5:
            if message.content == '231433':
                await client.send_message(message.author, 'Answer is no morse code. Decode the hidden message.')

        if playersDB(message.author.name) and named(message.author):
            await client.send_message(message.author, 'Wrong answer n00b')
        elif named(message.author):
            players[message.author.name] += 1
            with open('players.pkl', 'wb') as f:
                pickle.dump(players, f)
        else:
            await client.send_message(message.author, choice(idk))
    if message.channel.name == 'general' and message.author.name not in whitelist:
        for i in ANS:
            if i in message.content.lower():
                await client.ban(message.author)
                await client.send_message(message.channel, message.author.name + ' has been banned for trying to cheat. :)')
                # await client.unban(message.server, message.author)
    if message.author.name not in whitelist and message.channel.name == 'general':
        await client.delete_message(message)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
client.run(TOKEN)
