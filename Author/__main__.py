import pandas as pd
import process
import random
import time
import os

# Get train text
millis 			= int(round(time.time() * 1000))
files 			= os.listdir("../Song Lyrics/Data/Lyrics")
files			= random.sample(files, 5)
LyricsData		= []

for file in files:
	
	df		= pd.read_csv("../Song Lyrics/Data/Lyrics/" + file)
	song 	= ['.'.join(x.splitlines()) for x in df["Lyrics"]]
	LyricsData.append('\n'.join(song))

train 				= '\n'.join(LyricsData)
train 			= process.clean_file(train)

mapFirsts, mapCentres, mapLasts, Firsts, Centres, Lasts = process.create_map(train)

# Map with lag 1 (Hope to create a probabilistic model)

millis			= process.log("Processed document in ", millis, 1)
mapRhymes  		= process.get_rhymes(Lasts)
millis 			= process.log("Created rhyme maps for the document in ", millis, 1)
millis 			= process.log("Now I will start writing!\n", millis, 0)

author.write_poem(Firsts, Centres, Lasts, mapFirsts, mapCentres, mapLasts, mapRhymes, 10, 7)