import pandas as pd

data = pd.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (ind, row) in data.iterrows()}
print(phonetic_dict)

def gen_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, please use only the English Lexicon.")
        gen_phonetic()
    else:
        print(output_list)

gen_phonetic()
