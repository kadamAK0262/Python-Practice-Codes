import random

def guess_number():
    while True:
        
        secret_number = random.randint(1, 100)  # Generate a random number between 1 and 100
        # secret_number = 75
        attempts = 5 

        print("Welcome to the Guessing Game!")
        print(f"I'm thinking of a number between 1 and 100. You have {attempts} attempts to guess it.")

        while attempts > 0:
            guess = int(input("Enter your guess: "))

            if guess == secret_number:
                print("Congratulations! You guessed the number correctly!")
                break  
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")

            attempts -= 1
            print(f"You have {attempts} attempts left.")

        else:
            print("Sorry, you've run out of attempts. The number was:", secret_number)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

guess_number()




# play_again = "yes"
    
#     while play_again.lower() == "yes":