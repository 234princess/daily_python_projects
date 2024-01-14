import random


rock = 0
paper = 1
scissors = 2

computer_choice = random.randint(0,2)
user_choice = int(input("Make a selection ; Type 0 for Rock, 1 for Paper or 2 for Scissors\n")) 
print (f"Computer chose {computer_choice}")

if user_choice >= 3 :
    print ("Please input a vaid number")
    
elif user_choice == computer_choice:
    print ("Draw, play again ?")

elif user_choice == 0 and computer_choice == 2 :
    print ("You win !")

elif user_choice == 2 and computer_choice == 0 :
    print ("You lose!")

elif user_choice > computer_choice:
    print ("You win !")

else :
    print("You lost !")

