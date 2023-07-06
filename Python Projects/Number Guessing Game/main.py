
import random
from ART import logo

print(logo)
print('Welcome to the number guessing Game !')
print("I'm thinking of a number between 1 and 100.")

# Generates random number
number = random.randint(1,100)

#Receives the mode of game hard or easy
mode_of_game = input("Choose a difficulty. Type 'easy' or 'hard': ")


def modeof(mode):
  isgame_over = False
  if mode == "hard":
    life = 5
  else:
    life = 10
  while not isgame_over:
    if life == 0:
      print("You've run out of guesses, you lose.")
      print(f"The number was {number}")
      isgame_over = True
    else:
      print(f"You have {life} attempts remaining to guess the number")
      # print(number)
      guess = int(input('Make a Guess '))
      if guess > number:
        print('Too high\nGuess Again')
        life -= 1
      elif guess < number:
         print('Too low\nGuess Again')
         life -= 1
      elif guess == number:
        print('You win')
        isgame_over = True

modeof(mode_of_game)
