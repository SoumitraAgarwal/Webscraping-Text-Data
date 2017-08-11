# -*- coding: utf-8 -*-
import os
import time
import urllib2
import requests
import pandas as pd
from bs4 import BeautifulSoup


# Initialisations for proxy and other metas to be used later
proxies = {
  'http': 'http://172.16.114.112:3128/',
  'https': 'http://172.16.114.112:3128/',
}

base 	= "http://www.lyrics.com"
files = os.listdir("Data/Songs")
batch = 1

files.sort()
for file in files:

	print("Working for " + file)
	lyrics = []
	artist = []
	song = []

	data = pd.read_csv("Data/Songs/" + file)
	millis 	= int(round(time.time() * 1000))

	for i in range(len(data["Url"])):

		url = data["Url"][i]

		if(url[:6]=="/lyric"):
			
			

			# Continuous tries to avoid breaking in between and without data
			while(True):
				try:
					webp = requests.get(base + data['Url'][i], proxies = proxies)
					break
				
				except requests.exceptions.RequestException as e:  # This is the correct syntax
					print(e)
					time.sleep(20)

			
			# Basic pre processing
			html 	= webp.content
			soup 	= BeautifulSoup(html,'lxml')
			metas 	= soup.find('pre', class_="lyric-body")

			try:
				lyric 	= metas.find(text = True)

				artist.append(data["Band"])
				song.append(data["Song"])
				lyrics.append(lyric)
			except:
				print("Didn't work for " + data["Song"][i])
				continue


		if(i%1000 == 0 and i>0):

			millis 	= int(round(time.time() * 1000)) - millis
			print("Took " + str(millis) + " millis for 100 uploads")
			millis 	= int(round(time.time() * 1000))
			df = pd.DataFrame({'Song' : song, 'Band' : artist, 'Lyrics' : lyrics})
			df.to_csv("Data/Lyrics/LyricsBatch" + str(batch) + ".csv", index = False, encoding = 'utf-8')
			batch = batch + 1
			lyrics = []
			artist = []
			song = []
