import asyncio
from replit import db
from discord import Embed


async def init(channel, announceChannel):
	await TurdLog(channel, announceChannel)


async def TurdLog(channel, announceChannel):
	stefan_url = "https://i.imgur.com/LT3cAQP.jpg"
	init_message_format = \
 "```" \
 + "Press React To Init Turd" \
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
					await TurdCreate(channel, announceChannel)
					await asyncio.sleep(10)
					await message.clear_reactions()
					await message.add_reaction(turd_emoji)


async def TurdCreate(channel, announceChannel):

	messageId = await channel.send(
	 '***TurdLog*** -- Turd Incoming ... React With Rating Of Experience To Deploy Turd -- ***TurdLog*** '
	)

	while True:

		message = await announceChannel.fetch_message(messageId)

		rating_emojis = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣"]

		for i in range(len(rating_emojis)):
				await message.add_reaction(rating_emojis[i])

		for reaction in message.reactions:
			async for user in reaction.users():
				if user.name == "Stefan Hebis":
					print("")
				else:
					await TurdDeploy(channel, announceChannel, reaction, user)
					await message.delete(10)


async def TurdDeploy(channel, announceChannel, reaction):

	print(reaction)

	messageText = f"***TurdLog Notification*** -- Turd (rating: {reaction.emoji}) Deployed By {user.name} ..."

	await channel.send(messageText)
