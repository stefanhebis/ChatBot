import discord
from discord.utils import get
import random
import asyncio

async def main(channel, debuginit):

	debug = True
	# init cyoa
	# printa prompt från adventures
	#if not adventure:
	#	adventure = 1
	
	await playAdventure(channel, debug)

async def playAdventure(channel, debug):
	page = 1
	nextpage = 0
	vinst = 0

	if vinst == 0:
		await Prompt(channel, page, debug)


async def Prompt(channel, page, debug):
	prompt_message = str(renderPromptMessage(page))
	sent_message = await channel.send(prompt_message)
	await sent_message.add_reaction("1️⃣")
	await sent_message.add_reaction("2️⃣")
	await asyncio.sleep(3)
	voteresult = await Vote(sent_message, debug)
	await Prompt(channel, voteresult, debug)

async def Vote(message, debug):
	reaction_list = message.reactions
	
	first = 0
	second = 0

	first += int(reaction_list.count) 
	second += int(reaction_list.count)
		
	if debug:
		await message.channel_send(str(reaction_list))
		await message.channel.send(first)
		await message.channel.send(second)

	if first > second:
		return 1
	if second > first:
		return 2
	else:
		return random.randint(1,2)

def renderPromptMessage(page):
	adventure_content = adventure[str(page)]
	prompt_t = adventure_content[0]
	first_t = adventure_content[1]
	first_r = adventure_content[2]
	second_t = adventure_content[3]
	second_r = adventure_content[4]
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






adventure = {
	"1": ["Du möter en ensam vandrare. Vad gör du?", "Jag går till havet.", "2", "Jag går till skogs.", "3"],
	"2": ["Du är vid havet. Nu då?", "Gå tillbaks till vandraren.", "1", "Gå till skogs.", "3"],
	"3": ["Du är i skogen. Du kommer att dö här."],
}
