import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return(random_card)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return


players_cards = []
cpu_cards = []

if_game_over = False
x = 2
while x > 0:
    new_player_card = deal_card()
    players_cards.append(new_player_card)

    new_cpu_card = deal_card()
    cpu_cards.append(new_cpu_card)
    x = x - 1

while not if_game_over:
    total_players_cards = calculate_score(players_cards)
    total_cpu_cards = calculate_score(cpu_cards)

    print(f" Your cards:{players_cards}, current score: {total_players_cards}")    
    print(f" Your cards:{cpu_cards}, current score: {total_cpu_cards}")    


    if total_players_cards == 0 or total_cpu_cards == 0 or total_cpu_cards > 21:
        if_game_over = True
    else:
        draw = input("Type 'y' to get another card, type 'n' to pass: ")
        if draw == "y":
            players_cards.append(deal_card())
        else:
            if_game_over = True

    
while total_cpu_cards != 0 and total_cpu_cards < 17:
    cpu_cards.append(deal_card())
    total_cpu_cards = calculate_score(cpu_cards)















