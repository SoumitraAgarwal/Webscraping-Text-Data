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

base 	= "http://www.addic7ed.com/shows.php"

while(True):
	try:
		webp = requests.get(base, proxies = proxies)
		# time.sleep(20)
		break
	except requests.exceptions.RequestException as e:  # This is the correct syntax
		print(e)
		time.sleep(20)

df1 = pd.DataFrame({})


html = webp.content
soup = BeautifulSoup(html,'lxml')
rows = soup.findAll('table')
shows = rows[1].findAll('option')
showNames = []
showOpt = []

for show in shows:
	if(show["value"]!="0"):
		showNames.append(show.find(text=True).encode('utf-8'))
		showOpt.append(show["value"])

df1["Show"] 	= showNames
df1["Option"]	= showOpt

df1.to_csv("Data/Shows.csv", index = False)
