from os import system
from os import path
import getpass

file = []

def number_of_files():
	return len(file)

def free_files_from_memory():
	file = []

def push_file(data):
	file.append(data)

def browse_file(index):
	return file[index-1]

def download_file(index):
	user = getpass.getuser()

	directory_name = "TorrentBrowserDownloads"
	dir_exists = path.exists(f"/home/{user}/Downloads/{directory_name}")
	directory = f"/home/{user}/Downloads/{directory_name}"

	if dir_exists == False:
		system(f"mkdir {directory}")

		bash_cmd  = f"transmission-gtk {file[index-1]['Magnet Link']}"
		command = f"xterm -hold -e {bash_cmd}"
		system(command)
	else:
		bash_cmd  = f"cd {directory} && transmission-gtk {file[index-1]['Magnet Link']}"
		command = f"xterm -hold -e {bash_cmd}"
		system(command)
