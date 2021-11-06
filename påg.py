import random
import glob

def main() -> str:
	påg_text =  "Påg !" 
	return påg_text

def pic() -> str:
	pics = glob.glob("påg/*.*")
	picture = random.choice(pics)
  
	return picture