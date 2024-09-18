# Structure for Python Lists

# 1. Introduction to Lists
# Lists are mutable, ordered, and heterogeneous.
# Syntax:
# my_list = [element1, element2, element3]

# Lists are mutable, meaning elements can be changed after creation.

"""
2. Creating and Accessing Lists
"""

# a) Creating a List
# Example:
my_list = [1, 2, 3, "apple", True]
print(my_list)  # Outputs: [1, 2, 3, "apple", True]

# b) Accessing Elements
# Use index numbers to access list items.
# Example:
my_list = ["apple", "banana", "cherry"]
print(my_list[0])  # Outputs: apple
print(my_list[-1])  # Outputs: cherry (negative indexing)


"""
3. Modifying Lists
"""

# a) Changing Elements
# Example:
my_list = [1, 2, 3]
my_list[1] = "changed"
print(my_list)  # Outputs: [1, "changed", 3]

# b) Adding Elements
# append(): Adds an item to the end of the list.
# insert(): Adds an item at a specific index.
# Example:
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Outputs: [1, 2, 3, 4]

my_list.insert(1, "inserted")
print(my_list)  # Outputs: [1, "inserted", 2, 3, 4]

# c) Removing Elements
# remove(), pop(), and del are used for removal.
# Example:
my_list = [1, 2, 3, 4]
my_list.remove(2)
print(my_list)  # Outputs: [1, 3, 4]

my_list.pop(1)
print(my_list)  # Outputs: [1, 4]

del my_list[0]
print(my_list)  # Outputs: [4]

"""
4. List Slicing
"""

# a) Slicing a List
# Syntax: list[start:end:step]
# Example:
my_list = [10, 20, 30, 40, 50]
print(my_list[1:4])  # Outputs: [20, 30, 40]
print(my_list[:3])   # Outputs: [10, 20, 30]
print(my_list[::2])  # Outputs: [10, 30, 50]


"""
5. List Comprehension
"""

# a) Basic List Comprehension
# Syntax: [expression for item in iterable]
# Example:
my_list = [x**2 for x in range(5)]
print(my_list)  # Outputs: [0, 1, 4, 9, 16]

# b) Conditional List Comprehension
# Example:
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # Outputs: [0, 4, 16, 36, 64]

"""
6. Looping Through a List
"""

# a) Using for Loop
# Example:
my_list = ["apple", "banana", "cherry"]
for fruit in my_list:
    print(fruit)

# b) Using while Loop
# Example:
my_list = [1, 2, 3, 4, 5]
i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

"""
7. List Functions and Methods
"""

# a) Common List Methods: len(), max(), min(), sort(), reverse()
# Example:
my_list = [3, 1, 4, 1, 5, 9]
print(len(my_list))  # Outputs: 6
my_list.sort()
print(my_list)  # Outputs: [1, 1, 3, 4, 5, 9]
my_list.reverse()
print(my_list)  # Outputs: [9, 5, 4, 3, 1, 1]

"""
8. Nested Lists
"""

# a) Accessing Elements in a Nested List
# Example:
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested_list[1][2])  # Outputs: 6

"""
9. Tasks and Exercises
"""

# Task 1: Write a Python program to find the sum of all the elements in a list.

# Task 2: Create a list of squares of numbers from 1 to 10 using list comprehension.

# Task 3: Write a Python function that removes duplicates from a list.

# Task 4: Given a list of integers, write a Python program to find the second largest element.

# Task 5: Write a Python program to sort a list of strings based on their lengths.

# Task 6: Write a Python program that uses slicing to reverse a list.

# Task 7: Create a nested list and write a program to access elements from it using a loop.
