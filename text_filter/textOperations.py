#just normal functions 
#for formatting the texts
def print_view(data):
	print(f"""\n
	+====================================================================================================================================
	|Title       |  {data['Title']}
	|Link        |  {data['Link']}
	|Size        |  {data['Size']}
	|Seeders     |  {data['Seeders']}
	+====================================================================================================================================
			\n""")

#	|Magnet Link |  {data['Magnet Link']}
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

def screen():
	print("""\n
		========================================

		        TORRENT BROWSER SCRIPT
		
		========================================
				  Author: Ian Wright
				  github.com/ianwright27
			          ----------------------
		\n""")