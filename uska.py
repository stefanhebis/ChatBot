import random
import glob

def main() -> str:
	ljud =[
    "Wowawiwa", "Humina humina", "Vilken pangbrud", "Mamma mia", "Awoooooooga", "God dag, min sköna", "Vilken donna", "100% babe", "Wowee zowee", "Mums hehe", "Hälsa på borgmästaren i Babe City"
    ]
	uska_text =  random.choice(ljud) + " !" 
	return uska_text

def pic() -> str:
	pics = glob.glob("uska/*.jpg")
	picture = random.choice(pics)
  
	return picture