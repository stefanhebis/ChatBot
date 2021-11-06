import asyncio
from replit import db
from discord import Embed

async def main(channel):
	await StartLads(channel)


async def StartLads(channel):
	stefan_url = "https://i.imgur.com/LT3cAQP.jpg"
	lads_message_format = \
	"```" \
	+ "\nOi ! Lads check !\n" \
	+ "```\n" \

	lads_message = str(lads_message_format)

	embed=Embed(title="Lads !", color=0x737ad9)
	embed.set_author(name="Stefan Hebis", icon_url=stefan_url)
	embed.set_thumbnail(url=stefan_url)
	embed.add_field(name="Lads check !", value=lads_message, inline=False)
	embed.set_footer(text="/ Stefan")
	sent_message = await channel.send(embed=embed)	

	await LadsCheck(channel, sent_message.id)
	

async def PrintTopLads(channel):
	lads_emoji = "<:svoda:787100880188473354>"
	#stefan_url = channel.author.avatar_url
	stefan_url = "https://i.imgur.com/LT3cAQP.jpg"
	top_lads_return = await GetTopLads(3)


	firstlad = await GetName(top_lads_return[0])
	secondlad = await GetName(top_lads_return[2])
	thirdlad = await GetName(top_lads_return[4])
	
	top_lads_msg = "```" \
	"\n" \
	+ "1: " + firstlad + " (" + str(top_lads_return[1]) + " LadPoints)" \
	+ "\n" \
	+ "2: " + secondlad + " (" + str(top_lads_return[3]) + " LadPoints)" \
	+ "\n" \
	+ "3: " + thirdlad + " (" + str(top_lads_return[5]) + " LadPoints)" \
	+ "\n```" 

	#await channel.send(str(top_lads_msg))

	embed=Embed(title="Lads !", color=0x737ad9)
	embed.set_author(name="Stefan Hebis", icon_url=stefan_url)
	embed.set_thumbnail(url=stefan_url)
	embed.add_field(name="Top Lads !", value=str(top_lads_msg), inline=False)
	embed.set_footer(text="/ Stefan")
	await channel.send(embed=embed)	


async def GetTopLads(lads_limit):
	keys = db.prefix("l+")
	top_lad = {"name":"name", "score":0}
	top_lads = []
	top_lads_message = []

	for ladname in keys:
		sladname = str(ladname)
		sname = str(ladname)[2:]
		score = db[sladname]
		top_lad["name"] = sname
		top_lad["score"] = int(score)
		top_lad_c = top_lad.copy()
		top_lads.append(top_lad_c)
	
	top_lads.sort(key=lambda x: x.get("score"), reverse=True)
	
	for t_l in top_lads:
		sname = t_l["name"]
		score = t_l["score"]
		top_lads_message.append(sname)
		top_lads_message.append(score)

	return top_lads_message


async def AddHighScore(channel, name):
	sname = "l+" + str(name)
	val = str(int(db[sname]) + 1)
	db[sname] = val
	return val


async def LadsCheck(channel, message_id):
	lads_emoji = "<:svoda:787100880188473354>"
	message = await channel.fetch_message(message_id)
	await message.add_reaction(lads_emoji)
	await asyncio.sleep(300)
	lads = set()
	message = await channel.fetch_message(message_id)
	for reaction in message.reactions:
		async for user in reaction.users():
			if user.name == "Stefan Hebis":
				print("stefan")
			else: 
				lads.add(user)
		
	await UpdateHighScore(channel, lads)


async def UpdateHighScore(channel, lads):
	for lad in lads:
			await AddHighScore(channel, lad.name)


async def JoinLads(channel, name):
	sname = "l+" + str(name)
	db[sname] = "0"
	await channel.send("Oi " + name + " your a lad now !")

	
async def GetName(disc_name) -> str:
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