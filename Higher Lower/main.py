from insta_data import data
from art import logo, vs
import random
from os import system

#Function definitions
def format_data(acc):
    """ Helps in formatting the data into a printable fashion. """
    acc_name = acc["name"]
    acc_desc = acc["description"]
    acc_country = acc["country"]
    return f"{acc_name}, a {acc_desc}, from {acc_country}"

def check_ans(guess, A_foll, B_foll):
    """ Checks whether the user has guessed the correct answer or not. """
    if A_foll > B_foll:
        return guess == "a"
    else: 
        return guess == "b"

#Driver program
print(logo)
score = 0
game_resumes = True
acc_B = random.choice(data)

while game_resumes:
    acc_A = acc_B
    acc_B = random.choice(data)
    while acc_A == acc_B:
        acc_B = random.choice(data)

    print(f"\nCompare A: {format_data(acc_A)}")
    print(f"{vs}")
    print(f"Against B: {format_data(acc_B)}\n")

    guess = input("Who has more followers? Type 'A' or 'B'... ").lower()

    A_followers = acc_A["follower_count"]
    B_followers = acc_B["follower_count"]

    is_correct = check_ans(guess, A_followers, B_followers)
    system('cls')
    print(logo)
    if is_correct:
        score += 1
        print("\nYou're correct!")
    else:
        game_resumes = False
        print(f"\nThat's wrong, try again next time..\nYour final score: {score}")
