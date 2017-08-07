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


base 	= "http://www.lyrics.com/"
bands	= []
songs 	= []
urls 	= []
df = pd.read_csv("/Data/ArtistUrl.csv")
for i in range(len(df))
	print("Working for " + df['Artist'][i])
	while(True):
		try:
			webp = requests.get(base + df['Urls'][i], proxies = proxies)
			# time.sleep(20)
			break
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			time.sleep(20)

	html = webp.content
	soup = BeautifulSoup(html,'lxml')
	metas = soup.findAll('table', class_="tdata")
	num = 0
	for meta in metas:
		rows = meta.findAll('a')
		url = [x["href"] for x in rows]
		name = [x.find(text=True).encode('utf-8') for x in rows]
		songs += name
		urls += url
		bands += [df['Artist'][i]]*len(url)
		num += len(url)
	print("Done for " + df['Artist'][i])
	print("Total songs : " + str(num))

	if(i%1000 == 0 and i>0):
		df1 = pd.DataFrame({})
		df1["Song"] = songs
		df1["Url"]	 = urls
		df1["Band"] = bands
		band	= []
		songs 	= []
		urls 	= []
		df1.to_csv("Data/SongData.csv", index = False)
