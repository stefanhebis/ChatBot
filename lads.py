import asyncio
from replit import db
from discord.utils import get



async def main(channel):
	print("main")
	
	await StartLads(channel)

async def StartLads(channel):
	print("start lads")
	
	lads_message_format = \
	"```" \
	+ "\nOi ! Lads check !\n" \
	+ "```\n" \


	lads_message = str(lads_message_format)

	sent_message = await channel.send(lads_message)
	
	await LadsCheck(channel, sent_message.id)
	

async def PrintTopLads(channel):
	top_lads_return = await GetTopLads(3)

	firstlad = await GetName(top_lads_return[0])
	secondlad = await GetName(top_lads_return[2])
	thirdlad = await GetName(top_lads_return[4])
	
	top_lads_msg = "```" \
	+ "\nTOP LADS = \n" \
	+ "1: " + firstlad + " (" + str(top_lads_return[1]) + " LadPoints)" \
	+ "\n" \
	+ "2: " + secondlad + " (" + str(top_lads_return[3]) + " LadPoints)" \
	+ "\n" \
	+ "3: " + thirdlad + " (" + str(top_lads_return[5]) + " LadPoints)" \
	+ "\n```" 

	await channel.send(str(top_lads_msg))

async def GetTopLads(lads_limit):
	print("top lads")
	keys = db.prefix("l+")
	print(keys)
	
	loop = 0

	top_lad = {"name":"name", "score":0}

	top_lads = []

	top_lads_message = []

	for ladname in keys:
		print(loop)
		sladname = str(ladname)
		sname = str(ladname)[2:]
		score = db[sladname]
		top_lad["name"] = sname
		top_lad["score"] = int(score)
		top_lad_c = top_lad.copy()
		top_lads.append(top_lad_c)
	
	#sort_orders = sorted(top_lads.items(), key=lambda x: x[1][1], reverse=True)
	#sort_key = top_lads[1]
	#sorted_top_lads = []
	#top_lads.sort(key=sort_key)
	print("osorterad lista: " + str(top_lads))
	top_lads.sort(key=lambda x: x.get("score"), reverse=True)
	print("sorterad lista: " + str(top_lads))

	for t_l in top_lads:
		sname = t_l["name"]
		score = t_l["score"]
		top_lads_message.append(sname)
		top_lads_message.append(score)


	
	return top_lads_message




async def AddHighScore(channel, name):
	print("add high score")
	sname = "l+" + str(name)
	print(sname)

	val = str(int(db[sname]) + 1)
	db[sname] = val
	return val


async def LadsCheck(channel, message_id):
	lads_emoji = "<:svoda:787100880188473354>"
	print("lads check")
	message = await channel.fetch_message(message_id)
	await message.add_reaction(lads_emoji)
	await asyncio.sleep(8)
	lads = set()
	message = await channel.fetch_message(message_id)
	for reaction in message.reactions:
		async for user in reaction.users():
			if user.name == "Stefan Hebis":
				print("stefan")
			else: 
				print("add LadsCheck")
				lads.add(user)
		
	await UpdateHighScore(channel, lads)

async def UpdateHighScore(channel, lads):
	for lad in lads:
			val = await AddHighScore(channel, lad.name)
			#await channel.send(str(val))

async def JoinLads(channel, name):
	sname = "l+" + str(name)
	db[sname] = "0"
	await channel.send("Oi " + name + " your a lad now !")

async def Init(channel):
	db["Stefan Hebis"] = "69"
	db["British Bloke"] = "1"
	print("init")
	

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
			

