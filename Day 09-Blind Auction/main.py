from art import logo
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
print("Welcome to the secret auction program. ")

players = {}

end_game = False

while not end_game:

    name = input("What is your name?").strip()
    bid = input("What's your bid? $")
    
    while not bid.isdigit():
        print("Invalid bid. Please enter a number.")
        bid = input("What's your bid? $")
    
    bid = int(bid)

    players[name] = bid

    other_players = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    
    while other_players not in ['yes', 'no']:
        print("Invalid input. Please type 'yes' or 'no'.")
        other_players = input("Are there any other bidders? Type 'yes' or 'no': ").lower()

    if other_players == "no":
        end_game = True
    elif other_players == "yes":
        clear_console()

max_name = max(players, key=players.get)
max_bid = players[max_name]
clear_console()

print("All bids:")
for name, bid in players.items():
    print(f"{name}: ${bid}")

time.sleep(2)

print(f"\nThe winner is {max_name} with a bid of ${max_bid}.\n")
print("Thank you all for participating in the secret auction!")