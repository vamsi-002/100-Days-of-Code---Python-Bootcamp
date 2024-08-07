import random
import os
from art import logo, vs
from game_data import data

def pick_account():
    return random.choice(data)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

print(logo)
score = 0
end_game = False
profile_a = pick_account()
while not end_game:
    profile_b = pick_account()
    while profile_a == profile_b:
        profile_b = pick_account()

    print("🔥 Let's Compare 🔥")
    print(f"👤 Compare A: {profile_a['name']}, a {profile_a['description']}, from {profile_a['country']}.")
    print(vs)
    print(f"👤 Compare B: {profile_b['name']}, a {profile_b['description']}, from {profile_b['country']}.")
    
    guess = input("🤔 Who has more followers on Instagram? Type 'A' or 'B': ").lower()
    clear()
    print(logo)
    if (guess == 'a' and profile_a['follower_count'] > profile_b['follower_count']) or \
       (guess == 'b' and profile_a['follower_count'] < profile_b['follower_count']):
        score += 1
        print(f"🎉 You are right! Current Score: {score}")
        profile_a = profile_b
    else:
        print(f"💥 Sorry, that's wrong. Final Score: {score}")
        end_game = True
print("👋 Thanks for playing! See you next time!")
