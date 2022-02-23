import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
all_options = [rock, paper, scissors]


choice = int(input("Enter 0 for rock, 1 for paper, 2 for scissors: "))
comp_choice = random.randint(0, 2)


print("You chose: ")
print(all_options[choice])
print("The computer chose: ")
print(all_options[comp_choice])


if choice == comp_choice :
    print("It's a draw!")
elif choice == 0 and comp_choice == 2:
    print("You won!")
elif choice == 1 and comp_choice == 0:
    print("You won!")
elif choice == 2 and comp_choice == 1:
    print("You won!")
else:
    print("Better luck next time!")