#Author : Ian Wright
#Email: thewian27@gmail.com

import requests as r
from bs4 import BeautifulSoup
from os import system
import time
import text_filter.textOperations as text
import fetch_link.magnet_links as fetch
import __download__.file_indexing as __file__
import sys

def view_list(number):
	text.screen()
	numberOfFiles = __file__.number_of_files()
	for fl in range(0,numberOfFiles):
		file_object = __file__.browse_file(fl)
		text.print_view(file_object)
	proceed_ = input('[TB] > Do you want to proceed downloading the files? <y/n>')
	if proceed_ == "y":
		view_file(number)
	else:
		__file__.free_files_from_memory()
		main()

def view_file(number):
	index_ = input(f'[TB] > Which file do you want? <1-{number}> :\n\t') 
	f_index = int(index_)
	file = __file__.browse_file(f_index)

	system('clear')
	text.screen()
	text.print_view(file)

	is_download = input('[TB] > Download? <y/n>: ')
	if is_download == 'y':
		__file__.download_file(f_index)
	else:
		system('clear')
		view_list(number)


def parse(url,source_code):
	print ('\n\t[ fetching torrents.... ]\n\t[ Please wait a minute... ]\n')
	file_index = 0
	source = BeautifulSoup(source_code,'html5lib')
	tbody = source.find('tbody')
	links = tbody.find_all('tr')
	for row in links:
		title = row.find('div', {'class':'detName'})
		link_N_title = title.find('a')
		full_url = f"{url}{link_N_title['href']}"
		magnetLink = fetch.fetch_magnet_link(full_url)

		desc = row.find('font', {'class':'detDesc'})
		_size = str(desc)
		size = text.textFilter(_size)
		the_rest = row.find('td', {'align':'right'})
		extras = []
		for item in the_rest:
			seeders = item
		file_index += 1
		_thefile_ = {
			'Title':link_N_title.text,
			'Link':full_url,
			'Size':size,
			'Seeders':seeders,
			'Magnet Link':magnetLink
		}
		__file__.push_file(_thefile_)
	load_files = True
	return file_index
		

def main():
	system('clear')
	site="https://www.thepiratebay.org/"
	headers = {'Referer':'https://thepiratebay.org/','User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linu…) Gecko/20100101 Firefox/64.0'}
	text.screen()
	
	__search__ = input('[TB] > Search > ')
	search = text.refine(__search__)
	payload = {'q':search, 'page':0,'orderby':99}
	url = "https://www.thepiratebay.org/s/"
	request = r.get(url,params=payload,timeout=60)
	fetched_files = parse(site,request.text)

	proceed = input(f'[TB] > Fetched {fetched_files} files. Do you want to proceed downloading the files? <y/n>\n\t:')

	if proceed == "y":
		view_list(fetched_files)
	else:
		print('>Bye bye...')
		sys.exit()


try:
	main()
except Exception as e:
	print(f'{e}\t> Try Again')
