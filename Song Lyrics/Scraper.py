# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import time
import string
import urllib2
import requests
import pandas as pd

proxies = {
  'http': 'http://172.16.114.112:3128/',
  'https': 'http://172.16.114.112:3128/',
}

pages 	= string.lowercase
pages 	= list(pages)
pages.append("19")
pages 	= [x + '.html' for x in pages]
base 	= "http://www.azlyrics.com/"

people	= []
urls 	= []
for page in pages:
	print("Working for page " + str(page))
	while(True):
		try:
			webp = requests.get(base + page ,proxies=proxies)
			time.sleep(50)
			break
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			time.sleep(50)

	html = webp.content
	print(html)
	soup = BeautifulSoup(html,'lxml')
	rows = soup.findAll('div', class_="col-sm-6 text-center artist-col")
	print("Done for page " + str(page))
	for row in rows:
		artists = row.findAll('a')
		for artist in artists:
			url = artist["href"]
			name = artist.find(text=True).encode('utf-8')
			people.append(name)
			urls.append(url)
			# try:
			# 	artp = requests.get(base + url ,proxies=proxies)
			# except requests.exceptions.RequestException as e:  # This is the correct syntax
			# 	print(e)

			# print("Working for " + name)
			# arthtml = artp.content
			# artsoup = BeautifulSoup(arthtml,'lxml')

			# struct 	= artsoup.find('div', id_ = "listAlbum")
			# df1 = pd.DataFrame({})
			# songNames = []
			# urls = []
			# for a in struct.findAll('a'):
			# 	if(a.has_attr('href')):
			# 		songNames.append(a.find(text=True))
			# 		urls.append(a["href"])

			# df1["Songs"] = songNames
			# df1["Urls"]	 = urls

			# df1.to_csv("Data/" + artist + ".csv", index = False)

print(people)
print(urls)
df1 = pd.DataFrame({})
df1["Artist"] = people
df1["Urls"]	 = urls

df1.to_csv("Data/Artists/ArtistUrl.csv", index = False)
