# Hangman

import random
import hangman_words
import hangman_art

lives = 6
chosen_word = random.choice(hangman_words.word_list)

print(hangman_art.logo)

# Testing code
print(f"Psst, the solution is {chosen_word}.")

display = ["_"] * len(chosen_word)

while '_' in display and lives > 0:

    guess = input("Please guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    guessed_correctly = False

    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = guess
            guessed_correctly = True
    
    if not guessed_correctly:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1

    print(" ".join(display))
    print(hangman_art.stages[lives])

if lives > 0:
    print("You win.")
else:
    print("You lose.")