PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_files:
    names = names_files.readlines()
    print(names)

with open("./Input/letters/starting_letters.txt") as letter_files:
    letter_contents = letter_files.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open("./Output/example.txt") as output:
             output.write(new_letter)
