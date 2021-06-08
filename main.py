from bs4 import BeautifulSoup
import urllib.request
from urllib.request import Request, urlopen
import os
from unidecode import unidecode

path = os.getcwd()
flac = open(path+'/'+'strip.txt', 'r', encoding="utf8")
#print(flac)
links = open(path+'/'+'links.txt', 'w', encoding="utf8")
lines = flac.readlines()

count = 0
# Strips the newline character
for line in lines:
	count += 1
	unaccented_string = unidecode(line.strip())
	#print(unaccented_string)
	encode = urllib.parse.quote(unaccented_string.strip()) #just encode artist/album (don't split)
	artist_ascii, album_ascii = unaccented_string.split('/', 1) #split artist/album
	artist_uni = urllib.parse.quote(artist_ascii.strip()) #convert ASCII to Unicode
	album_uni = urllib.parse.quote(album_ascii.strip()) #convert ASCII to Unicode

	print(artist_uni)
	print(album_uni)

	content = urllib.request.urlopen('https://api.deezer.com/search/album/?q=artist:"{0}"%20album:"{1}"&index=0&limit=1&output=xml'.format(artist_uni, album_uni))

	read_content = content.read()
	soup = BeautifulSoup(read_content,'xml')

	for el in soup.select('root > data > album'):
		link = el.link.text.strip()
		title = el.title.text.strip()

	for el in soup.select('root'):
		total = int(el.total.text.strip())

		if total == 0:
			content = urllib.request.urlopen('https://api.deezer.com/search/album/?q={}&index=0&limit=1&output=xml'.format(encode))
			read_content = content.read()
			soup = BeautifulSoup(read_content,'xml')

			for el in soup.select('root > data > album'):
				link = el.link.text.strip()
				title = el.title.text.strip()

			for el in soup.select('root'):
				total = int(el.total.text.strip())

				if total == 0:
					print('No Result For: {}'.format(line.strip()))
					links.write('No Result For: {}'.format(line.strip()))
				else:
					print(link + ' - ' + title)
					links.write(link + ' - ' + title)
					links.write('\n')
		else:
			print(link + ' - ' + title)
			links.write(link + ' - ' + title)
			links.write('\n')


flac.close()
links.close()
