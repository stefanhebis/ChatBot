import asyncio
from discord import Embed
from builtins import bot

stefan_url = "https://i.imgur.com/LT3cAQP.jpg"


async def init(channel, announceChannel):
	await TurdLog(channel, announceChannel)


async def TurdLog(channel, announceChannel):

	init_message_format = \
 "```" \
 + "React To Init Turd" \
 + "```" \

	init_message = str(init_message_format)

	embed = Embed(title="TurdLog", color=0x737ad9)
	embed.set_author(name="Stefan Hebis", icon_url=stefan_url)
	embed.set_thumbnail(url=stefan_url)
	embed.add_field(name="", value=init_message, inline=False)

	sent_message = await channel.send(embed=embed)

	await TurdCheck(channel, sent_message.id, announceChannel)


async def TurdCheck(channel, message_id, announceChannel):
	turd_emoji = "<:svoda:787100880188473354>"

	while True:
		message = await channel.fetch_message(message_id)
		await message.add_reaction(turd_emoji)

		for reaction in message.reactions:
			async for user in reaction.users():
				if user.name == "Stefan Hebis":
					print("")
				else:
					await TurdCreate(channel, announceChannel, user)
					await asyncio.sleep(10)
					await message.clear_reactions()
					await message.add_reaction(turd_emoji)


async def TurdCreate(channel, announceChannel, user):

	postedUser = user

	init_message = '***TurdLog*** -- Turd Incoming ... React With Rating Of Experience To Deploy Turd -- ***TurdLog*** '

	embed = Embed(title="TurdLog", color=0x737ad9)
	embed.set_author(name="Stefan Hebis", icon_url=stefan_url)
	embed.set_thumbnail(url=stefan_url)
	embed.add_field(name="", value=init_message, inline=False)

	messageId = await channel.send(embed=embed)

	while True:

		message = await channel.fetch_message(messageId.id)

		def check(reaction, user):

			return user == postedUser

		try:
			reaction, user = await bot.wait_for(event="reaction_add",
			                                    timeout=600,
			                                    check=check)

		except asyncio.TimeoutError:

			return

		else:
			await TurdDeploy(channel, announceChannel, reaction, user)
			await message.delete()


async def TurdDeploy(channel, announceChannel, reaction, user):

	messageText = f"***TurdLog Notification*** -- Turd (rating: {reaction.emoji}) Deployed By {getName(user.name)} ..."

	embed = Embed(title="TurdLog", color=0x737ad9)
	embed.set_author(name="Stefan Hebis", icon_url=stefan_url)
	embed.set_thumbnail(url=stefan_url)
	embed.add_field(name="", value=messageText, inline=False)

	await announceChannel.send(embed=embed)


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
