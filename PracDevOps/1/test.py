import os

folders = input(
    "Please provide the names of the folders with spaces between them: ").split()

for folder in folders:
    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide a valid folder name")
        continue

    print(" ===== listing files for the folder - " + folder)

    for file in files:
        print(file)
