print("Welcome to the rollercoster!")
height = int(input("what your height in CM?\n"))
bill = 0

if height >= 120:
    print("You can Ride!")
    age = int(input("What's your age?\n"))
    if age < 12:
        bill = 10
        print("Your Ticket will be $10")
    elif age <= 18:
        bill = 15
        print("Your Ticket will be $15")
    elif age >= 45 and age <= 55:
        print("Welcome to Midlife crisis, Have a free ride")
    else:
        bill = 20
        print("Your Ticket will be $20")

    photos = input("Do you want a photo taken? Y or N\n")
    if photos == "Y" or photos == "y":
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry! Chotu")