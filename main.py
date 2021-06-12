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

#strips the newline character.
for line in lines:
	count += 1

	unaccented_string = unidecode(line.strip())
	strip = unaccented_string.split('/') #decompile to list
	#print(unaccented_string)
	#since we are only looking for tracks, albums, and artists, trash all other junk data.
	#you could probally use CDx but it doesn't improve acuracy.
	cd_count = 1 #if CDx is in the list, then remove it
	while cd_count < 20: #bc whos got 20 cds?
		cd = 'CD{}'.format(cd_count)
		if cd in strip:
			strip.remove(cd)
		else:
			cd_count += 1

	#Deezer Advanced Search doesn't have any parameters for the track number. So burn it!
	track_count = 0 #if the track number is in the list, then remove it.
	while track_count < 120: #bc whos got 120 tracks?
		track_2d = '%02d' % track_count
		track_3d = '%03d' % track_count
		if track_2d in strip[2]:
			strip.remove(track_2d)
		elif track_3d in strip[2]:
			strip.remove(track_3d)
		else:
			track_count += 1

# ['Artist', 'Album', 'CDx', 'Num', 'Title1', 'Title2', 'Title3']
# ['Artist', 'Album', 'Title1', 'Title2', 'Title3']

	if len(strip) > 3: #if more than 3 items in list, assume everything after ['Album'] is the title.
			title_ascii = strip[2:]
			#print(title_ascii)
	print(strip) #check out what got removed.

	if len(strip) == 3: #if the list contains the title (single track).
		recomp = '' #converting list back to str bc im lazy (also, its easy (but its kinda messy (also, parenthesis! (uwu)))).
		for i in strip:
			recomp += ('{}/').format(i)
		artist_ascii, album_ascii, title_ascii, *other = recomp.split('/')
		title_uni = urllib.parse.quote(title_ascii) #convert ASCII to Unicode
		print(artist_ascii, album_ascii, title_ascii)
	else:
		recomp = ''
		for i in strip:
			recomp += ('{}/').format(i)
		artist_ascii, album_ascii, *other = recomp.split('/')
		print(artist_ascii, album_ascii)

	artist_uni = urllib.parse.quote(artist_ascii) #convert ASCII to Unicode
	album_uni = urllib.parse.quote(album_ascii) #convert ASCII to Unicode
	stop = False
	
	if 'title_uni' in locals(): #if there was a title in the list, search for it.
		print('https://api.deezer.com/search/?q=album:"{0}"%20track:"{1}"&index=0&limit=1&output=xml'.format(album_uni, title_uni))
		content = urllib.request.urlopen('https://api.deezer.com/search/?q=album:"{0}"%20track:"{1}"&index=0&limit=1&output=xml'.format(album_uni, title_uni))
		read_content = content.read()
		soup = BeautifulSoup(read_content,'xml')

		for el in soup.select('root > data > track'):
				link = el.link.text.strip()
				title = el.title.text.strip()
		for el in soup.select('root'):
			total = int(el.total.text.strip()) #get how many results.

			if total == 0: #if we couldn't find that track, give up...
				print("Couldn't Find Track: {0} - {1}, {2}".format(title_ascii, artist_ascii, album_ascii))
				links.write("Couldn't Find Track: {0} - {1}, {2}".format(title_ascii, artist_ascii, album_ascii + '\n'))
				stop = True
	else: #if title_uni doesn't exist, only the album and artist was provided
		if artist_uni in ['easter'] and album_uni in ['egg']:
			print('Wow! An Easter Egg!? In Open Code? Yes, I was bored.')
			break

		print('https://api.deezer.com/search/album/?q=artist:"{0}"%20album:"{1}"&index=0&limit=1&output=xml'.format(artist_uni, album_uni))
		content = urllib.request.urlopen('https://api.deezer.com/search/album/?q=artist:"{0}"%20album:"{1}"&index=0&limit=1&output=xml'.format(artist_uni, album_uni))
		read_content = content.read()
		soup = BeautifulSoup(read_content,'xml')

		for el in soup.select('root > data > album'):
			link = el.link.text.strip()
			title = el.title.text.strip()

		for el in soup.select('root'):
			total = int(el.total.text.strip())

			if total == 0: #if no results return, fallback to the less strict method of searching.
				content = urllib.request.urlopen('https://api.deezer.com/search/album/?q={0}/{1}&index=0&limit=1&output=xml'.format(artist_uni, album_uni)) #i know i could .join but ¯\_ (ツ)_/¯
				read_content = content.read()
				soup = BeautifulSoup(read_content,'xml')

				for el in soup.select('root > data > album'):
					link = el.link.text.strip()
					title = el.title.text.strip()

				for el in soup.select('root'):
					total = int(el.total.text.strip())

					if total == 0: #if still no results, give up...
						print("Couldn't Find Album: {}".format(line.strip()))
						links.write("Couldn't Find Album: {}".format(line.strip()) + '\n')

	if stop == False:
		print(link + ' - ' + title)
		links.write(link + ' - ' + title + '\n')
	if 'title_uni' in locals():
		del(title_uni)
flac.close()
links.close()
