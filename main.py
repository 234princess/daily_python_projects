PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt", mode="r") as names:
    list_of_names= names.readlines()
    #print(list_of_names)
    

with open("./Input/Letters/starting_letter.txt", mode = "r") as letter:
    letter_template = letter.read()
    for name in list_of_names:
        stripped_name = name.strip()
        new_letter = letter_template.replace(PLACEHOLDER,stripped_name)
        #print(new_letter)

        with open(f"./Output/ReadytoSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
        


