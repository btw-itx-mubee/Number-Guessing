import random


def guess_number():
    secret_number = random.randint(1, 100)


    attempts = 0
    max_attempts = 10


    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 to 100. Can you guess the Number? : ")


    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))

            if guess == secret_number:
                print("Great!, You Guessed the correct Number!")
                break
            elif guess < secret_number:
                print("Too low. Try Again!")
            else:
                print("Too high. Try Again!")
            
            attempts += 1
        
        except ValueError:
            print("Invalid Input. PLease enter a valid number.")

    else:
        print(f"Sorry, You have rum out of attempts. The Correct number was {secret_number}.")

if __name__ == "__main__":
    guess_number()