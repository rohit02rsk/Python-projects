import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_l = int(input("How many letters would you like in your password?\n")) 
num_s = int(input(f"How many symbols would you like?\n"))
num_n = int(input(f"How many numbers would you like?\n"))

pwd = []
for char in range(1, num_l + 1):
    pwd.append(random.choice(letters))

for sym in range(1, num_s + 1):
    pwd.append(random.choice(symbols))

for num in range(1, num_n + 1):
    pwd.append(random.choice(numbers))

random.shuffle(pwd)
print("\nYour new password is: ")
for char in pwd:
    print(char, end="")
