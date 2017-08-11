# -*- coding: utf-8 -*-

#
#	Script to get song urls and store in
#	batches of 5000 in the Data folder using
#	ArtistUrl.csv. The data is scraped over from 
#	lyrics.com
#

import time
import string
import urllib2
import requests
import pandas as pd
from bs4 import BeautifulSoup

# Initialisations for proxy and other metas to be used later
proxies = {
  'http': 'http://172.16.114.112:3128/',
  'https': 'http://172.16.114.112:3128/',
}

bands	= []
songs 	= []
urls 	= []
millis 	= int(round(time.time() * 1000))
base 	= "http://www.lyrics.com/"

# Data frame with all the artist data in Band name -> Url format
df 		= pd.read_csv("Data/Artist/ArtistUrl.csv")

for i in range(116001,len(df)):
	
	print("Working for " + df['Artist'][i] + ", i : " + str(i))
	
	# Continuous tries to avoid breaking in between and without data
	while(True):

		try:
			webp = requests.get(base + df['Urls'][i], proxies = proxies)
			break
		
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			time.sleep(20)


	# Basic pre processing
	html 	= webp.content
	soup 	= BeautifulSoup(html,'lxml')
	metas 	= soup.findAll('table', class_="tdata")


	# Initialisation to get song count
	num 	= 0


	for meta in metas:
		
		# Getting all anchor tags representing songs (huge!!!)
		rows 	= meta.findAll('a')

		try:
			url 	= [x["href"] for x in rows]
			name 	= [x.find(text=True).encode('utf-8') for x in rows]

			# Simple concatenation
			songs 	+= name
			urls 	+= url
			bands 	+= [df['Artist'][i]]*len(url)
			num 	+= len(url)
		except:
			print("Nonetype error!")
	# Log comment
	print("Done for " + df['Artist'][i])
	print("Total songs : " + str(num))


	# Log comment every 100th artist
	if(i%100 == 0 and i>0):
		millis = int(round(time.time() * 1000))-millis
		print("Seconds for 100 artists : " + str(millis/1000))	
		millis = int(round(time.time() * 1000))
	

	# Save backup and decrease memory usage every 5000 artists
	if(i%2000 == 0 and i>0):
		
		df1 		= pd.DataFrame({})
		df1["Url"]	= urls
		df1["Song"] = songs
		df1["Band"] = bands

		# Reinitialise to decrease memory use
		bands	= []
		songs 	= []
		urls 	= []

		# Write to batch output
		df1.to_csv("Data/Songs/SongData" + str(i/2000) + ".csv", index = False)

# Write to terminal
df1.to_csv("Data/Songs/SongData" + str(i/2000) + ".csv", index = False)