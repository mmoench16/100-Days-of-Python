import random
from art import logo

HARD = 5
EASY = 10

def check_answer(guess, answer, attempts):
    """Checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return attempts - 1
    elif guess < answer:
        print("Too low.")
        return attempts - 1
    else:
        print(f"You got it! The answer is {answer}")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'hard':
        return HARD
    else:
        return EASY
    
def play():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num_to_guess =  random.randint(1,100)
    print(f"Pssst, the correct answer is {num_to_guess}")

    attempts = set_difficulty()

    guess = 0

    while guess != num_to_guess:
        print(f"You have {attempts} attempts remaining to guess the number.")

        guess = int(input("Make a guess: "))

        attempts = check_answer(guess, num_to_guess, attempts)
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != num_to_guess:
            print("Guess again.")
        
play()