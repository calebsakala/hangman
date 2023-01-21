import arraymaker


def format(dest, string_list):
	formatted_string_list = []
	
	for element in string_list:
		string = ''
		split_sentence = element.split()
		for word in split_sentence:
			if word == 'verb' or word == 'adj.' or word == 'noun' or word == 'pron.' or word == 'interj.' or word == 'adv':
				word += ':'
			string += word + ' '
		formatted_string_list.append(string)

	destination_file = 'Output\dictionarymaker\{}.txt'.format(dest)
	
	with open(destination_file, "w") as writefile:
		writefile.write("{")
		for element in formatted_string_list:
			writefile.write(f"\"{element}\",")
		writefile.write("}")

if __name__ == "__main__":
	source = input("Enter the name of the file that contains the data you need made into an array. \nInclude extensions like .txt or .docx\n> ")
	dest = input("What would you like to call the file that this program will output? \nDo not include extensions.\n> ")
	format(dest, arraymaker.create_array(source, dest))



