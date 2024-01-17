import random

word_list = ["monkey", "cat", "rat"]
display = []
chosen_word = random.choice(word_list)
print("Psst...The word is {chosen_word}")

for letter in chosen_word:
    letter_count = len(chosen_word)
    display += "_"
    print(display)

end_of_game = False

while not end_of_game:
    guess = input("Guess the word !: ").lower()
    for position in range (len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess :
            display[position] = letter
            print("That is correct")
        else:
            print("That is wrong")

    if "_" not in display:
        end_of_game = True
        print("You win !")

