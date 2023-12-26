import random

rock = '''  
    _______
---'   ____)  
      (_____)  
      (_____)  
      (____)
---.__(___)  
'''

paper = '''  
    _______
---'   ____)____  
          ______)  
          _______)  
         _______)
---.__________)  
'''

scissors = '''  
    _______
---'   ____)____  
          ______)  
       __________)  
      (____)
---.__(___)  
'''

game_img = [rock, paper, scissors]
user_choice = int(input("what do you choose? Type 0 for rock , type 1 for paper, type 2 for scissors.\n"))
if user_choice >= 3 or user_choice < 0:
    print("Invalid Input")
else:
    print(game_img[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer Chose:")
    print(game_img[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You Won!!!")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lost! :(")
    elif computer_choice > user_choice:
        print("You Lost! :(")
    elif user_choice > computer_choice:
        print("You Won!!!")
    elif computer_choice == user_choice:
        print("It's a Tie!")