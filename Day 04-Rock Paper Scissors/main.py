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

continue_game = True

while continue_game:
    try:
        choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors: "))
        if choice not in [0, 1, 2]:
            print("Invalid input. Please choose 0, 1, or 2.")
            continue

        computer = random.randint(0, 2)

        choices = [rock, paper, scissors]

        print("You chose:")
        print(choices[choice])

        print("Computer chose:")
        print(choices[computer])

        if choice == computer:
            print("It's a draw!")
        elif (choice == 0 and computer == 2) or (choice == 2 and computer == 1) or (choice == 1 and computer == 0):
            print("You won!")
        else:
            print("You lose!")

        cont = input('Do you want to continue the game? Type "Yes" or "No": ').strip().lower()
        if cont != "yes":
            continue_game = False

    except ValueError:
        print("Invalid input. Please enter a number (0, 1, or 2).")
