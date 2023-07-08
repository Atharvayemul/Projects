from game_data import data
import random
import art
import replit


def checker(data1, data2):

    print(
        f"Comapare A : {data1['name']}, a {data1['description']}, from {data1['country']}")
    print(art.vs)
    print(
        f"Comapare B : {data2['name']}, a {data2['description']}, from {data2['country']}")

    if data1['follower_count'] > data2['follower_count']:
        return 'a'
    else:
        return 'b'


def game():
    print(art.logo)
    game = True
    score = 0
    account_a = random.choice(data)
    account_b = random.choice(data)
    correct_ans = checker(account_a, account_b)
    while game != False:
        guess = input("Who has more followers? Type 'a' or 'b': ")
        if correct_ans == guess:
            score += 1
            replit.clear()
            print(art.logo)
            print(f"You're right! Current score: {score}")
            correct_ans = checker(account_b, random.choice(data))
        else:
            print(f"Sorry Thats wrong. Your final Score : {score}")
            game = False


game()
