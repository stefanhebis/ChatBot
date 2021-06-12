import random
from replit import db

def main(init):
  if init == True:
    misogyny = random.randint(1,4)
    name_calling = random.randint(1,4)
    n_word = random.choice([True, False])
    racism = random.randint(1,4)
    swearing = random.randint(1,4)
  else:
    try:
      misogyny = db["misogyny"]
      name_calling = db["name_calling"]
      n_word = db["n_word"]
      racism = db["racism"]
      swearing = db["swearing"]
    except:
      misogyny = random.randint(1,4)
      name_calling = random.randint(1,4)
      n_word = random.choice([True, False])
      racism = random.randint(1,4)
      swearing = random.randint(1,4)

  #misogyny = rand(misogyny)
  #name_calling = rand(name_calling)
  #if random.choice([True, False]): n_word = random.choice([True, False])
  #racism = rand(racism)
  #swearing = rand(swearing)

  db["misogyny"] = misogyny
  db["name_calling"] = name_calling
  db["n_word"] = n_word
  db["racism"] = racism
  db["swearing"] = swearing

  rad = random.randint(0,5)
  misogyny_text = line(misogyny, rad)
  name_calling_text = line(name_calling, rad)
  racism_text = line(racism, rad)
  swearing_text = line(swearing, rad)

  if n_word:
    n_word_text = "…………👍"
  else:
    n_word_text = "👎…………"

  #if init == True:
  header = "DAGENS INSTÄLLNINGAR"
  #else:
  #  header = "NYA INSTÄLLNINGAR"
  
  bleep_message = "***" + header + "***" + "\n```    MISOGYNI: " + misogyny_text + "\nFÖROLÄMPNING: " + name_calling_text + "\n       N-ORD: " + n_word_text + "\n      RASISM: " + racism_text + "\n   SVORDOMAR: " + swearing_text + "```"

  return bleep_message

def rand(variabel) -> int:
  variabel = max(1, min(variabel, 4))
  
  if random.choice([True, False]):
    if variabel == 4:
      variabel = variabel + random.randint(-1,0)
    elif variabel == 1:
      variabel = variabel + random.randint(0,1)
    else:
      variabel = variabel + random.randint(-1,1)

  return variabel

def getEmoji(variabel, rad) -> str:
    emojis = [
      ["😇", "😌", "😉", "🤨"],
      ["🥰", "😏", "😘", "😍"],
      ["😋", "😝", "😜", "🤪"],
      ["😅", "😓", "😰", "🥶"],
      ["🤏", "☝️", "👌", "🤌"],
      ["👋", "🤙", "💪", "🤝"]
    ]
      #["", "", "", ""]

    emoji = emojis[rad][variabel-1]
    return emoji

def line(variabel, rad) -> str:
  var_text = ""
  for i in range(1,5):
    if variabel == i:
      if i == 4: var_text = var_text + "…"
      var_text = var_text + getEmoji(variabel, rad)
    else:
      var_text = var_text + "…"
    if i < 4:
      var_text = var_text + "…………"

  return var_text

def getMood() -> str:
  misogyny = db["misogyny"]
  name_calling = db["name_calling"]
  racism = db["racism"]
  swearing = db["swearing"]

  moods = [
    ["misogyni", misogyny], 
    ["förolämpning", name_calling], 
    ["rasism", racism], 
    ["svordomar", swearing]
  ]
  moods = sorted(moods, key=lambda l:l[0], reverse=False)

  #print(moods)

  if moods[0][1] <= 2:
    return "angle"
  elif moods[0][1] == moods[1][1]:
    if moods[1][1] == moods[2][1]:
      if moods[2][1] == moods[3][1]:
        return "devil"
      else:
        return random.choice([moods[0][0], moods[1][0], moods[2][0]])
    else:
      return random.choice([moods[0][0], moods[1][0]])
  else:
    return moods[0][0]