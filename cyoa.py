import discord
from discord.utils import get
import random
import asyncio

async def main(channel, debuginit):
	debug = False
	
	await playAdventure(channel, debug)

async def playAdventure(channel, debug):
	page = 1
	await Prompt(channel, page, debug)

async def endAdventure(channel, debug):
	end_message = \
	"```" \
	+ "Slutet gott, allting gott...?" \
	+ "```" 
	await channel.send(end_message)

async def Prompt(channel, page, debug):
	End = getEnd(page)
	
	prompt_message = str(renderPromptMessage(page, End))
	sent_message = await channel.send(prompt_message)

	if End:	
		await endAdventure(channel, debug)

	else:
		refers = getRefer(page)
		first_refer = refers[0]
		second_refer = refers[1]
		await sent_message.add_reaction("1️⃣")
		await sent_message.add_reaction("2️⃣")
		await asyncio.sleep(20)
		voteresult = await Vote(channel, sent_message.id, debug, first_refer, second_refer)

		refer = str(voteresult[0])
		returntext = str(voteresult[1])

		reply_message_text = adventure[str(page)][returntext]
		reply_message = \
			"```" \
			+ str(reply_message_text) \
			+ "```" 

		await channel.send(reply_message)

		await Prompt(channel, refer, debug)

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
		return first_refer, "first.return"
	elif second_r > first_r:
		return second_refer, "second.return"
	else:
		return random.randint(1,2)

def renderPromptMessage(page, end):
	# todo stöd för fler val !
	
	prompt_t = adventure[str(page)]["prompt.text"]

	if not end:
		first_t = adventure[str(page)]["first.text"]
		second_t = adventure[str(page)]["second.text"]
		prompt_message = \
		"```" \
		+ prompt_t \
		+ "\n" \
		+ "\n" \
		+ "\n" \
		+ "--- \n" \
		+ "1️⃣: " \
		+ first_t \
		+ "\n" \
		+ "2️⃣: " \
		+ second_t \
		+ "```" 

	end_message = \
		"```" \
		+ prompt_t \
		+ "```" \
	
	if end:
		return end_message
	else:
		return prompt_message

def getRefer(page):
	first_refer = adventure[str(page)]["first.refer"]
	second_refer = adventure[str(page)]["second.refer"]

	return first_refer, second_refer

def getEnd(page):
	End = adventure[str(page)]["ending"]
	return End



adventure = {
	"1": {
		"prompt.text": "Mitt namn är Teo och jag jobbar i dildofabriken.\nKlockan ringer! Dags att vakna och åka till jobbet!", 
		"first.text": "Jag cyklar till jobbet på min enhjuling.", 
		"first.refer": 2, 
		"first.return": "Pling pling! Ur vägen!",
		"second.text": "Jag flyger till jobbet i mitt lilla propellerplan.", 
		"second.return": "Brum brum! Det är helt normalt att flyga propellerplan till jobbet faktiskt.",
		"second.refer": 2,
		"ending": False},

	"2": {
		"prompt.text": "Äntligen på jobbet! Dags att suga dildos!\nPå vägen till dildosugarrummet går jag förbi en kollega.", 
		"first.text": "Hej Stefan!",
		"first.refer": 3,
		"first.return": "Hej Stefan!",
		"second.text": "Ingen tid för snack - det finns dildos att suga!", 
		"second.return": "Ingen tid för snack - det finns dildos att suga!",
		"second.refer": 4,
		"ending": False},

	"3": {
		"prompt.text": "Hej Teo! svarar min kollega Stefan Hebis.", 
		"first.text": "Hej Stefan!", 
		"first.return": "Hej Stefan!",
		"first.refer": 3, 
		"second.text": "Hejdå Stefan!", 
		"second.return": "Hejdå Stefan!", 
		"second.refer": 4, 
		"ending": False},

	"4": {
		"prompt.text": "Äntligen framme i dildosugarrummet. Nu är det dags för mitt jobb att börja!", 
		"first.text": "Mums!", 
		"first.return": "Mums!",
		"first.refer": 5, 
		"second.text": "Smask!",
		"second.return": "Smask!",
		"second.refer": 5,
		"ending": False},

	"5": {
		"prompt.text": "Ja älsk å sug dildos ja!",
		"ending": True},
	
}
