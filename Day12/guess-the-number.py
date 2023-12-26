import random
import os

EASY_LEVEL = 10
HARD_LEVEL = 5


#! Function to check answers
def check_answer(make_a_guess, answer, turns):
    """Check answers against guess. Returns the number of turns remaining"""
    if make_a_guess > answer:
        print("Too high!")
        return turns - 1
    elif make_a_guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}")


#! Function to set Difficulty
def set_difficulty():
    difficulty = input("choose difficulty. Type 'easy' or 'hard'\n")
    if difficulty == "easy":
        return EASY_LEVEL
    else:
        return HARD_LEVEL


def game():

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 100)
    print(f"ans = {answer}")

    #! Set Difficulty
    turns = set_difficulty()

    #! Repeat the guessing functionality if they got wrong answers
    make_a_guess = 0
    while make_a_guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")

        #! Let User Guess Number
        make_a_guess = int(input("Make a guess: "))

        #! track the number of turns and reduce -1 if wrong
        turns = check_answer(make_a_guess, answer, turns)
        if turns == 0:
            print("You ran out of guesses, You Lost!")
            return
        elif make_a_guess != answer:
            print("Guess Again.")


def play_again():
    play_again = input("\nWould you like to play again? Types 'yes' or 'no'\n")
    if play_again == "yes":
        os.system('clear')
        game()

    elif play_again == "no":
        os.system('clear')
        print("Thanks for playing!")


game()
play_again()
