from art import logo
print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(inp_text, inp_shift, inp_dir):
    if inp_dir == "encode":
        # encrypt
        code = ""
        for letter in inp_text:
            pos = alphabet.index(letter)
            new_pos = (pos + inp_shift) % 26
            code += alphabet[new_pos]
        
        print(f"The codeword is {code}")

    elif inp_dir == "decode":
        # decrypt
        msg = ""
        for letter in inp_text:
            pos = alphabet.index(letter)
            new_pos = (pos - inp_shift) % 26
            msg += alphabet[new_pos]

        print(f"The message is {msg}")

end_prog = "no"
while end_prog != "yes":

    dir = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if dir == "encode":
        caesar(text, shift, "encode")
    elif dir == "decode":
        caesar(text, shift, "decode")
    else:
        print("Please enter a valid input.")
    end_prog = input("Type 'yes' if you want to exit the program or enter 'no':\n")