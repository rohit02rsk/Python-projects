from random import random
import art
import random

print(art.logo)

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calc_score(card):
    if sum(card) == 21 and len(card) == 2:
        return 0

    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
    
    return sum(card)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw!"
    elif c_score == 0:
        return "Computer had blackjack, you lost!"
    elif u_score > 21:
        return "You went over, you lost!" 
    elif c_score > 21:
        return "Opponent went over, you win!"
    elif u_score>c_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    game_over = False
    user_cards = []
    comp_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        comp_cards.append(deal_card())

    while not game_over:
        user_score = calc_score(user_cards)
        comp_score = calc_score(comp_cards)
        print(f"Your cards: {user_cards}, score: {user_score}")
        print(f"Comp's first card: {comp_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21:
            game_over = True
        else:
            user_shd_deal = input("Type 'y' to get another card, 'n' to pass: ")    
            if user_shd_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while comp_score != 0 and comp_score < 17:
        comp_cards.append(deal_card())
        comp_score = calc_score(comp_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

play_game()
while input("Do you want to play another game? type 'y' or 'n'") == 'y':
    print(art.logo())
    play_game()
