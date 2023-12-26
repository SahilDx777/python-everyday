import os 
import random
from words import hangman_words
from lives import  logo, stages



end_of_game = False
chose_variable = random.choice(hangman_words).lower()
word_length = len(chose_variable)

lives = 6

print(logo)


display = []
for _ in range(word_length):
    display += "_"


while not end_of_game:
    guess_letter = input("Guess a letter: ").lower()
    
    clear = os.system('clear')
    
    if guess_letter in display:
        print(f"You've guessed the letter already.")


    for position in range(word_length):
        letter = chose_variable[position]
        # print(f"current position: {position}\n current letter: {letter}\n guess letter: {guess_letter}")
        if letter == guess_letter:
            display[position] = letter
    
    if guess_letter not in chose_variable:
        print(f"You gussed {guess_letter}, that's not in the word. You loose a life.")
        lives -= 1       
        if lives == 0:
           end_of_game = True 
           print("You Lost!")
             
            
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You Won!")
        
        
    print(stages[lives])    