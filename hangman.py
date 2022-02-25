import logo
import words
import random

print(logo.logo_game)

chosen_word = random.choice(words.word_list) 

disp = []
for i in range(len(chosen_word)):
    disp.append("_")

end_game = False
lives = 6

while not end_game:
    guess = input("\n\nGuess a letter: ").lower()
    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]

        if letter == guess:
            disp[pos] = letter

    if guess not in chosen_word:
      lives -= 1
      print(logo.stages[lives])
      if lives == 1:
        print("You have 1 life left.")
      else:
        print(f"You have {lives} lives left.")

    if lives != 0:
      print(f"\n{' '.join(disp)}\n")

    if "_" not in disp or lives == 0:
        end_game = True
        if lives == 0:
            print(f"\n\nThe word was {chosen_word}")
            print("Better luck next time!\n\n")
        else:
            print("\n\nYou win!\n\n")