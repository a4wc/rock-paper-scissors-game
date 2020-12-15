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
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if choice < 0 or choice > 2:
  print("You input an invalid number!")
else:
  choices = [rock, paper, scissors]

  computer_choice = random.randint(0,2)

  print(choices[choice])
  print(f"Computer choose\n{choices[computer_choice]}")

  if choice == computer_choice:
    print("It's a tie!")
  elif choice == 0 and computer_choice == 2:
    print("You win!")
  elif computer_choice == 0 and choice == 2:
    print("You lose!")
  elif choice > computer_choice:
    print("You win!")
  elif computer_choice > choice:
    print("You lose!")


