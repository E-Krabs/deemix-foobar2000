from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import os

path = os.getcwd()
flac = open(path+'/'+'strip.txt', 'r', encoding="utf8")
#print(flac)
links = open(path+'/'+'links.txt', 'w', encoding="utf8")
lines = flac.readlines()

count = 0
# Strips the newline character
for line in lines:
	count += 1
	separate = '{}'.format(line.strip()).replace(' ', ' ').replace('-', ' ').replace('/', ' - ').replace(
        '_', ' ').replace('!', '').replace("'", ' ').replace('(', '').replace(')', '').replace('ö', 'o').replace('é', 'e').replace('è', 'e').replace('à', 'a').replace('ú', 'u')

	encode = urllib.parse.quote(separate.strip())
	print(encode)

	content = urllib.request.urlopen('https://api.deezer.com/search/album/?q={}&index=0&limit=1&output=xml'.format(encode))
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
