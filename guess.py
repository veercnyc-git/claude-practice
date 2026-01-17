import random  # Import the random module to generate random numbers

# Print a welcome message to the player
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print()  # Print a blank line for better readability

# Generate a random number between 1 and 100 (inclusive)
# This is the secret number the player needs to guess
secret_number = random.randint(1, 100)

# Initialize a variable to count how many guesses the player makes
attempts = 0

# Initialize a variable to store the player's guess
# We start with None to indicate they haven't guessed yet
guess = None

# Keep looping until the player guesses correctly
# The loop continues as long as guess is not equal to secret_number
while guess != secret_number:
    # Ask the player for their guess
    # input() returns a string, so we need to convert it to an integer
    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        # If the player enters something that's not a number,
        # we catch the error and ask them to try again
        print("Please enter a valid number!")
        continue  # Skip the rest of this loop iteration and start over
    
    # Increase the attempt counter by 1
    attempts += 1
    
    # Check if the guess is too low
    if guess < secret_number:
        print("Too low! Try again.")
    # Check if the guess is too high
    elif guess > secret_number:
        print("Too high! Try again.")
    # If it's not too low or too high, it must be correct!
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts!")
        print(f"The number was {secret_number}.")

# Ask if the player wants to play again
play_again = input("Would you like to play again? (yes/no): ")

# Check if they said yes (we use .lower() to handle "Yes", "YES", etc.)
if play_again.lower() == "yes":
    print("Great! Restarting the game...")
    print()
    # Note: In a real game, you'd want to put all the game logic in a loop
    # or a function to actually restart. For now, just run the program again!
else:
    print("Thanks for playing! Goodbye!")