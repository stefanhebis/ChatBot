import random


def main(namn) -> str:
	race = get_race(namn)
	klass = get_klass(namn)
	alignment = get_alignment()
	strength = random.randint(1, 20)
	dexterity = random.randint(1, 20)
	constitution = random.randint(1, 20)
	intelligence = random.randint(1, 20)
	wisdom = random.randint(1, 20)
	charisma = random.randint(1, 20)
	kar_namn = randomName(race)

	roll_message = \
  "**Character sheet för " + namn + "**\n" \
  + "__Namn:__ " + kar_namn + "\n" \
  + "__Race:__ " + race + "\n" \
  + "__Class:__ " + klass + "\n" \
  + "__Alignment:__ " + alignment + "\n" \
  + "```" \
  + print_stat("Str", strength) + "\n" \
  + print_stat("Dex", dexterity) + "\n" \
  + print_stat("Con", constitution) + "\n" \
  + print_stat("Int", intelligence) + "\n" \
  + print_stat("Wis", wisdom) + "\n" \
  + print_stat("Cha", charisma) \
  + "```"

	return roll_message


def get_race(name) -> str:
	races = [
	 "Dragonborn", "Dwarf", "Elf", "Gnome", "Half-Elf", "Halfling", "Half-Orc",
	 "Human", "Tiefling"
	]

	if name == "Micke":
		races.append("Troll")
	elif name == "Teo":
		races.append("Goblin")

	return random.choice(races)


def get_klass(name) -> str:
	klasser = [
	 "Barbarian", "Bard", "Cleric", "Druid", "Fighter", "Monk", "Paladin",
	 "Ranger", "Rogue", "Sorcerer", "Warlock", "Wizard"
	]

	if name == "Ed":
		klasser.append("Weedlock")
	elif name == "Teo":
		klasser.append("Techno Bard")
	elif name == "Nils":
		klasser.append("Lover")

	return random.choice(klasser)


def get_alignment() -> str:
	alignments = [
	 "Lawful Good", "Neutral Good", "Chaotic Good", "Lawful Neutral",
	 "True Neutral", "Chaotic Neutral", "Lawful Evil", "Neutral Evil",
	 "Chaotic Evil"
	]
	return random.choice(alignments)


def modifier(roll) -> str:
	mod = int(roll / 2 - 5)

	if mod == 0:
		pos = "+"
	elif mod > 0:
		pos = "+"
	else:
		pos = ""

	return "(" + pos + str(mod) + ")"


def print_stat(name, stat) -> str:
	return name + ": " + str(stat).ljust(2) + " - " + modifier(stat)


