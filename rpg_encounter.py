import rpg
import rpg_encounters
import discord
from discord.utils import get
import asyncio
import random
from replit import db
from builtins import bot



async def random_encounter(sender, channel, sender_raw) -> str:
	#await rpg.rsend("Encounter !")

	encounter = rpg_encounters.randomEncounter(sender)

	enemy_hp = encounter["hp"]

	await run_encounter(encounter, sender, channel, sender_raw, enemy_hp)

async def run_encounter(encounter, sender, channel, sender_raw, enemy_hp) -> str:

	encounter_image = encounter["imagename"]

	encounter_message = \
	"***" + encounter["titel"] + "***\n" \
	+ "Du stöter på " + encounter["namn"] + "!\n\n" \
	+ "Vad gör du?\n\n" \
	+ "```" \
	+ encounter["emoji1"] + " " + encounter["val1"] + "\n\n" \
	+ encounter["emoji2"] + " " + encounter["val2"] + "\n\n" \
	+ encounter["emoji3"] + " " + encounter["val3"] + "\n\n" \
	+ encounter["emoji4"] + " " + encounter["val4"] + "\n\n" \
	+ "```"

	sent_message = await rpg.esend(encounter_message, channel, encounter_image)

	await sent_message.add_reaction(encounter["emoji1"])
	await sent_message.add_reaction(encounter["emoji2"])
	await sent_message.add_reaction(encounter["emoji3"])
	await sent_message.add_reaction(encounter["emoji4"])

	def check(reaction, user):
		
		return (str(user) == str(sender_raw))
		
	try:
		reaction, user = await bot.wait_for(event="reaction_add", timeout=60, check=check)
		
	except asyncio.TimeoutError:
			
			return
				
	else:
		
		if str(reaction.emoji) == encounter["emoji1"]:
			nr = "1"
		if str(reaction.emoji) == encounter["emoji2"]:
			nr = "2"
		if str(reaction.emoji) == encounter["emoji3"]:
			nr = "3"
		if str(reaction.emoji) == encounter["emoji4"]:
			nr = "4"
		
		stat = str(encounter["stat"+nr])
		attack = str(encounter["attack"+nr])
		ge_skada = str(encounter["ge_skada"+nr])
		ge_mycket_skada = str(encounter["ge_mycket_skada"+nr])
		ta_skada = str(encounter["ta_skada"+nr])
		ta_mycket_skada = str(encounter["ta_mycket_skada"+nr])
		dodsrossling = str(encounter["dodsrossling"])
		triumf = str(encounter["triumf"])
		enemystat = encounter[stat]
		enemyhp = enemy_hp

		resolve = await encounterChallenge(stat, attack, ge_skada, ge_mycket_skada, ta_skada, ta_mycket_skada, dodsrossling, triumf, enemystat, enemyhp, sender, channel)

		if resolve[0]:
			await run_encounter(encounter, sender, channel, sender_raw, resolve[1])

		



async def encounterChallenge(stat, attack, ge_skada, ge_mycket_skada, ta_skada, ta_mycket_skada, dodsrossling, triumf, enemystat, enemyhp, sender, channel):
	powner = str("rpg+" + sender)
	
	challenge_stat = str(stat)
	if challenge_stat == "strength" or "dexterity":
		health_stat = "constitution"
	if challenge_stat == "intelligence" or "charisma":
		health_stat = "wisdom"

	character_hp = db[powner+health_stat]
	enemy_hp = enemyhp
	character_namn = db[powner+"charname"]

	character_stat = db[powner+challenge_stat] 

	character_t20 = random.randint(1,20)
	enemy_t20 = random.randint(1,20)

	enemyroll = enemystat + enemy_t20
	characterroll = character_stat + character_t20

	roll = characterroll - enemyroll

	damage = roll

	roll_text = \
	"```" \
	+ "Du rullar " + str(characterroll) + "(" + str(character_stat) + " plus t20(" + str(character_t20) + "))\n" \
	+ "Fienden rullar " + str(enemyroll) + "(" + str(enemystat) + " plus t20(" + str(enemy_t20) + "))\n" \
	+ "Total roll: " + str(roll) \
	+ "\n```" 


	dmg_text = attack
	
	if damage > 0:
		skada = "gör"
		txt = ge_skada
	if damage > 10:
		skada = "gör"
		txt = ge_mycket_skada
	if damage < 0:
		skada = "tar"
		txt = ta_skada
	if damage < -10:
		skada = "tar"
		txt = ta_skada

	skada_text = "\n" + character_namn + " " + skada + " " + str(damage) + " skada!\n"
	
	char_hp_text = character_namn + "s kvarvarande hp: " + str(character_hp)
	hp_text = "\nfiendens kvarvarande hp: " + str(enemy_hp)

	dmg_text = dmg_text + txt + skada_text + roll_text + char_hp_text + hp_text

	await rpg.send(dmg_text, channel)

	if skada == "gör":
		enemy_hp -= damage
		if enemy_hp < 0:
			await winEncounter(sender, channel, dodsrossling)
			return False, 0
		else:
			return True, enemy_hp
	elif skada == "tar":
		character_hp += damage
		db[powner+health_stat] = character_hp
		if character_hp < 1:
			await loseEncounter(sender, channel, triumf)
			return False, 0
		else:
			return True, enemy_hp

	


async def winEncounter(sender, channel, dodsrossling):
	wintext = \
	"```" \
	+ dodsrossling \
	+ "```\n" \
	+ "Du segrade i striden!"

	await rpg.send(wintext, channel)

async def loseEncounter(sender, channel, triumf):
	powner = str("rpg+" + sender)
	
	losetext = \
	"```" \
	+ triumf \
	+ "```\n" \
	+ "Du stupade i striden!"

	db[powner+"levande"] = "nej"

	await rpg.send(losetext, channel)



	
	
			

