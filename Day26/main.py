import pandas

phonetic_alphabet = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet_dict = {row.letter:row.code for (_, row) in phonetic_alphabet.iterrows()}

word = input("Type a word: ").upper()

phonetic_word = [phonetic_alphabet_dict[letter] for letter in word]

print(phonetic_word)