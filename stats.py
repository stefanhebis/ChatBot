import random

def main(namn) -> str:
  print_iq = get_iq()
  print_fukt = get_fukt()
  print_hl = get_hl(namn)

  stats_message = "**STATS FÖR " + str(namn).upper() + "**\n" + print_iq + "\n" + print_fukt + "\n" + print_hl

  return stats_message

def get_iq():
  iq = random.randint(1,100)
  iq_str = str(iq)

  if iq <= 10: iq_message = "damn fkn neandertalare!"
  if 10 <= iq <= 20: iq_message = "idiotjävel lmao. riktigt korkad"
  if 20 <= iq <= 30: iq_message = "pucko som fan..."
  if 30 <= iq <= 40: iq_message = "snubben behövde gå om ettan  fem gånger lol"
  if 40 <= iq <= 50: iq_message = "lol denna knasten kan typ inte skriva sitt eget namn"
  if 50 <= iq <= 60: iq_message = "lagom iq.. inget konstigt"
  if 60 <= iq <= 70: iq_message = "kan typ femhundra ord O_O"
  if 70 <= iq <= 80: iq_message = "smart jävel! ye !"
  if 80 <= iq <= 90: iq_message = "wow denna jäveln kan typ alla tal i hela världen...."
  if 90 <= iq <= 100: iq_message = "snubben e fkn Ainstain.."
  if iq == 100: iq_message = "hooly shit perfekt iq....!!!"
  if iq == 69: iq_message = "nice :P"

  return_iq_message = "__IQ: " + iq_str + "__ " + " - \"" + iq_message + "\""
  return return_iq_message

def get_fukt():
  fukt = random.randint(1,10)
  fukt_str = str(fukt)

  if fukt <= 2: fukt_message = "snustorr o_O inte bra!"
  if 2 <= fukt <= 4: fukt_message = "lite småfuktig men mest torr tbh"
  if 4 <= fukt <= 6: fukt_message = "halvfuktig.."
  if 6 <= fukt <= 8: fukt_message = "fuktig! blöt! ye"
  if 8 <= fukt <= 10: fukt_message = "mycket mycket fuktig!! :P"
  if fukt == 10: fukt_message = "yooo killen e VÅT .. torka av dig !"

  return_fukt_message = "__Fukt: " + fukt_str + "__ " + " - \"" + fukt_message + "\""
  return return_fukt_message

def get_hl(name):
  if name == "Danne":
      hl = random.randint(6,10)
  else:
      hl = random.randint(1,10)
  
  hl_str = str(hl)
  if hl <= 2: hl_message = "noll bånge öht.."
  if 2 <= hl <= 4: hl_message = "lite pirrig kanske :P"
  if 4 <= hl <= 6: hl_message = "halvsvullen.."
  if 6 <= hl <= 8: hl_message = "tänker på brudar o svetten lackar hehe .. je"
  if 8 <= hl <= 10: hl_message = "daaamn denna snubben e KÅT !!"
  if hl == 10: hl_message = "awoooga!! ta en kalldusch kompis!!!!"

  return_hl_message = "__HL: " + hl_str + "__ " + " - \"" + hl_message + "\""
  return return_hl_message
