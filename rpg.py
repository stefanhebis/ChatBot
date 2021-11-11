from builtins import bot

import rpg_roll
import rpg_character
import rpg_encounter
import discord


from discord.ext import commands
from discord import Embed

send_channel = 828918567712849920
stefan_url = "https://i.imgur.com/LT3cAQP.jpg"

async def action(command, sender, channel, sender_raw) -> str:
	print(str(command))
	

	if command == "roll":
		await rpg_roll.roll(sender, channel, "nej")

	if command == "reroll":
		await rpg_roll.roll(sender, channel, "ja")

	if command == "character":
		await rpg_character.showCharacter(sender, channel)

	if command == "encounter":
		await rpg_encounter.random_encounter(sender, channel, sender_raw)
	


	return

async def send(text, channel):
	embed=Embed(title="Stefan RPG", color=0x737ad9)
	embed.set_author(name="Stefan Hebis", icon_url=stefan_url)
	embed.set_thumbnail(url=stefan_url)
	embed.add_field(name="Stefan RPG", value=text, inline=False)
	embed.set_footer(text="/ Stefan")
	await channel.send(embed=embed)
	
async def esend(text, channel, encounter_image):

	
	with open(encounter_image, 'r+b') as file:
			f = discord.File(file, "encounter.png")

	embed=Embed(title="Stefan RPG", color=0x737ad9)
	embed.set_author(name="Stefan Hebis", icon_url=stefan_url)
	embed.set_thumbnail(url=stefan_url)
	
	#embed.set_image(url="attachment://encounter.png")
	embed.add_field(name="Stefan RPG", value=text, inline=False)
	embed.set_footer(text=" ")
	sent_message = await channel.send(embed=embed, file=f)

	return sent_message
	