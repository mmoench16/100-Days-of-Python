from art import logo
from art import vs
from game_data import data
import random
import os

clear = lambda: os.system('clear')

def draw_social_media_account():
    account_index = random.choice(range(len(data)))
    account = data[account_index]
    del(data[account_index])
    
    return account

def pit_against(account1, account2):
    print(f"Compare A: {account1["name"]}, {account1["description"]}, from {account1["country"]}.")
    print(vs)
    print(f"Compare B: {account2["name"]}, {account2["description"]}, from {account2["country"]}.")

def compare(account1, account2):
    return "A" if account1["follower_count"] > account2["follower_count"] else "B"

def play():
    score = 0
    game_active = True
    first_account = draw_social_media_account()
    
    print(logo)

    while game_active:
        second_account = draw_social_media_account()
        print(first_account)
        print(second_account)
        pit_against(first_account, second_account)
        letter_more_followers = compare(first_account, second_account)
        answer = input("Who has more followers? Type 'A' or 'B': ")

        if letter_more_followers == answer:
            score += 1
            first_account = second_account
            clear()
            print(logo)
            print(f"You are right! Current score: {score}.")
            if len(data) == 0:
                print("Wow. You are a superstar. You beat the game")
                game_active = False
        else:
            game_active = False
            clear()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}.")

play()