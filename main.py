import discord
import os
import random
import pytz
from discord.ext import tasks
from datetime import datetime, timedelta
from keep_alive import keep_alive
import asyncio
import builtins
from replit import db

import roll, stats, bleep, headline, opinion, uska, cyoa, lads, påg
from discord.ext import commands

bot = commands.Bot(command_prefix='!')
builtins.bot = bot

import rpg
import TurdLog

client = discord.Client()
kanal_dev = 828918567712849920
kanal_chatt = 757565322034151474
kanal_turdlog = 1193542284172607548


def getName(disc_name) -> str:
	if disc_name == "edv_rd":
		return "Ed"
	elif disc_name == ".shamshir":
		return "Kawa"
	elif disc_name == "loopline":
		return "Teo"
	elif disc_name == "ogarmage":
		return "Ale"
	elif disc_name == "mindytyrone":
		return "Bendik"
	elif disc_name == "medelsnygg":
		return "Danne"
	elif disc_name == "marremarre":
		return "Marre"
	elif disc_name == "da_white_bernie_mac":
		return "Micke"
	elif disc_name == "kamyasso":
		return "Kamy"
	elif disc_name == "stibba2g4u":
		return "Stibba"
	elif disc_name == "nils4444":
		return "Nils"
	else:
		return disc_name


def giveName() -> str:
	chatten = [
	 "Ed", "Kawa", "Teo", "Ale", "Bendik", "Danne", "Marre", "Micke", "Kamy",
	 "Nils"
	]

	return random.choice(chatten)


