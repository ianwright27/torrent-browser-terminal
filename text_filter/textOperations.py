#just normal functions 
#for formatting the texts

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