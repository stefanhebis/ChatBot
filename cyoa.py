import discord
from discord.utils import get
import random
import asyncio

async def main(channel, debuginit):

	debug = False
	# init cyoa
	# printa prompt från adventures
	#if not adventure:
	#	adventure = 1
	
	await playAdventure(channel, debug)

async def playAdventure(channel, debug):
	page = 1
	
	vinst = 0

	if vinst == 0:
		await Prompt(channel, page, debug)


async def Prompt(channel, page, debug):
	prompt_message = str(renderPromptMessage(page))

	refers = getRefer(page)
	first_refer = refers[0]
	second_refer = refers[1]

	sent_message = await channel.send(prompt_message)
	await sent_message.add_reaction("1️⃣")
	await sent_message.add_reaction("2️⃣")
	await asyncio.sleep(20)
	voteresult = await Vote(channel, sent_message.id, debug, first_refer, second_refer)
	await Prompt(channel, voteresult, debug)

async def Vote(channel, message_id, debug, first_refer, second_refer):
	
	first_refer = first_refer
	second_refer = second_refer

	message = await channel.fetch_message(message_id)

	first_reactions = get(message.reactions, emoji='1️⃣')
	first_r = first_reactions.count

	second_reactions = get(message.reactions, emoji='2️⃣')
	second_r = second_reactions.count

	if debug:
		await message.channel.send(first_r)
		await message.channel.send(second_r)

	if first_r > second_r:
		return first_refer
	elif second_r > first_r:
		return second_refer
	else:
		return random.randint(1,2)

def renderPromptMessage(page):
	adventure_content = adventure[str(page)]
	prompt_t = adventure_content[0]
	first_t = adventure_content[1]
	second_t = adventure_content[3]
	
	#if adventure_content[6]:
	#	third_t = adventure_content[6]
	#if adventure_content[7]:
	#	third_r = adventure_content[7]
	#if adventure_content[8]:
	#	vinstsida = adventure_content[8]

	prompt_message = \
		"```" \
		+ prompt_t \
		+ "```" \
		+ "\n" \
		+ "```" \
		+ "1️⃣: " \
		+ first_t \
		+ "```" \
		+ "\n" \
		+ "```" \
		+ "2️⃣: " \
		+ second_t \
		+ "```" 
	return prompt_message

def getRefer(page):
	refer_content = adventure[str(page)]

	first_refer = refer_content[2]
	second_refer = refer_content[4]

	return first_refer, second_refer






adventure = {
	"1": [
		"Du möter en ensam vandrare. Vad gör du?", 
		"Jag går till havet.", 2, 
		"Jag går till skogs.", 3],

	"2": [
		"Du är vid havet. Nu då?", 
		"Gå tillbaks till vandraren.", 1, 
		"Gå till skogs.", 3],

	"3": [
		"Du är i skogen. Du kommer att dö här.", 
		"Gå o skit på dej!", 4, 
		"Gå o dö i havet!", 2],

	"4": [
		"Du är på väg någonstans illa.", 
		"Skiter jag i.", 4, 
		"Sug min jerry!", 1],
}
