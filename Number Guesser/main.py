from random import randint
from art import logo

EASY_TURNS = 15
HARD_TURNS = 10

def check(guess, ans, turns):
    if guess > ans:
        print("Your guess is a bit too high..")
        return turns - 1
    elif guess < ans:
        print("Your guess is a but too low..")
        return turns - 1
    else:
        print(f"Congrats! {ans} was the number I was thinking of!")
        return turns
    
def easy_or_hard():
    lvl = input("Type 'easy' or 'hard' to set your difficulty.. ")
    if lvl == "easy":
        return EASY_TURNS
    else:
        return HARD_TURNS

def game():
    
    print(logo)
    print("Welcome to the number guessing game!")
    print("I am thinking of a number between -100 and 100...")
    ans = randint(-100, 100)
    
    turns = easy_or_hard()
    print(f"You have a total of {turns} turns left, Use them wisely..\n")

    guess = ans + 1
    while guess != ans:
        guess = int(input("Make a guess... "))
        turns = check(guess, ans, turns)
        print(f"You have a further {turns} turns left..")

        if turns == 0:
            print("You've run out of turns, Better luck next time..\n")
            break
        elif guess!=ans:
            print("Guess again..\n")

game()