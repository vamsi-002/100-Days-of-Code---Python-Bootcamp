from art import logo

print(logo)

def caesar(start_text, shift_number, shift_direction):
        end_text = ""
        if shift_direction == "decode":
            shift_number *= -1
        for c in start_text:
            if c not in alphabets:
                end_text += c
                continue
            letter_position = alphabets.index(c)
            end_text += alphabets[(letter_position+shift_number)%26]

        return end_text

end_game = False
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while not end_game:
    print("\nWelcome to the Caesar Cipher Program!")
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    if direction not in ["encode", "decode"]:
        print("Invalid input. Please type 'encode' or 'decode'.")
        continue

    text = input("Type your message:\n").lower()

    try:
        shift = int(input("Type the shift number:\n"))
    except ValueError:
        print("Invalid shift number. Please enter an integer.")
        continue
    
    result = caesar(start_text=text, shift_number=shift, shift_direction=direction)
    print(f"\nHere's the {direction}d result: {result}")

    continue_game = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()

    if continue_game != "yes":
        print("GoodBye!!!")
        end_game = True