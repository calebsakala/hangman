# This program generated the array of strings that I copied into my Hangman C file
# Ideally, the input text should be a .txt file with each word/entry on a NEW line
# Such that each different word/entry has its own line

def create_array(source, dest):
    words_array = []

    # the source file is opened
    with open(source, "r") as file:
        for line in file:
            words_array.append(line.strip())  # each line is added to the words array (omitting any newline characters or spaces)

    with open(dest, "w") as writefile:
        writefile.write("{")   # the left brace of an array in C
        for element in words_array:
            writefile.write(f"\"{element}\",")  # the word dog would be written as "dog" in the array.
        writefile.write("}")   # the right brace of an array in C

    return words_array


if __name__ == "__main__":
    source = input(
        "Enter the name of the file that contains the data you need made into an array. \nInclude any necessary file extensions\n> ")
    dest = input(
        "What would you like to call the file that this program will output? \nInclude any necessary file extensions\n> ")
    create_array(source, dest)
