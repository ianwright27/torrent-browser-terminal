import os
import getpass
import sys

user = getpass.getuser()

dependencies = ['transmission-gtk', 'python3', 'xterm']

for app in dependencies:
	command = f"sudo apt-get install {app}"
	os.system(command)

cwd = os.getcwd()
#/home/ian/Desktop

remove_home = cwd[cwd.find('/home/')+6:]
the_rest = remove_home[remove_home.find('/'):]

_dir = "/home/"+user+the_rest
os.system("touch torrent-browser-terminal")
with open('torrent-browser-terminal','w') as f:
	line1 = "#!/bin/bash \n" 
	line2 = f"python3 {_dir}/torrent_browser.py"
	f.write(line1)
	f.write(line2)

os.system("sudo chmod +x torrent-browser-terminal")

c = input('[TB] > Do you want to put Torrent Browser Terminal in path? <y/n>')
if c == 'y':
	os.system('clear')
	os.system("sudo cp torrent-browser-terminal /usr/bin")
	print("\n\nNow you can open up Terminal and type 'torrent-browser-terminal' to execute")
else:
	sys.exit()