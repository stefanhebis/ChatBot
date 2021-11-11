from replit import db
import rpg

def characterExists(owner) -> str:
	keys = db.prefix("rpg+")

	for character in keys:
		powner = str("rpg+" + owner)
		if not db[powner+"levande"]:
			db[powner+"levande"] = "nej"
			return False

		if db[powner+"levande"] == "ja":
				return True
		else:
				return False

		

async def addCharacter(owner, channel, race, klass, alignment, strength, dexterity, constitution, intelligence, wisdom, charisma, charname) -> str:
	
	powner = str("rpg+" + owner)

	db[powner+"race"] = race
	db[powner+"klass"] = klass
	db[powner+"alignment"] = alignment
	db[powner+"strength"] = strength
	db[powner+"dexterity"] = dexterity
	db[powner+"constitution"] = constitution
	db[powner+"intelligence"] = intelligence
	db[powner+"wisdom"] = wisdom
	db[powner+"charisma"] = charisma
	db[powner+"charname"] = charname
	db[powner+"levande"] = "ja"
	db[powner+"level"] = 1
	db[powner+"xp"] = 0

	await showCharacter(owner, channel)

async def showCharacter(owner, channel) -> str:

		powner = str("rpg+" + owner)

		roll_message = \
	 		"**Character sheet för " + owner + "**\n" \
	 		+ "__Namn:__ " + db[powner+"charname"] + "\n" \
	 		+ "__Race:__ " + db[powner+"race"] + "\n" \
	 		+ "__Class:__ " + db[powner+"klass"] + "\n" \
	 		+ "__Alignment:__ " + db[powner+"alignment"] + "\n" \
	 		+ "```" \
	 		+ print_stat("Str", db[powner+"strength"]) + "\n" \
	 		+ print_stat("Dex", db[powner+"dexterity"]) + "\n" \
	 		+ print_stat("Con", db[powner+"constitution"]) + "\n" \
	 		+ print_stat("Int", db[powner+"intelligence"]) + "\n" \
	 		+ print_stat("Wis", db[powner+"wisdom"]) + "\n" \
	 		+ print_stat("Cha", db[powner+"charisma"]) + "\n" \
			+ "```" + "\n" \
			+ "__Level:__ " + str(db[powner+"level"]) + "\n" \
			+ "__Experience:__ " + str(db[powner+"xp"]) \
	 		

		await rpg.send(roll_message, channel)

def print_stat(name, stat) -> str:
	return name + ": " + str(stat).ljust(2) + " - " + modifier(stat)

def modifier(roll) -> str:
	mod = int(roll/2-5)

	if mod == 0:
		pos = "+"
	elif mod > 0:
		pos = "+"
	else:
		pos = ""

	return "(" + pos + str(mod) + ")"

	
		
		

	
	