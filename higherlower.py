from art import logo
from art import vs
import random
import os
from game_data import data

#Generate logo for the Game
print(logo)

score = 0
game_should_continue = True
account_b = random.choice(data)
def format_data(account):
    """formating the account data"""
    account_name = account['name']
    account_descr = account['description']
    account_cntry = account['country']
    return f"{account_name}, {account_descr}, {account_cntry} "

def check_ans(guess,a_follower_count,b_follower_count):
      if a_follower_count > b_follower_count:
        return guess == "A"
      else:
        return guess == "B"

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
            account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")

    print(vs)

    print(f"Compare B: {format_data(account_b)}")

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    guess = input("Who has more follower count. Type 'A' or 'B' ")
    is_correct = check_ans(guess, a_follower_count,b_follower_count)
    os.system('cls || clear')

    if is_correct:
        score += 1
        print(f"You're right.Current score is : {score} ")
    else:
        game_should_continue = False
        print(f"Wrong answer. Your current score is : {score}")
