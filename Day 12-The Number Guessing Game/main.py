import random
from art import logo

print(logo)

correct_number = random.randint(1, 100)

print("🎉 Welcome to the Number Guessing Game! 🎉")
print("I'm thinking of a number between 1 and 100.")

level = input("Choose the difficulty level: 'easy' or 'hard' ➡️   ").lower()
lives = 0

if level == 'easy':
    lives = 10
    print("You've chosen the 'easy' level. 😊")
elif level == 'hard':
    lives = 5
    print("You've chosen the 'hard' level. 😎")

print(f"You have {lives} attempts to guess the number. Good luck!")

while lives > 0:
    guess_number = int(input("Make a Guess: "))

    if guess_number == correct_number:
        print(f"🎉 You got it! The answer is {guess_number}. 🥳")
        break
    else:
        lives -= 1
        if guess_number > correct_number:
            print("📉 Too high!")
        else:
            print("📈 Too low!")

        if lives == 0:
            print("😔 You've run out of moves. You lose!")
            print(f"The correct number was {correct_number}. Better luck next time!")
        else:
            feedback = ""
            if abs(guess_number - correct_number) <= 10:
                feedback = "You're very close! 🔥"
            print(f"{feedback} Guess again!")
            print(f"You have {lives} attempts left. 💪")

print("Thanks for playing! 🎮")
