import requests as r
from bs4 import BeautifulSoup
from os import system
import time

def refine(data):
	output = ""
	for char in data:
		if char == " ":
			output += "+"
		else:
			output+=char
	return output

def textFilter(str_):
	string = ""
	for ch in str_:
		if ch == "<":
			string += "a"
		elif ch == ">":
			string += "b"
		elif ch == "/":
			string += "c"
		else:
			string += ch
	new_string = string[string.find('S'):string.find(', ULed')]
	return new_string

def parse(url,source_code):
	source = BeautifulSoup(source_code,'html5lib')
	tbody = source.find('tbody')
	links = tbody.find_all('tr')
	for row in links:
		title = row.find('div', {'class':'detName'})
		link_N_title = title.find('a')
		desc = row.find('font', {'class':'detDesc'})
		_size = str(desc)
		size = textFilter(_size)
		the_rest = row.find('td', {'align':'right'})
		extras = []
		for item in the_rest:
			seeders = item
		print(f"""\n
		+====================================================================================================================================
		|Title    |  {link_N_title.text}
		|Link     |  {url}{link_N_title['href']}
		|Size     |  {size}
		|Seeders  |  {seeders}
		+====================================================================================================================================
			\n""")
		#extras = []
		

def main():
	site="https://www.thepiratebay.org/"
	headers = {'Referer':'https://thepiratebay.org/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/64.0'}
	print("""\n
		========================================

		        TORRENT BROWSER SCRIPT
		
		========================================
				  Author: Ian Wright
				  github.com/ianwright27
			          ----------------------
		\n""")
	__search__ = input('Search > ')
	search = refine(__search__)
	payload = {'q':search, 'page':0,'orderby':99}
	url = "https://www.thepiratebay.org/s/"
	request = r.get(url,params=payload,timeout=60)
	parse(site,request.text)
	print(f'URL: {request.url}')


try:
	system('clear')
	main()
except Exception as e:
	print(f'{e}\t> Try Again')
	#time.sleep(2)
