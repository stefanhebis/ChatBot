import random
import glob
import roll

def main() -> str:

	skribent = roll.randomName("Skribent")
	tidningsnamn = tidning()

#
#
# uppmaning målgrupp aktiviteter tidplats

	uppmaning = ["10 skäl att", "Varför jag anser att", "Vi borde prata mer om att", "Det är dags att bryta tystnaden om hur", "Är det bara jag som tycker att", "Varför pratar ingen om att", "För mig är det självklart att", "Löfvén vill inte prata om att", "Min fru berättade för mig att"
    
    ]
	målgrupp = ["tonåringar", "nyinflyttade", "långtidssjuka", "skolungdomar", "invandrare", "unga flickor", "äldre män", "mentalt sjuka", "stafettläkare", "EU-migranter", "fagra unga män", "mopedbilsförare", "homofiler", "invandrargäng", "fibromyalgisjuka", "starka och långa män", "vi som har höga fuktnivåer", "vi som lätt blir sexuellt upphetsade", "alla med körkort"
    
    ]
	aktiviteter = ["borde dra upp sina byxor", "borde visa hänsyn", "påverkar tryggheten", "kostar staten pengar", "skapar bekymmer för polisen", "monterar ned vår frihet", "tar skada av att leva", "förstör stadsbilden", "känner sig \"kränkta\"", "har slutat läsa böcker", "är ett hot mot vårt sätt att leva", "skapar oro", "inte visar respekt", "har bristfällig intimhygien", "skapar glädje och lust", "röstar på socialdemokraterna"    
    ]
	tidplats = ["idag", "i vår samtid", "i kollektivtrafiken", "i Örkelljunga", "på äldreboenden", "på landsbygden", "i Torslanda", "i Malungs kommun", "i våra bibliotek", "bland våra kvinnor", 
   ]

#
#
#
# koncept - retorisk_fraga?
	koncept = ["Tredje vågens feminism", "Toppstyre i Stockholmsregionen", "Ökande brist på respekt", "Landsbygdens avbefolkning", "Skjutningar på öppen gata", "Politisk korrekthet", "\"Den svenska situationen\"", "Aktivistiska familjerättsadvokater",
	"Den ökande polariseringen", "Dagens samtalsklimat",
	"Tyrannisk Systembolaget-personal", "Alkoholmonopolet", "Sjöfyllerilagen från 2010",
	"Hot och hat mot oliktänkande", "De riktiga problemen", "Båda sidors extremism"]

	retorisk_fråga = ["är det okej", "ska det vara så", "vems fel är det", "är det ett problem", "vem ligger bakom", "vad ligger bakom", "hur kom vi hit", 
	"vad säger Löfvén", "vem har vi att skylla", 
	"vem vågar stå till svars", "är det inte dags att tala sanning nu", "går det att ha en mogen debatt"]

	#
	#
	#
	# Nej, person, det är inte "ord" med foreteelse

	person = ["Stefan Löfvén", "Annie Lööf", "demokratins fiender", "feminister" , "Vänsterpartiet", "Socialdemokraterna"]

	ord = ["episkt", "coolt", "okej", "inne", "swag"]

	företeelse = ["korrupta tjänstemän", "omvänd rasism", "rasism mot vita ensamstående män", "manshat", "extremfeminism",
	"våldsglorifierande hip-hop", "anti-entreprenöriell kulturpolitik", "antivitism", "hatkampanjer mot frihetsälskare",
	"godhetsknarkande" 
	]


	headline_design =  random.choice([1, 2, 3])

	if headline_design == 1:
		headline_text = \
		"**" + \
    random.choice(uppmaning) + " " + \
    random.choice(målgrupp) + " " + \
    random.choice(aktiviteter) + " " + \
    random.choice(tidplats) + "**" + "\n" + \
		"*" + skribent + ", " + tidningsnamn + "*"

	elif headline_design == 2:
		headline_text = \
		"**" + \
		random.choice(koncept) + " – " + \
		random.choice(retorisk_fråga) + "?" + "**" + "\n" + \
		"*" + skribent + ", " + tidningsnamn + "*"

	elif headline_design == 3:
		headline_text = \
		"**" + \
		"Nej, " + \
		random.choice(person) + ", "+ \
		"det är inte" + " \"" + \
		random.choice(ord) + "\" " + \
		"med " +	random.choice(företeelse) + "**" + "\n" + \
		"*" + skribent + ", " + tidningsnamn + "*"

		



	return headline_text

def pic() -> str:
  pics = glob.glob("byline/*.jpg")
  picture = random.choice(pics)
  
  return picture

def tidning() -> str:
	tidning1 = ["Skåne", "Nya ", "Fria ", "Sydskånska ", "Alingsås", "Nerike", "Östgöta", "Svenska ", "Oberoende ", "Särskilda ", "Dagliga ", "Sörmlands"]

	tidning2 = ["demokraten", "tidningen", "nyheter", "nytt", "bladet", "kuriren", "allehanda", "liberalen"]

	tidningsnamn = random.choice(tidning1) + random.choice(tidning2)

	return tidningsnamn