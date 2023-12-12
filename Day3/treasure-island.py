print('''
  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
 
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("\nYou find yourself at a crossroad.")
choice1 = input("Do you want to go left or right? ").lower()

if choice1 == "left":
    print("\nYou chose the left path.")
    print("You arrive at a mystical lake with a magical waterfall.")

    choice2 = input("Do you swim across the enchanted lake or take the hidden path around it? ").lower()

    if choice2 == "swim across":
        print("\nYou dive into the sparkling water and swim across.")
        print("As you reach the other side, you see a mysterious island.")

        choice3 = input(
            "On the island, you find a grand castle with three doors: red, blue, and yellow. Which door do you choose? ").lower()

        if choice3 == "red":
            print("\nYou open the red door and discover a room filled with treasure!")
            print("Congratulations! You found the treasure. You win!")
        elif choice3 == "blue":
            print("\nYou open the blue door and are surrounded by magical creatures. They guide you to safety.")
            print("They reward you with a small treasure. You win!")
        elif choice3 == "yellow":
            print("\nYou open the yellow door and find a room full of traps.")
            print("You narrowly escape and find a hidden passage leading to more treasure. You win!")
        else:
            print("\nInvalid choice. The castle crumbles, and you barely escape. Game over.")

    elif choice2 == "take the hidden path":
        print("\nYou choose the hidden path, filled with glowing fireflies.")
        print("The path leads you to a secret cave with a mysterious inscription.")

        choice4 = input("Do you decipher the inscription or continue without understanding it? ").lower()

        if choice4 == "decipher":
            print("\nYou decipher the inscription and discover a shortcut to the treasure.")
            print("Congratulations! You found the treasure. You win!")
        else:
            print("\nYou continue without understanding the inscription.")
            print("You encounter a friendly hermit who guides you to the treasure. You win!")

    else:
        print("\nYou got attacked by an angry water serpent. Game over.")

elif choice1 == "right":
    print("\nYou chose the right path.")
    print("You find a dark cave with glowing crystals.")

    choice5 = input("Do you enter the cave or climb the mountain beside it? ").lower()

    if choice5 == "enter the cave":
        print("\nYou enter the cave and discover a hidden treasure chamber.")
        print("Congratulations! You found the treasure. You win!")
    elif choice5 == "climb the mountain":
        print("\nYou climb the mountain and encounter a wise old wizard.")

        choice6 = input("The wizard offers you a magical carpet or a magical amulet. Which do you choose? ").lower()

        if choice6 == "magical carpet":
            print("\nYou ride the magical carpet and find the treasure in the clouds.")
            print("Congratulations! You found the treasure. You win!")
        elif choice6 == "magical amulet":
            print("\nThe magical amulet protects you from traps in a hidden cave.")
            print("Congratulations! You found the treasure. You win!")
        else:
            print("\nInvalid choice. The wizard sends you on a detour. Game over.")

    else:
        print("\nYou trigger a rockslide while climbing. Game over.")

else:
    print("\nYou stumble in confusion and fall into a deep pit. Game over.")
