import process
import random

def write_poem(Firsts, Centres, Lasts, mapFirsts, mapCentres, mapLasts, mapRhymes, lines, catches):
	millis = 0
	for i in range(lines):
		line1 	= random.choice(Firsts)	
		word  	= random.choice(mapFirsts[line1])
		line1 	= line1 + " " + word
		for i in range(catches - 2):
			word 	= random.choice(mapCentres[word])
			line1 	= line1 + " " + word
		
		while(True):
			wordl 	= random.choice(Lasts)
			if(len(wordl)>1):
				word1 	= random.choice(mapLasts[wordl])
				if(word1 in mapCentres[word]):
					line1 	= line1 + " " + word1 + " "  + wordl + ",\n"
					endword = random.choice(mapRhymes[wordl[len(wordl)-2:]])
					break
		
		process.log(line1, millis, 0)

		line1 	= random.choice(Firsts)	
		word  	= random.choice(mapFirsts[line1])
		line1 	= line1 + " " + word
		for i in range(catches - 2):
			word 	= random.choice(mapCentres[word])
			line1 	= line1 + " " + word

		while(True):
			wordl = random.choice(mapRhymes[wordl[len(wordl)-2:]])
			if(len(wordl)>1):
				word1 	= random.choice(mapLasts[wordl])
				if(word1 in mapCentres[word]):
					line1 	= line1 + " " + word1 + " "  + wordl + ",\n"
					endword = random.choice(mapRhymes[wordl[len(wordl)-2:]])
					break

		process.log(line1, millis, 0)