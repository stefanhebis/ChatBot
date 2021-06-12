import discord
import os
import random
import pytz
import roll, stats, bleep, headline, opinion, uska, cyoa
from discord.ext import tasks
from datetime import datetime
from keep_alive import keep_alive

client = discord.Client()
kanal_dev = 828918567712849920
kanal_chatt = 262912061950918656

def getName(disc_name) -> str:
	if disc_name == "ed":
		return "Ed"
	elif disc_name == "Shamshir":
		return "Kawa"
	elif disc_name == "333o":
		return "Teo"
	elif disc_name == "Crank":
		return "Ale"
	elif disc_name == "MindyTyrone":
		return "Bendik"
	elif disc_name == "worst person shooter":
		return "Danne"
	elif disc_name == "Ironisktvit":
		return "Hånken"
	elif disc_name == "marre":
		return "Marre"
	elif disc_name == "jorts_michael":
		return "Micke"
	else:
		return disc_name

def getTitle(mood) -> str:
	titlar = {
		"main":
			["king", "maestro", "bror", "chefen", "boss"],
		"angle":
			["älskling", " <3", "finis", "darling", "sötnos"],
		"misogyni":
			["vännen", "gullet", "plutten", "gumman", "tösen"],
		"förolämpning":
			["bitch !", "fucker !", "tjockskalle !", "biatch !"],
		"rasism":
			["sahib"],
		"svordomar":
			["för tusan", "för fasen"]
	}

	if mood == "devil":
		sel_titlar = []
		for grej in titlar:
			if grej != "main" and grej != "angle":
				sel_titlar.extend[grej]
	else:
		sel_titlar = titlar["main"]
		sel_titlar.extend(titlar[mood])
  
	return random.choice(sel_titlar)

@client.event
async def on_ready():
	print('inloggad som {0.user} .. yee'.format(client))

@client.event
async def on_message(message):
	#namn = getName(message.author.name)
	meddelande = message.content.lower()
	#titel = getTitle(bleep.getMood())
	channel = message.channel

	if message.author == client.user:
		return

	if "Ye" in message.content:
		await message.channel.send('Ye !')

#	if "stefan hebis" in meddelande:
#		await message.channel.send('Fakkajoo !')

	if "svidde" in meddelande:
		emoji1 = '<:svidde:768197875652886560>'
		await message.add_reaction(emoji1)

	if meddelande.startswith('!stats'):
		namn = getName(message.author.name)
		stats_message = stats.main(namn)
		await message.channel.send(stats_message)

	if meddelande.startswith('!headline'):
		headline_return = headline.main()
		headline_message = headline_return[0]
		picture_url = headline_return[1]

		with open(picture_url, 'rb') as f:
			picture_send = discord.File(f)

		await message.channel.send(headline_message, file = picture_send)
  
	if meddelande.startswith('!uska'):
		uska_message = uska.main()
		picture_url = uska.pic()

		with open(picture_url, 'rb') as f:
			picture_send = discord.File(f)

		await message.channel.send(uska_message, file = picture_send)  

	if meddelande.startswith('!opinion'):
		opinion_message = opinion.main()
		picture_url = opinion.pic()

		with open(picture_url, 'rb') as f:
			picture_send = discord.File(f)

		await message.channel.send(opinion_message, file = picture_send)

	if meddelande.startswith('!roll'):
		namn = getName(message.author.name)
		roll_message = roll.main(namn)
		await message.channel.send(roll_message)

	if meddelande.startswith('!bleep'):
		bleep_message = str(bleep.main(init=False))
		await message.channel.send(bleep_message)

	if meddelande.startswith('!cyoa'):
		await cyoa.main(channel, 1)

	if meddelande.startswith("stefan"):
		if meddelande.endswith("?"):
			eightball = random.randint(1, 2)

			if eightball == 1:
				await message.channel.send("Jäpp !")
				await message.add_reaction("👍")
			elif eightball == 2:
				await message.channel.send("Nä !")
				await message.add_reaction("👎")
		else: 
			if random.randint(1,10) == 10:
				await message.add_reaction("👁️")

	if meddelande.startswith("gn ") or meddelande.startswith("gnsg") or meddelande == "gn":
		titel = getTitle(bleep.getMood())
		await message.channel.send("gn " + titel)
		await message.add_reaction("💋")

	if meddelande.startswith("gm ") or meddelande == "gm":
		titel = getTitle(bleep.getMood())
		await message.channel.send("gm " + titel)
		await message.add_reaction("🌞")

	if meddelande.startswith("morn"):
		await message.channel.send("Morn")
		if getName(message.author.name) == "Bendik":
			await message.add_reaction(random.choice(["🇩🇰", "🇫🇮", "🇫🇴"]))
		else:
			await message.add_reaction("🇳🇴")

@tasks.loop(seconds=1)
async def kolla_klockan():
  nutid = datetime.now(pytz.timezone("Europe/Stockholm"))
  nutid_str = datetime.strftime(nutid, "%H:%M:%S")
  if nutid_str == "06:00:00":
    inställningar = bleep.main(init=True)
    print(inställningar)
    #await client.get_channel(int(kanal_dev)).send(inställningar)

@kolla_klockan.before_loop
async def w8():
  await client.wait_until_ready()

kolla_klockan.start()
keep_alive()

client.run(os.getenv('TOKEN'))