print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name_1 = name1 + " " + name2
name = name_1.lower()
true_int = name.count('t') + name.count("r") + name.count("u") + name.count("e")
love_int = name.count("l") + name.count("o") + name.count("v") + name.count("e")
true = str(true_int)
love = str(love_int)

score_str = true + love
score = int(score_str)

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50 :
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")