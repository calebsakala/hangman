def create_array(source, dest):
    words_array = []

    with open(source, "r") as file:
        for line in file:
            words_array.append(line.strip())

    destination_file = 'Output\\arraymaker\{}.txt'.format(dest)

    with open(destination_file, "w") as writefile:
        writefile.write("{")
        for element in words_array:
            writefile.write(f"\"{element}\",")
        writefile.write("}")

    return words_array


if __name__ == "__main__":
    source = input(
        "Enter the name of the file that contains the data you need made into an array. \nInclude extensions like .txt or .docx\n> ")
    dest = input(
        "What would you like to call the file that this program will output? \nDo not include extensions.\n> ")
    create_array(source, dest)
