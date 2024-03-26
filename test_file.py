import math
import pyjokes

def tell_joke():
    joke = pyjokes.get_joke()
    print(joke)

def main():
    print("Welcome to the Random Joke Generator!")
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