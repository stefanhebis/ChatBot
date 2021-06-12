import random
import glob

def main() -> str:

	#kategori = ["gammal", "ung", "naken", "stor"]

	personer = {
    "default": ["Medelålders man", "Oidentifierad person",  "Lokal profil",  "Hemlös man", "Förvirrad man",  "Man i sjukhuskläder",  "FN-veteran", "Populär trädgårdsmästare", "Berusad man", "Man med brännbollsrack",  "Rymling från tvångsvården", "Arg man", "Ensamstående fembarnsfar", "Arbetslös", "Lokal man känd som \"Borgmästarn\"", "Narkotikapåverkad man", "Lokal komikerprofil"],

		"gammal": ["Pensionär", "Äldre man", "Senildement man", ],

		"ung": ["Härjad 23-åring", "Ung man", "Tonåring"],

		"naken": ["Skjortlös person", "Naken man", ],

		"stor": ["Enorm man", "Rundlagd man", "Fet man"],
		}
	aktiviteter = [
    "hittad död", "funnen avliden", "omhändertagen", "anträffad avliden", "arresterad", "inblandad i slagsmål", "skjuten av polis", "biten av hund", "rånad av barn", "misshandlade vårdpersonal", "vandrade naken", "protesterade för apartheid", "återfunnen kraftigt nedkyld", "påkörd av traktor", "eftersökt av polis, senast sedd", "angrep förbipasserande", "rånad och nerslagen", "körde rattfull", "exponerade sig", "gick byxlös", "dödade vän i duell", "vann miljonvinst på upphittad trisslott", "hade alla rätt på tipset efter uppenbarelse", "sålde cigaretter med spikklubba", "dödade travhäst i hämndattack", "dödad i narkotikauppgörelse", "\"bortförd av utomjordingar\"", "såg Bigfoot", "jagade bort Dracula med vitlök", "fick \"provköra vänliga utomjordingars rymdskepp\"", "fast för tobakssmuggling", "gick vilse", "försvunnen", "mobbad av skolbarn", "sålde piratkopierade hockeybilder", "självantände", "hävdar att han såg Gud", "gjorde en deal med djävulen", "sålde originaltavlor av Hitler på bakluckeloppis", "biten av varulv", "gömde sig från en svärm av bin formad som en knytnäve", "upptäckte kall fusion", "tog med sig turister in i Zonen", "fick en killstreak", "fastnade i rulltrappa", "började tala flytande portugisiska efter skallskada till följd av fall"
    ]
	platser = [
    "i grustag", "i dike", "i skogsbryn", "vid fritidshus", "vid avtagsväg", "vid landsväg", "i skogsområde", "i stulen husvagn", "på campingplats", "i bibliotek", "i villaområde", "vid rastplats", "vid förskola", "på offentlig toalett", "i utbränd bil", "på nöjesfält", "i spökhus", "i brunn", "utanför bensinstation", "vid renhållningsverk", "i mataffär", "i galleria", "vid bowlinghall", "på åker", "bredvid stor monolit", "i slottsruin"
    ]
	geografier = [
    "utanför Torslanda", "vid gränsen till Halland", "utanför industriområde", "i närheten av Alingsås", "nära E4:an", "utanför Örkelljunga", "bakom Ica Maxi", "söder om Birsta"
   ]

	personer_kategori = random.choice(list(personer.keys()))

	headline_text = \
    random.choice(list(personer[personer_kategori])) + " " + \
    random.choice(aktiviteter) + " " + \
    random.choice(platser) + " " + \
    random.choice(geografier)

	pics = glob.glob("headline/" + str(personer_kategori) + "/*.jpg")
	picture = random.choice(pics)

	return headline_text, picture

