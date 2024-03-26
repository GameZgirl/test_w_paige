import math
import pyjokes

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)

def main():
    print("Welcome to the Random Joke Maisy!")
    while True:
        print("\nPress 'Enter' to hear a joke or type 'exit' to quit.")
        user_input = input().strip().lower()
        if user_input == 'exit':
            print("Thank you for using the Random Joke Generator. Have a great day!")
            break
        else:
            tell_joke()

if __name__ == "__main__":
    main()

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
