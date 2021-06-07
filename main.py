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
	separate = '{}'.format(line.strip()).replace(' ', '+').replace('-', '+').replace('/', '%2F')
	#print(separate)

	content = 'https://html.duckduckgo.com/html/?q=site%3Adeezer.com+' + separate
	#print(content)
	user_agent_list = [
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
	'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
	]
	for i in range(1,4):
		#Pick a random user agent
		user_agent = random.choice(user_agent_list)
		hdr = {'User-Agent': user_agent}
	req = Request(content,headers=hdr)
	read_content = urlopen(req)
	soup = BeautifulSoup(read_content,'lxml')
	album = soup.find_all('a', {'class' : 'result__a'}, href=True, limit=1)
	#print(album)
	for el in album:
		print(el['href'])
		links.write(el['href'])
		links.write('\n')

flac.close()
links.close()
