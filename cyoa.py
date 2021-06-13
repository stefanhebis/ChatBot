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

	refers = getRefer(page)
	first_refer = refers[0]
	second_refer = refers[1]

	sent_message = await channel.send(prompt_message)

	if End:
		await endAdventure(channel, debug)

	else:
		await sent_message.add_reaction("1️⃣")
		await sent_message.add_reaction("2️⃣")
		await asyncio.sleep(20)
		voteresult = await Vote(channel, sent_message.id, debug, first_refer, second_refer)
		# todo skicka ett litet svar efter val
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

def renderPromptMessage(page, end):
	#ska fixa bättre data system :)
	# todo stöd för fler val !
	adventure_content = adventure[str(page)]
	prompt_t = adventure_content[0]
	first_t = adventure_content[1]
	second_t = adventure_content[3]
	

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
	refer_content = adventure[str(page)]

	first_refer = refer_content[2]
	second_refer = refer_content[4]

	return first_refer, second_refer

def getEnd(page):
	end_content = adventure[str(page)]

	End = end_content[5]

	return End



# det är detta som ska bli bättre asså
adventure = {
	"1": [
		"Mitt namn är Teo och jag jobbar i dildofabriken. \n Klockan ringer! Dags att vakna och åka till jobbet!", 
		"Jag cyklar till jobbet på min enhjuling.", 2, 
		"Jag flyger till jobbet i mitt lilla propellerplan.", 2,
		False],

	"2": [
		"Äntligen på jobbet! Dags att suga dildos! \n På vägen till dildosugarrummet går jag förbi en kollega.", 
		"Hej Stefan!", 3, 
		"Ingen tid för snack - det finns dildos att suga!", 4,
		False],

	"3": [
		"Hej Teo! svarar min kollega Stefan Hebis.", 
		"Hej Stefan!", 3, 
		"Hejdå Stefan!", 4, 
		False],

	"4": [
		"Äntligen framme i dildosugarrummet. Nu är det dags för mitt jobb att börja!", 
		"Mums!", 5, 
		"Smask!", 5,
		False],
	"5": [
		"Ja älsk å sug dildos ja!",
		"",5,
		"",5,
		True],
	
}
