from art import logo

def add(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mul(num1, num2):
    return num1 * num2

def div(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is not allowed."
    return num1 / num2

def calculation(num1, num2, operator):
    if operator == '+':
        return add(num1, num2)
    elif operator == '-':
        return sub(num1, num2)
    elif operator == '*':
        return mul(num1, num2)
    elif operator == '/':
        return div(num1, num2)
    else:
        return "Error: Invalid operator."

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Error: Please enter a valid number.")

print(logo)

end = False
num1 = get_number("What is your first number?\n")

while not end:
    operator = input("Pick an operator (+, -, *, /):\n")
    
    if operator not in ['+', '-', '*', '/']:
        print("Error: Invalid operator. Please select from +, -, *, or /.")
        continue

    num2 = get_number("What is your second number?\n")

    ans = calculation(num1, num2, operator)
    
    if isinstance(ans, str):  # Check if ans is an error message
        print(ans)
    else:
        print(f"The result of {num1} {operator} {num2} is {ans}")
        num1 = ans

    continue_game = input("Do you want to continue the game? Type 'yes' to continue or 'no' to exit:\n").lower()

    if continue_game == 'no':
        end = True
        print("Thank you for playing. Goodbye!")
    elif continue_game != 'yes':
        print("Invalid input. Exiting the game.")
        end = True
