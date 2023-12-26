def greet_with(name, location):
    print(f"Hello, {name}!")
    print(f"I'm from {location}.")


greet_with("Bob", "Planet Earth")


#! Function with keyword arguments
def greet(a, b):
    print(f"Hello, {a}!")
    print(f"What is it like in {b}.")


greet(a="Max", b="Utopia")
