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

pages 	= string.uppercase
pages 	= list(pages)
pages.append("0")
# pages 	= [x + '.html' for x in pages]
base 	= "http://www.lyrics.com/"

people	= []
urls 	= []
for page in pages:
	print("Working for page " + str(page))
	while(True):
		try:
			webp = requests.get(base + "artists/" + page + "/99999", proxies = proxies)
			# time.sleep(20)
			break
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			time.sleep(20)

	html = webp.content
	soup = BeautifulSoup(html,'lxml')
	meta = soup.find('table', class_="tdata")
	rows = meta.findAll('a')
	print("Done for page " + str(page))
	print(len(rows))
	url = [x["href"] for x in rows]
	name = [x.find(text=True).encode('utf-8') for x in rows]
	people += name
	urls += url

df1 = pd.DataFrame({})
df1["Artist"] = people
df1["Urls"]	 = urls

df1.to_csv("Data/Artists/ArtistUrl.csv", index = False)
