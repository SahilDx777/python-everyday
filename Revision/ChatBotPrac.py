from datetime import datetime
import sys


def get_response(text) -> str:

    lowered = text.lower()

    if lowered in ["hello", "hi", "hey"]:
        return "Hey there!"
    elif "how are you" in lowered:
        return "I'm good, Thanks!"
    elif "your name" in lowered:
        return "My name is Chat Bot!"
    elif "time" in lowered:
        curr_time = datetime.now()
        return f"The time is: {curr_time:%H:%M}"
    elif lowered in ["bye", "goodbye", "see you"]:
        return "It was nice talking to you"
    else:
        return f"I don't understand, please try again your, TEXT: {text}"


while True:
    print("Hello and Welcome to Chat Bot!")
    user_input = input("You: ")

    if user_input == "exit":
        print("Bot: It was pleasure talking to you!")
        sys.exit()
    bot_response = get_response(user_input)
    print(f"Bot: {bot_response}")
