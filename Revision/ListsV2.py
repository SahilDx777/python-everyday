my_list = ["Bob", "Charlie", "Alice", "James"]

print("Original list:", my_list)

my_list.append("TanKKK")  # ! add element at the end of the list
print(my_list)

my_list.remove("Bob")  # ! removes first element
print(my_list)

my_list.pop()  # ! removes last element
print(my_list)

my_list[0] = "TanKKK"  # ! change value
print(my_list)

my_list.insert(1, "Hello")  # ! add element at index 1
print(my_list)

my_list.clear()  # ! remove all elements
print(my_list)
