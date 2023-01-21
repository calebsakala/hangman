# This program formatted the list of word definitions that I got from easydefine.com
# It uses arraymaker (included in this repository) to turn all the definitions into a list 
# And then formats all elements of the list into an array of definitions that I could copy and paste into C.
# The format is: 'word - type of word: definition of word'

import arraymaker

def format(dest, string_list):
	formatted_string_list = []
	
	for element in string_list:
		string = ''
		# The sentence is split into parts
		split_sentence = element.split()
		# all types of words must have a colon afterwards
		# I knew what types of words were in the document as I used easydefine.com for all definitions
		for word in split_sentence:
			if word == 'verb' or word == 'noun' or word == 'adj.' or word == 'pron.' or word == 'interj.' or word == 'adv.':
				word += ':'    # A colon is added if the word from the list is a word that describes the grammar/use of other words
			string += word + ' '
		formatted_string_list.append(string)  # A formatted list is created to be output
	
	# Creates a file formatted as '{"str1", "str2", "str3"}' that I can copy and paste into C
	with open(dest, "w") as writefile:
		writefile.write("{")
		for element in formatted_string_list:
			writefile.write(f"\"{element}\",")
		writefile.write("}")

if __name__ == "__main__":
	source = input("Enter the name of the file that contains the data you need made into an array. \nInclude all necessary extensions.n> ")
	dest = input("What would you like to call the file that this program will output? \nInclude all necessary extensions.\n> ")
	format(dest, arraymaker.create_array(source, dest))



