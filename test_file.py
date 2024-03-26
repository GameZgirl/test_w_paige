import math

def placeholder():
    pass

# Get user input
user_input = input("Enter a number: ")

while(True): 
    # Convert input to an integer
    try:
        number = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        exit()

    # Check if the number is even
    if number % 2 == 0:
        print("I love you")
        break
    else:
        print("Please type an even number.")
