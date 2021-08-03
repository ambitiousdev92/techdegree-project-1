"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random


def start_game():
    """Psuedo-code Hints
    
    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".
    
    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.
    
    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    
    print("\n****Welcome to the Number Guessing Game!****\n")
    
    random_number = random.randint(1, 10)
    guess_count = 1
    high_score = None
    play_again = "y"
    
    while play_again == "y":
        guess = ""
        while guess != random_number:
            try:
                guess = int(input("Take a guess between 1 and 10:  "))
            except ValueError:
                print("Please choose a valid number.")
                continue
            else:
                if guess < 1 or guess > 10:
                    print("Please choose a number between 1 and 10.")
                elif guess > random_number:
                    print("Go lower.")
                    guess_count += 1
                elif guess < random_number:
                    print("Go higher.")
                    guess_count += 1
        print("\nCongratulations! It took you {} tries.".format(guess_count))
        if high_score == None or guess_count < high_score:
            high_score = guess_count
            
        play_again = input("Would you like to play again?  Y/N  ")
        if play_again.lower() == "n":
            print("\nThank you, come again!")
        else:
            print("\nThe HIGHSCORE is {}".format(high_score))
            random_number = random.randint(1, 10)
            guess = ""
            guess_count = 1

# Kick off the program by calling the start_game function.
start_game()