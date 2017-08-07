# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import os
import urllib2
import time
import pandas as pd


proxies = {
  'http': 'http://172.16.114.112:3128/',
  'https': 'http://172.16.114.112:3128/',
}

base 	= "http://www.addic7ed.com/"

df = pd.read_csv("Data/Shows.csv")
for i in range(len(df['Show'])):

	option = df['Option'][i]
	print("Trying out " + df['Show'][i])
	while(True):
		try:
			webp = requests.get(base + "show/" + str(option), proxies = proxies)
			# time.sleep(20)
			break
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			time.sleep(20)

	html = webp.content
	soup = BeautifulSoup(html,'lxml')
	subs = soup.findAll('tr', class_="epeven completed")
	proxy = urllib2.ProxyHandler(proxies)
	opener = urllib2.build_opener(proxy)
	urllib2.install_opener(opener)


	os.mkdir("Data/" + df['Show'][i])
	for sub in subs:
		meta = sub.findAll('td')
		language = meta[3].find(text=True).encode('utf-8')
		meta = sub.findAll('a')
		with open("Data/" + df['Show'][i] + "/" + df['Show'][i] + language + '.txt' ,'wb') as f:
		    f.write(urllib2.urlretrieve(base + meta[1]['href']).read())
		    f.close()
	break