def randomName(race) -> str:
	firsts = {
	 "Human": [
	  "Jake", "Jim", "Carl", "Roberto", "Julius", "Donald", "Harris", "Carlos",
	  "Strongman", "Wilhelm", "Adolf", "Knut", "Kenneth", "Ian", "Mofo",
	  "Bajsmannen", "Boppe", "Pepe", "Frank", "Tintin", "Franco", "Ralf", "Romeo",
	  "Peder", "Jerry", "Otto", "Kent", "Dick", "Kawa", "Marre", "Edvard", "Nils",
	  "Teodor", "Daniel", "Ale"
	 ],
	 "Elf": [
	  "Caramellio", "Sebasthyon", "Legolas", "Nilsolas", "Tristan", "Fentanyl",
	  "Citrus", "Alvedon", "Silvbert", "Linux", "Marzipanius"
	 ],
	 "Halfling": [
	  "Frodo", "Grodo", "Melvin", "Mapp", "Bilf", "Grogu", "Merry", "Perry",
	  "Pippin", "Sam", "Bongo", "Snoddas", "Bingo", "Milf"
	 ],
	 "Half-Orc": ["Boby", "Fucker", "Micke", "Garg", "Raaagghhhh", "Normalo"],
	 "Dwarf": [
	  "Micke", "Runko", "Gimli", "Osvaldo", "Fernando", "Julio", "Antonio", "Damp"
	 ],
	 "Dragonborn": [
	  "Drake", "Draco", "Draken", "Svärmor", "Exfru", "Nalxestuandor", "Naloxone",
	  "Oxycontin", "Dinosaurius"
	 ],
	 "Tiefling": ["Tiefan", "Moronius", "Dumbassus", "Suckadickir", "Horny"],
	 "Half-Elf": ["Lolo"],
	 "Gnome":
	 ["Liten", "Lille", "Mini", "Smutser", "Toker", "Plutten", "Slimp", "Dorkus"],
	 "Troll": ["Michael"],
	 "Goblin": ["Teodor"],
	 "Skribent": [
	  "Michael", "Edvard", "Owe", "Gunnar", "Börge", "Anders", "Gréger", "Knut",
	  "Göran", "Wilhelm von", "P-e-O", "Paul \"Bingo\"", "Otto", "Åkhe", "Golf",
	  "Lehnart", "Cleo", "Karl-Teodor", "\"M\"", "Rudolf", "Jöran", "Hjohn",
	  "Bimbi", "Mef"
	 ]
	}
	lasts = {
	 "Human": [
	  "Anderson", "Rogers", "Harris", "Hard", "Brown", "Hardbody", "Buff", "Bajs",
	  "Häst", "Kill", "Fighter", "Weedsmoker", "Weed", "Grill", "Fuckington",
	  "Löfvén", "Storkuk", "Snopp", "Keatington", "Travolta", "Pitt", "Hitler"
	 ],
	 "Elf": [
	  "Fjärilsdröm", "Kokos", "Orb", "Sybian", "Gyllenkuk", "Tampong", "Kretinius"
	 ],
	 "Halfling": [
	  "Baggins", "Froggy", "Cruddy", "Gump", "Blob", "Gamgee", "Rökström",
	  "Bongo", "Muffins", "Dolme"
	 ],
	 "Half-Orc": [
	  "Kokos",
	  "Gruff",
	  "Bajs",
	  "Sten",
	  "Röv",
	  "Turd",
	  "Gurk",
	  "Burk",
	 ],
	 "Dwarf": [
	  "Mongo", "Löfvén", "Storkuk", "Dvärgsson", "Llorente", "Torres", "Alba",
	  "Banderas"
	 ],
	 "Dragonborn": [
	  "Draksson", "Drakonius", "Drakström", "Skalman", "Weedburner", "Assfucker",
	  "Thongsong"
	 ],
	 "Tiefling":
	 ["Tiefsson", "Meurling", "Chingy", "DemoniusX", "Joker", "Slok", "Skurk"],
	 "Half-Elf": ["Moce", "Plam"],
	 "Gnome": [
	  "Röv", "Nöt", "Task", "Boll", "Pinne", "Rövpillare", "Lol", "Keso", "Banan",
	  "Sniglet", "Groda", "Mini"
	 ],
	 "Troll": ["Andersson"],
	 "Goblin": ["Meurling"],
	 "Skribent": [
	  "Andersson", "Ekström", "Svenson", "Nilsson", "Karlström", "Wirén",
	  "Bergström-Nylén", "H Pettersson", "Janzon", "Bredäng", "Sportelius",
	  "Bengtén", "Örixon", "Kranströmer", "Bromën", "Lindberg-Berglind",
	  "Maxzelius", "P-son", "Ollberg", "Nilbert", "van Korgh"
	 ]
	}

	first = firsts[race]
	last = lasts[race]

	if race == "Half-Elf":
		if random.choice([True, False]):
			first.extend(firsts["Human"])
			last.extend(lasts["Elf"])
		else:
			first.extend(firsts["Elf"])
			last.extend(lasts["Human"])
	elif race == "Half-Orc":
		if random.choice([True, False]):
			first.extend(firsts["Human"])
			last.extend(lasts["Halfling"])
		else:
			first.extend(firsts["Halfling"])
			last.extend(lasts["Human"])
	elif race == "Goblin":
		if random.choice([True, False]):
			first.extend(firsts["Gnome"])
			last.extend(lasts["Dwarf"])
		else:
			first.extend(firsts["Dwarf"])
			last.extend(lasts["Gnome"])

	name = random.choice(first) + " " + random.choice(last)

	return name