# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import string
import urllib2
import requests
import pandas as pd

proxies = {
  'http': 'http://10.4.22.5:3128',
  'https': 'https://10.4.22.5:3128',
}

pages 	= string.lowercase
pages 	= list(pages)
pages.append("19")
pages 	= [x + '.html' for x in pages]
base 	= "http://www.azlyrics.com/"


for page in pages:

	try:
		webp = requests.get(base + page ,proxies=proxies)
	except requests.exceptions.RequestException as e:  # This is the correct syntax
		print(e)

	html = webp.content
	soup = BeautifulSoup(html,'lxml')
	print(type(soup))	
	rows = soup.findAll('div', class_="col-sm-6 text-center artist-col")
	for row in rows:
		artists = row.findAll('a')
		for artist in artists:
			url = artist["href"]
			name = artist.find(text=True)

			try:
				artp = requests.get(base + url ,proxies=proxies)
			except requests.exceptions.RequestException as e:  # This is the correct syntax
				print(e)

			arthtml = artp.content
			artsoup = BeautifulSoup(arthtml,'lxml')