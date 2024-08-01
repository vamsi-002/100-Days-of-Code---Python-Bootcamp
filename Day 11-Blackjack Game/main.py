import random
import os
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def cal_score(player):
    score = sum(player)
    if 11 in player and score > 21:
        score -= 10
    return score

def compare(user_score, computer_score):
    if user_score > 21:
        return "You went over 21. You lose!"
    elif computer_score > 21:
        return "Computer went over 21. You win!"
    elif user_score == computer_score:
        return "It's a draw!"
    elif user_score == 21:
        return "Blackjack! You win!"
    elif computer_score == 21:
        return "Computer has a Blackjack! You lose!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "Computer wins!"

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_rules():
    print("Welcome to Blackjack!")
    print("""
    🃏 Blackjack Rules:
    1. The goal is to get as close to 21 as possible without going over.
    2. Kings, Queens, and Jacks are worth 10 points. Aces can be worth 11 or 1 point.
    3. The player and dealer each start with two cards.
    4. The player goes first and can choose to 'hit' (take another card) or 'stand' (end their turn).
    5. If your hand value goes over 21, you bust, and the dealer wins.
    6. The dealer must continue to take cards ('hit') until their score is 17 or higher.
    7. The closest hand to 21 without going over wins. A Blackjack (21 with the first two cards) is an automatic win.
    8. If both you and the dealer have the same score, it's a draw.
        """)

def blackjack_game():
    print(logo)

    user = []
    computer = []

    user.append(random.choice(cards))
    user.append(random.choice(cards))
    computer.append(random.choice(cards))
    computer.append(random.choice(cards))

    print(f"Your cards: {user}, Current score: {cal_score(user)}")
    print(f"Computer's first card: {computer[0]}")

    if cal_score(computer) == 21:
        print("Computer has a Blackjack! You lose!")
        return

    if cal_score(user) == 21:
        print("You have a Blackjack! You win!")
        return

    end_game = False
    while not end_game:
        another_card = input("Do you want another card? Type 'yes' to draw or 'no' to pass: ").lower()
        
        if another_card == "yes":
            user.append(random.choice(cards))
            user_score = cal_score(user)
            print(f"Your cards: {user}, Current score: {user_score}")
            if user_score > 21:
                print("You went over 21! Computer wins!")
                return
        else:
            end_game = True

    while cal_score(computer) < 17:
        computer.append(random.choice(cards))

    user_score = cal_score(user)
    computer_score = cal_score(computer)
    
    print(f"Your final hand: {user}, final score: {user_score}")
    print(f"Computer's final hand: {computer}, final score: {computer_score}")
    
    print(compare(user_score, computer_score))

display_rules()

while input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ") == "yes":
    clear()
    blackjack_game()
