import process

train 			= process.clean_file(train)

mapFirsts, mapCentres, mapLasts, Firsts, Centres, Lasts = process.create_map(train)

# Map with lag 1 (Hope to create a probabilistic model)

millis			= process.log("Processed document in ", millis, 1)
mapRhymes  		= process.get_rhymes(Lasts)
millis 			= process.log("Created rhyme maps for the document in ", millis, 1)
millis 			= process.log("Now I will start writing!\n", millis, 0)

author.write_poem(Firsts, Centres, Lasts, mapFirsts, mapCentres, mapLasts, mapRhymes, 10, 7)