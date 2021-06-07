from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import random
import os

path = os.getcwd()
flac = open(path+'/'+'strip.txt', 'r')
#print(flac)
links = open(path+'/'+'links.txt', 'w')
lines = flac.readlines()

count = 0
# Strips the newline character
for line in lines:
	count += 1
	separate = '{}'.format(line.strip()).replace('/', '%20').replace(' ', '%20')
	#print(separate)

	content = urllib.request.urlopen('https://api.deezer.com/search/album/?q={0}&index=0&limit=1&output=xml'.format(separate))
	read_content = content.read()
	soup = BeautifulSoup(read_content,'xml')

	for el in soup.select('root > data > album'):
		link = el.link.text.strip()
		title = el.title.text.strip()
		print(link)
		print(title)
		links.write(link)
		links.write('\n')

flac.close()
links.close()
