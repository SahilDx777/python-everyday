users = {
    "Bob": "1234",
    2: "James"
}

empty = {}
print(users["Bob"])  # ! Prints 1234 from users dictionary with key "Bob"
print(users[2])  # ! Prints James from users dictionary with key 2
print(empty)

weather = {
    "time": "10:00",
    "city": "London",
    "temperature": 20,
    "weather": "sunny"
}

# ! Prints London from weather dictionary with key "city"
print(weather["city"])
# ! Prints 20 from weather dictionary with key "temperature"
print(weather["temperature"])
# ! Prints sunny from weather dictionary with key "weather"
print(weather["weather"])
