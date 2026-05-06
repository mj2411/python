import random

def guess_the_number():
    secret_num = random.randint(1, 50)
    guess = None
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 50.")

    while guess != secret_num:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_num:
                print("Too low! Try again.")
            elif guess > secret_num:
                print("Too high! Try again.")
            else:
                print(f" Correct! You found it in {attempts} attempts.")
        
        except ValueError:
            print("Please enter a valid whole number.")

if __name__ == "__main__":
    guess_the_number()