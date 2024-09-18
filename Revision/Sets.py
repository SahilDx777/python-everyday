elements = {99, True, "Bob"}  # ! sets are unordered
print(elements)

elements.add("TanKKK")  # ! add element
print(elements)

elements.remove("Bob")  # ! remove element
print(elements)

elements.pop()  # ! remove random element
print(elements)

elements.clear()  # ! remove all elements
# ! Prints the "set()" as an empty set instead of {} as a dictionary because sets are unordered and dictionaries are ordered by default in Python 3 and above versions of Python.
print(elements)
