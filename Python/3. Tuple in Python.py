# *Structure for Python Tuples*

# 1. Introduction to Tuples
# Tuples are immutable, ordered collections of elements. Once created, elements in a tuple cannot be modified.

# Syntax:
# Define a tuple with parentheses ()
my_tuple = (element1, element2, element3)

# Tuples are often used when you want to ensure that the data remains unchanged.
# Example:
my_tuple = (1, 2, 3)
print(my_tuple)  # Outputs: (1, 2, 3)

# 2. Creating Tuples

# a) Creating a Tuple
# Tuples can be created with zero or multiple elements
empty_tuple = ()  # Empty tuple
single_element_tuple = (42,)  # Note the comma for a single element tuple
multiple_element_tuple = (1, 2, 3, "apple")  # Tuple with mixed types

# b) Tuple Packing and Unpacking
# Tuple packing and unpacking is used to assign values to variables
# Packing: Creating a tuple by grouping multiple values.
# Unpacking: Assigning values from a tuple to multiple variables.

# Example:
my_tuple = ("Mahesh", 25, "Manager")  # Packing values into a tuple
name, age, profession = my_tuple  # Unpacking tuple into variables

print(name)       # Outputs: Mahesh
print(age)        # Outputs: 25
print(profession) # Outputs: Manager

# 3. Accessing Tuple Elements

# a) Indexing
# Access tuple elements by their index (starting from 0)
my_tuple = (10, 20, 30, 40)
print(my_tuple[1])  # Outputs: 20

# b) Negative Indexing
# Access elements from the end of the tuple using negative indices.
print(my_tuple[-1])  # Outputs: 40

# c) Slicing
# Use slicing to get a subset of elements from a tuple.
# Syntax: tuple[start:end:step]
print(my_tuple[1:3])  # Outputs: (20, 30)
print(my_tuple[::-1])  # Outputs: (40, 30, 20, 10)

# 4. Tuple Immutability

# a) Immutability
# Tuples cannot be modified after creation.
my_tuple = (1, 2, 3)
# Uncommenting the next line will raise an error as tuples are immutable
# my_tuple[1] = 10  # This will raise an error

# 5. Tuple Methods and Functions

# a) Common Tuple Methods
# Tuples support the count() and index() methods.
# count(): Returns the number of times a value appears in a tuple.
# index(): Returns the index of the first occurrence of a value.
my_tuple = (1, 2, 3, 2, 2, 4)
print(my_tuple.count(2))  # Outputs: 3
print(my_tuple.index(1))  # Outputs: 2

# b) Functions with Tuples
# len(), max(), min(), sum() can be used with tuples.
my_tuple = (1, 2, 3, 4)
print(len(my_tuple))  # Outputs: 4
print(max(my_tuple))  # Outputs: 4
print(min(my_tuple))  # Outputs: 1
print(sum(my_tuple))  # Outputs: 10

# 6. Nested Tuples

# a) Accessing Elements in a Nested Tuple
# Nested tuples can contain other tuples as elements.
nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
print(nested_tuple[1])       # Outputs: (4, 5, 6)
print(nested_tuple[1][2])    # Outputs: 6

# 7. Tuple vs List

# a) Differences Between Tuples and Lists
# - Tuples are immutable while lists are mutable.
# - Lists use square brackets ([]), tuples use parentheses (()).
# - Tuples are faster than lists due to immutability, which allows optimization.

# 8. Converting Between Lists and Tuples

# a) Converting a List to a Tuple
# Use tuple() to convert a list to a tuple.
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_tuple)  # Outputs: (1, 2, 3)

# b) Converting a Tuple to a List
# Use list() to convert a tuple to a list.
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)  # Outputs: [1, 2, 3]

# 9. Tasks and Exercises

# Task 1: Create a tuple with 5 different elements and print each element using a loop.
my_tuple = (10, "apple", 3.14, True, 42)
for item in my_tuple:
    print(item)

# Task 2: Write a Python function that takes a tuple of numbers and returns the largest element.
def find_largest(t):
    return max(t)

num_tuple = (10, 20, 5, 40)
print(find_largest(num_tuple))  # Outputs: 40

# Task 3: Given a tuple of integers, write a Python program to reverse the tuple.
def reverse_tuple(t):
    return t[::-1]

int_tuple = (1, 2, 3, 4, 5)
print(reverse_tuple(int_tuple))  # Outputs: (5, 4, 3, 2, 1)

# Task 4: Create a tuple containing the first 10 Fibonacci numbers.
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return tuple(fib)

print(fibonacci(10))  # Outputs: (0, 1, 1, 2, 3, 5, 8, 13, 21, 34)

# Task 5: Convert a tuple containing numbers into a list and find the sum of the elements in the list.
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)
print(sum(my_list))  # Outputs: 15

# Task 6: Write a Python program to check if an element exists in a tuple.
def element_exists(t, element):
    return element in t

my_tuple = (1, 2, 3, 4, 5)
print(element_exists(my_tuple, 3))  # Outputs: True
print(element_exists(my_tuple, 10))  # Outputs: False
