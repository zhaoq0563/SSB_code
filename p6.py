import sys
import random

hangman_figures = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """
]

def display_hangman(tries):
    print(hangman_figures[tries])

name = input("What is your name?\n")

def run():
    print(f"Hello, {name}, let's play hangman!")
    turns = 0
    display_hangman(turns)
    print("Start guessing...")
    # Defining the bag of words
    bag_of_words = ['Edureka', "python", "machinelearning", "looping", "whileloop", "devops", "forloop", "deeplearning",
                    "oops", "condition", "preprocessing", "modelling", "algorithms", "parameters", "control",
                    "exception", "nomalization"]
    word = random.choice(bag_of_words)
    guesses = " "
    while turns < 6:
        failed = 0
        for char in word:
            if char in guesses:
                print(char, end=" ")
            else:
                print("_", end=" ")
                failed += 1
        print()
        if failed == 0:
            print("You win!")
            choice = input("Would you like to play again? y/n\n")
            if "y" in choice:
                run()
            elif "n" in choice:
                sys.exit()
            else:
                print("Something went wrong, type y or n.")
        guess = input("Guess a character:")
        guesses += guess
        if guess not in word:
            turns += 1
            print("Wrong!")
            print(f"You have {6-turns} more guesses.")
            display_hangman(turns)
            print("\n")

            if turns == 6:
                print("You lose!")
                choice = input("Would you like to play again? y/n\n")
                if "y" in choice:
                    run()
                elif "n" in choice:
                    sys.exit()
                else:
                    print("Something went wrong, type y or n.")


run()
