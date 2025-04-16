# Generate a random number (1 to 100)

import random

def guess_the_number():
    number = random.randint(1, 100)
    
    print('Welcome to the Number Guessing Game!')
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess the number.")

    # Loop for 10 attempts
    for i in range(10):
        guess = int(input(f"Attempt {i + 1}: Enter your guess: "))
        
        if guess == number:
            print("🎉 Congratulations! You guessed the number correctly!")
            break
        elif guess < number:
            print("📉 Too low. Try again.")
        else:
            print("📈 Too high. Try again.")
    else:
        print(f"❌ Sorry, you've used all your attempts. The number was {number}.")

# Call the function
guess_the_number()
