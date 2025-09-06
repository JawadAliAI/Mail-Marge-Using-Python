import os
# YOLO Achie vement Test

PLACEHOLDER = "[name]"

# Read names
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Ensure Output folder exists
os.makedirs("./Output", exist_ok=True)

# Read the starting letter template
with open("./Input/Letters/starting_letters.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

        # Create a personalized letter file for each name
        with open(f"./Output/letter_for_{stripped_name}.txt", "w") as output_file:
            output_file.write(new_letter)
