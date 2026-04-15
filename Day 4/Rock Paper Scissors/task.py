import random
from operator import index

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

jokenpo = [rock, paper, scissors]
randomizer = random.randint(0, len(jokenpo)-1)
random = jokenpo[randomizer]
choice = int(input("Choose between rock(0), paper(1), scissors(2): "))
print(random)

if choice == 0:
    if random == rock:
        print("Draw")
    elif random == scissors:
        print("You win")
    else:
        print("You lose")

if choice == 1:
    if random == paper:
        print("Draw")
    elif random == rock:
        print("You win")
    else:
        print("You lose")

if choice == 2:
    if random == scissors:
        print("Draw")
    elif random == paper:
        print("You win")
    else:
        print("You lose")