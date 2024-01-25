import random
print("Welcome to thee Number Guessing Game !")
print("I am thinking of a number between 1 - 100.")

level = input("Choose a difficulty. Type in 'easy or 'hard':\n").lower()
if level == 'easy':
    user_attempts = 10
elif level == 'hard':
    user_attempts = 5
else:
    print("Please type in the correct keyword.")

number = random.choice(range(1,51))

game_is_on = True
while game_is_on:
    print(f"You have {user_attempts} attempts remaining to guess the number")
   
    if user_attempts == 0:
        print("You have run out of lives, you lose")
        print(f"The correct answer was {number}")
        game_is_on = False
        
    else :
        user_guess = int(input("Make a guess: "))
        if user_guess == number :
            print(f"You win , the answer is {number}!")
            game_is_on = False

        elif user_guess < number:
            print ("Too low.\nGuess again.")
            user_attempts -= 1

        elif user_guess > number:
            print ("Too high.\nGuess again.")
            user_attempts -= 1

        elif user_guess == ' ':
            print("Please type in the correct keyword.")
        
   
        


