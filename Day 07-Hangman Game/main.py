import random
import hangman_words
import hangman_art

print(hangman_art.logo)

chosen_word = random.choice(hangman_words.word_list)
lives = 6

display = ["_" for _ in chosen_word]
guessed_letters = set()

print(f"The word is: {' '.join(display)}")

end_of_game = False

while not end_of_game:
    guess = input("Enter a guess: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print(f"You've already guessed '{guess}'. Try again.")
        continue

    guessed_letters.add(guess)

    if guess in chosen_word:
        for position in range(len(chosen_word)):
            if chosen_word[position] == guess:
                display[position] = guess
        print(f"Good guess! The word now: {' '.join(display)}")
    else:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")
        if lives == 0:
            end_of_game = True
            print("You Lose.")
            print(f"The word was: {chosen_word}")

    print(hangman_art.stages[lives])
    
    if "_" not in display:
        end_of_game = True
        print("You Won!")
        print(f"The word is: {chosen_word}")
