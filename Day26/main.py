import pandas

phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet_dict = {row.letter:row.code for (_, row) in phonetic_alphabet.iterrows()}

def generate_phonetic():
    word = input("Type a word: ").upper()
    try:
        phonetic_word = [phonetic_alphabet_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else: 
        print(phonetic_word)

generate_phonetic()