def getTitle(mood) -> str:
	titlar = {
	 "main": ["king", "maestro", "bror", "chefen", "boss"],
	 "angle": ["älskling", " <3", "finis", "darling", "sötnos"],
	 "misogyni": ["vännen", "gullet", "plutten", "gumman", "tösen"],
	 "förolämpning": ["bitch !", "fucker !", "tjockskalle !", "biatch !"],
	 "rasism": ["sahib"],
	 "svordomar": ["för tusan", "för fasen"]
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


@bot.event
async def on_ready():
	print('inloggad som {0.user} .. yee'.format(bot))


@bot.command(pass_context=True, name="rpg")
async def stefanrpg(ctx, arg):

	sender = ctx.message.author.name
	sender_raw = ctx.message.author

	await rpg.action(arg, sender, ctx.channel, sender_raw)


@bot.command(pass_context=True, name="turdlog")
async def turdlog(ctx):

	channel_id = commands.Bot.get_channel(bot, 1193542284172607548)

	announceChannel = commands.Bot.get_channel(bot, 757565322034151474)

	await TurdLog.init(channel_id, announceChannel)


@bot.command(pass_context=True, name="nyttnamn")
async def nytt_smeknamn(ctx):
	#byter discord-smeknamn på random person i chatten

	nicknames = [
	 "LillaSnuttePojken", "Alfons_Hitler", "* * [ [ [ 3 CM LÅNG ] ] ] * *",
	 "DOLME3000", "Min Röv Ont..", "Da_AssLord", ".[ ShitSucker ].",
	 "bruce__springsteen.mp3", "irriterande snubbe",
	 "👼 Knubbig rosenkindad påg 👼", "TheJamaicanSvullo420",
	 "C_H_O_C_K_L_A_D_M_J_Ö_L_K_", "Han Som Inte Duschar",
	 "rosa fluff i näsan ^^", "svidde bäörs", "COVID = Rojalistisk Komplott",
	 f"{getName(ctx.author.name)} Har MR I Röven 🤭", "vem här gillar öl",
	 "UskaHunter69", "DRULEN", "-/- 0,3 på högskoleprovet -\-",
	 "MBGA Make Birsta Great Again", "Stolt moderator för /r/filthatt", "Mr MR",
	 "MMA-kille med för tighta jeans", "signerar sms med Hadde gött",
	 "EPA-raggare med Supremekeps", "PubQuizMästar'n", "da_enlightened_wigga",
	 "Gnarls Barkely-That make me Crazy", "Luttrad vinylkille",
	 "Hade varit modell om han var längre", "Personen bakom CP-listan",
	 "denna användare snackar bullshit", "Tyvärr inte välutrustad.",
	 "Min penis är liten. Och?", "🍤 ANVÄNDARE MED LITEN PENIS 🍤", "fibromannen",
	 "Utbränd sexarbetare", "Säsongsdeprimerad solovårare",
	 "Kille Danne ringt polisen på", "Kyrkogårdsvaktmästarens pojk",
	 "da Pussy Pirate", "DAN_DOLME.EXE", "Ales macka var inte ens så stor?",
	 "Erik i Polyfamiljen"
	]

	random_nick = random.choice(nicknames)
	await ctx.author.edit(nick=random_nick)

	await ctx.channel.send(f"{getName(ctx.author.name)} heter nu {random_nick}")


@bot.command(pass_context=True, name="dntest")
async def dagens_nyheter(ctx):
	# channel = commands.Bot.get_channel(bot, 757565322034151474)
	channel = ctx.channel

	dagens_datum = datetime.now(
	 pytz.timezone('Europe/Stockholm')).strftime("%d/%m/%Y")
	dagens_headline = headline.main()
	dagens_headline_text = dagens_headline[0]
	dagens_headline_bild_url = dagens_headline[1]
	dagens_headline_string = f"JUST NU: {dagens_headline_text}"

	dagens_opinion_string = opinion.main()

	dagens_opinion_namn = roll.randomName("Skribent")

	tidningsnamn = opinion.tidning()

	embed = discord.Embed(title=f"Dagens nyheter för {dagens_datum}",
	                      color=0x737ad9)
	embed.set_author(name=f"{tidningsnamn}")
	# embed.set_thumbnail(url=dagens_headline_bild_url)
	embed.add_field(name=dagens_headline_string, value="", inline=False)

	embed.add_field(name=f"Dagens insändare av {dagens_opinion_namn}",
	                value=dagens_opinion_string,
	                inline=False)

	await channel.send(embed=embed)


@bot.command(pass_context=True, name="duell")
async def duell(ctx, user: discord.User):
	deltagare1 = ctx.message.author
	deltagare2 = user

	text = f"{getName(deltagare1.name)} utmanar {getName(deltagare2.name)} på duell!"
	embed = discord.Embed()
	embed.add_field(name="Duell", value=text, inline=False)
	await ctx.message.channel.send(embed=embed)

	deltagare_array = [deltagare1, deltagare2]

	vinnare = random.choice(deltagare_array)

	if vinnare == deltagare1:
		loser = deltagare2
	else:
		loser = deltagare1

	resultat = [
	 f"{getName(vinnare.name)} hugger direkt av {getName(loser.name)}s huvud med en katana",
	 f"{getName(vinnare.name)} skjuter {getName(loser.name)} i huvudet med ett raketgevär",
	 f"{getName(vinnare.name)} spränger {getName(loser.name)} med en atombomb",
	 f"{getName(vinnare.name)} skjuter en Magnum 44 rakt i {getName(loser.name)}s anus",
	 f"{getName(vinnare.name)} smittar {getName(loser.name)} med fail aids...",
	 f"{getName(vinnare.name)} headshottar {getName(loser.name)} med railgun",
	 f"{getName(vinnare.name)} målar en tunnel på en bergsvägg och {getName(loser.name)} kör rakt in i den med bil",
	 f"{getName(vinnare.name)} skjuter ett snipergevär rakt på  {getName(loser.name)}s kulor",
	 f"{getName(vinnare.name)} suger {getName(loser.name)} helt torr",
	]

	text = random.choice(resultat)
	embed = discord.Embed()
	embed.add_field(name="Duell", value=text, inline=False)
	await ctx.message.channel.send(embed=embed)

	#timeout = (datetime.utcnow() + timedelta(seconds=30)).isoformat()
	#loser_ = ctx.message.guild.get_member(loser.id)

	#await loser_.edit(timed_out_until=timeout)


@bot.event
async def on_message(message):
	#namn = getName(message.author.name)
	namn = message.author.name
	meddelandetext = message.content
	meddelande = message.content.lower()
	#titel = getTitle(bleep.getMood())
	channel = message.channel

	if message.author == bot.user:
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

		await message.channel.send(headline_message, file=picture_send)

	if meddelande.startswith('!uska'):
		uska_message = uska.main()
		picture_url = uska.pic()

		with open(picture_url, 'rb') as f:
			picture_send = discord.File(f)

		await message.channel.send(uska_message, file=picture_send)

	if meddelande.startswith('!påg'):
		påg_message = påg.main()
		picture_url = påg.pic()

		with open(picture_url, 'rb') as f:
			picture_send = discord.File(f)

		await message.channel.send(påg_message, file=picture_send)

	if meddelande.startswith('!opinion'):
		opinion_message = opinion.main()
		picture_url = opinion.pic()

		with open(picture_url, 'rb') as f:
			picture_send = discord.File(f)

		await message.channel.send(opinion_message, file=picture_send)

	if meddelande.startswith('!roll'):
		namn = getName(message.author.name)
		roll_message = roll.main(namn)
		await message.channel.send(roll_message)

	if meddelande.startswith('!lads'):
		await lads.main(channel)

	if meddelande.startswith('!join'):
		await lads.JoinLads(channel, namn)

	if meddelande.startswith("!toplads"):
		await lads.PrintTopLads(channel)

	if meddelande.startswith('!bleep'):
		bleep_message = str(bleep.main(init=False))
		await message.channel.send(bleep_message)

	if meddelande.startswith('!cyoa'):
		await cyoa.main(channel, 0)

	if meddelande.startswith('!convoy'):

		convoy_message = "🚛"
		convoy = db["convoy"]

		for n in range(convoy):
			convoy_message = convoy_message + " 🚛 "
		await message.channel.send("Convoy " + convoy_message)
		db["convoy"] = convoy + 1

	if meddelande.startswith("stefan"):
		if meddelande.endswith("?"):
			if meddelande.startswith("stefan vem"):
				await message.channel.send("Där " + giveName() + " !")
			else:
				eightball = random.randint(1, 2)

				if eightball == 1:
					await message.channel.send("Jäpp !")
					await message.add_reaction("👍")
				elif eightball == 2:
					await message.channel.send("Nä !")
					await message.add_reaction("👎")
		else:
			if random.randint(1, 10) == 10:
				await message.add_reaction("👁️")

	if meddelande.startswith("gn ") or meddelande.startswith(
	  "gnsg") or meddelande == "gn":
		titel = getTitle(bleep.getMood())
		await message.channel.send("gn " + titel)
		await message.add_reaction("💋")

	if meddelande.startswith("gm ") or meddelande == "gm":
		titel = getTitle(bleep.getMood())
		await message.channel.send("gm " + titel)
		await message.add_reaction("🌞")

	if meddelande.startswith("morn"):
		await message.channel.send("Morn")
		if getName(
		  message.author.name) == "Bendik" or message.author.name == "Kolato":
			await message.add_reaction(random.choice(["🇩🇰", "🇫🇮", "🇫🇴"]))
		else:
			await message.add_reaction("🇳🇴")

	if meddelande.startswith("!jah"):
		peps = "<:peps:958381154690531409>"
		jahmessage = f"{message.author.name}, Jah har gett dig sin blessing {peps}"
		await message.channel.send(jahmessage)

	if meddelande.startswith("svidde, säg "):
		svidde = "<:svidde:768197875652886560>"
		text = meddelandetext[12:]
		embed = discord.Embed()
		embed.set_thumbnail(url="https://i.imgur.com/ElTkuBd.jpg")
		embed.add_field(name="Svidde säger", value=text, inline=False)
		await message.channel.send(embed=embed)

		sviddesays = []

		for say in db["svidde"]:
			sviddesays.append(say)

		sviddesays.append(text)
		db["svidde"] = sviddesays

	if meddelande.startswith("!svidde"):
		svidde = "<:svidde:768197875652886560>"
		text = random.choice(db["svidde"])
		embed = discord.Embed()
		embed.set_thumbnail(url="https://i.imgur.com/ElTkuBd.jpg")
		embed.add_field(name="Svidde säger", value=text, inline=False)
		await message.channel.send(embed=embed)

	if meddelande.startswith("!list"):
		for column in db["svidde"]:
			print(column)

	await bot.process_commands(message)


@tasks.loop(seconds=1)
async def kolla_klockan():
	nutid = datetime.now(pytz.timezone("Europe/Stockholm"))
	nutid_str = datetime.strftime(nutid, "%H:%M:%S")
	if nutid_str == "06:00:00":
		inställningar = bleep.main(init=True)
		print(inställningar)
		#await client.get_channel(int(kanal_dev)).send(inställningar)
	if nutid_str == "18:00:00":
		dagens_nyheter()
		print("dagens nyheter")


@kolla_klockan.before_loop
async def w8():
	await client.wait_until_ready()


kolla_klockan.start()
keep_alive()


@bot.event
async def waitForVal(message, author):

	try:
		reaction, user = await bot.wait_for(
		 "reaction_add", timeout=15, check=lambda reaction, user: print(author))
		#reaction, user = await client.wait_for("reaction_add", timeout=15, check = lambda reaction, user: user == author and (reaction.message.id == message.id))

	except asyncio.TimeoutError:

		return

	else:

		return reaction.emoji


bot.run(os.environ['TOKEN'])
