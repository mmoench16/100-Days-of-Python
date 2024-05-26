# Hangman

import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f"Psst, the solution is {chosen_word}.")

display = ["_"] * len(chosen_word)

guess = input("Please guess a letter: ").lower()

for index, letter in enumerate(chosen_word):
    if letter == guess:
        display[index] = guess

print(display)