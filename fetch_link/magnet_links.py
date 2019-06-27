import requests as r
from bs4 import BeautifulSoup as bs

def fetch_magnet_link(url):
	req = r.get(url, timeout=60)

	page = bs(req.text, 'html5lib')

	main_div = page.find('div', {'class':'download'})

	torrent_opt = main_div.find_all('a')

	for t in range(len(torrent_opt)):
		if t == 0:
			magnet_link = torrent_opt[t]['href']
	
	return magnet_link