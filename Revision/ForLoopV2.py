text = "Hello, world!"

for i in range(3):  # ! print line 3 times
    print(text)

people = ["Bob", "John", "Alice", "James", "Charlie"]

for person in people:  # ! print each person
    print(person)

for person in people:
    if len(person) > 4:  # ! print each person who contains more than 4 characters
        print(f"{person} has more than 4 characters")
    else:  # ! print each person who contains less than 4 characters
        print(f"{person} has less than 4 characters")
