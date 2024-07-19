import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!#$%&()*+'

print("Welcome to the PyPassword Generator")

try:
    num_letters = int(input("How many letters would you like in your password? \n"))
    num_numbers = int(input("How many numbers would you like? \n"))
    num_symbols = int(input("How many symbols would you like? \n"))
    
    password_list = [
        random.choice(letters) for _ in range(num_letters)
    ] + [
        random.choice(numbers) for _ in range(num_numbers)
    ] + [
        random.choice(symbols) for _ in range(num_symbols)
    ]

    random.shuffle(password_list)
    password = ''.join(password_list)
    print(f"Your password is: {password}")

except ValueError:
    print("Please enter valid numbers for the number of letters, numbers, and symbols.")
