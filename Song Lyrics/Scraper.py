# -*- coding: utf-8 -*-

#
#	Script to scrape data from lyrics.com
#	using beautiful soup. This script gets
#	the data for all the artists by iterating
#	over the lettered list.
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

people	= []
urls 	= []
pages 	= string.uppercase
pages 	= list(pages)
base 	= "http://www.lyrics.com/"

# Peculiar entry manually entered
pages.append("0")

# Iterate over each letter
for page in pages:

	# Log comment
	print("Working for page " + str(page))
	
	# Continuous tries to avoid breaking in between and without data
	while(True):
		try:
			webp = requests.get(base + "artists/" + page + "/99999", proxies = proxies)
			break
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			time.sleep(20)

	# Basic pre processing
	html 	= webp.content
	soup 	= BeautifulSoup(html,'lxml')
	meta 	= soup.find('table', class_="tdata")
	rows 	= meta.findAll('a')
	
	# Meta data extraction
	url 	= [x["href"] for x in rows]
	name 	= [x.find(text=True).encode('utf-8') for x in rows]
	people 	+= name
	urls 	+= url

	# Final log comment
	print("Done for page " + str(page))
	print(len(rows))
	
# Write to file
df1 			= pd.DataFrame({})
df1["Urls"]	 	= urls
df1["Artist"] 	= people

df1.to_csv("Data/Artists/ArtistUrl.csv", index = False)
