import random
import os

from game_data import data
from art import logo, logo_2

def format_data(option):
    """" Format the account info into a printable format."""
    option_name = option["name"]
    option_desc = option["description"]
    option_country = option["country"]
    return (f"{option_name}, a {option_desc}, from {option_country}")


def count_followers(guess, first_option, second_option):
    """Use to compare option a and option b followers"""
    first_option_fcount = first_option["follower_count"]
    second_option_fcount = second_option["follower_count"]

    if first_option_fcount > second_option_fcount:
        return guess == "a"
    else:
        return guess == "b"
        
    

print(logo)
user_score = 0
game_power = True
second_option = random.choice(data)

while game_power:


    first_option = second_option
    second_option = random.choice(data)
    
    while first_option == second_option :
        second_option = random.choice(data)

    print (f"\nCompare A: {format_data(first_option)}")
    print(logo_2)
    print (f"Against B: {format_data(second_option)}")  

    user_guess = input("Who has more followers? Type 'A' or 'B':\n").lower()
    is_correct = count_followers(user_guess, first_option, second_option)

    if is_correct:
        user_score += 1
        print(f"You are right!, Current score: {user_score}")
    else:
        game_power =False 
        print(f"You are wrong, Final score: {user_score}.")
        