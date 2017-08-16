import time
import string
import random

def process_files(files):
	train = ""
	for file in files:
		doc = open(file)
		doc = doc.read()
		train += doc + "\n" 

	return train


def clean_file(train):
	train = train.replace("\n", " ")
	train = train.decode('string_escape')
	# train = train.lower()
	train = train.split(".")
	train = [x.translate(string.maketrans("",""), string.punctuation) for x in train]
	return train

def log(phrase, millis, flag):
	if(flag == 1):
		millis = int(round(time.time() * 1000))-millis
		print(phrase + str(millis))	
		millis = int(round(time.time() * 1000))
	else:
		print(phrase)
	return(millis)

def create_map(train):

	Firsts 	= []
	Lasts 	= []
	Centres = []

	mapFirsts 		= {}
	mapCentres 		= {}
	mapLasts 		= {}
	for i in range(len(train)):
		sentence = train[i]
		sentence = sentence.split(" ")
		if(len(sentence) > 1):
			Firsts.append(sentence[0])
			mapFirsts[sentence[0]] = mapFirsts.get(sentence[0], []) + [sentence[1]]
			for j in range(1,len(sentence)-1):
				Centres.append(sentence[j])
				mapCentres[sentence[j-1]] = mapCentres.get(sentence[j-1], []) + [sentence[j]]
			Lasts.append(sentence[len(sentence)-1])
			mapLasts[sentence[len(sentence)-1]] = mapLasts.get(sentence[len(sentence)-1], []) + [sentence[len(sentence)-2]]
	return([mapFirsts, mapCentres, mapLasts, Firsts, Centres, Lasts])


def get_rhymes(Lasts):
	mapRhymes = {}
	for i in range(len(Lasts)):
		if(len(Lasts[i])>1):
			ending 				=  Lasts[i][len(Lasts[i]) - 2:]
			mapRhymes[ending] 	= mapRhymes.get(ending, []) + [Lasts[i]]
	return(mapRhymes)