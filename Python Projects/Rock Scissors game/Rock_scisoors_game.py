rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


import random
images = [rock,paper,scissors]

computer = random.randint(0,2)
input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
print(images[input])

print(f"Computer choose : \n {images[computer]}")


if input == 0 and computer == 2:
  print("You win")
elif input == 2 and computer == 1:
  print("You win")
elif input == 1 and computer == 0:
  print("You win")
elif input == computer:
  print("Its a draw")
else:
  print("You lose")
  
    
  