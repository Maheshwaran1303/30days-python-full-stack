# Loops in Python

"""
1. Introduction to Loops

Loops allow for executing a block of code repeatedly.
Python supports two types of loops: for and while loops.
"""

# 2. For Loop

# a) Basic for Loop
"""
Definition:
The for loop iterates over a sequence (such as a list, tuple, string, or range).

Syntax:
    for variable in sequence:
        # code to execute in each iteration
"""
# Example:
fruits = ['apple', 'banana', 'cherry']
for i in fruits:
    print(i)  # Output each fruit in the list

# b) Using range() in a for Loop
"""
The range() function generates a sequence of numbers.
Syntax:
    for i in range(start, stop, step):
        # code to execute
"""
# Example:
for i in range(5):
    print(i)
    
for i in range(1, 6):
    print(i)  # Output numbers from 1 to 5

for i in range(1,6,2):
    print(i)
    
# c) Looping through Strings
"""
Strings are iterable, so you can loop through each character.

Example:
    for i in "string":
        # code to execute for each character
"""
# Example:
for i in "Mahesh":
    print(i)  # Output each character in the string

# d) Looping through Dictionaries
"""
Looping through keys, values, or both.
Example:
    for key, value in dictionary.items():
        # code to execute for each key-value pair
"""
# Example:
person = {"name": "Mahesh", "age": 25, "city": "Tenkasi"}
for key, value in person.items():
    print(key, value)  # Output each key and value in the dictionary

# e) Nested for Loops
"""
Definition:
A loop inside another loop.
Syntax:
    for i in sequence1:
        for j in sequence2:
            # code to execute
"""
# Example:
for i in range(3):
    for j in range(2):
        print(f"i = {i}, j = {j}")  # Output combinations of i and j

# f) Using break and continue
"""
break: Exits the loop entirely.
continue: Skips the current iteration and continues with the next one.
"""
# Examples:
# break
for i in range(5):
    if i == 3:
        break  # Exit the loop when i equals 3
    print(i)  # Output 0, 1, 2

# continue
for i in range(5):
    if i == 3:
        continue  # Skip the iteration when i equals 3
    print(i)  # Output 0, 1, 2, 4

# 3. While Loop

# a) Basic while Loop
"""
Definition:
The while loop runs as long as a condition is True.

Syntax:
    while condition:
        # code to execute
"""
# Example:
i = 1
while i <= 5:
    print(i)  # Output numbers from 1 to 5
    i += 1

# b) Using break and continue in while Loops
"""
break: Exits the loop entirely.
continue: Skips the current iteration and continues with the next one.
"""
# Examples:
# break
i = 1
while i <= 5:
    if i == 3:
        break  # Exit the loop when i equals 3
    print(i)  # Output 1, 2
    i += 1

# continue
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue  # Skip the iteration when i equals 3
    print(i)  # Output 1, 2, 4, 5
    i += 1

# c) Infinite while Loop
"""
Definition:
A loop that never ends unless a break condition is met.
"""
# Example:
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input == 'exit':
        break  # Exit the loop when user types 'exit'

# d) Nested while Loops
"""
Definition:
A while loop inside another while loop.
"""
# Example:
i = 1
while i <= 3:
    j = 1
    while j <= 2:
        print(f"i = {i}, j = {j}")  # Output combinations of i and j
        j += 1
    i += 1

# 4. Tasks and Exercises

# Task 1:
"""
Write a program to print the numbers from 1 to 10 using a for loop.
"""
for num in range(1, 11):
    print(num)

# Task 2:
"""
Use a for loop to iterate over a list of integers and print only the even numbers.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num)  # Output even numbers

# Task 3:
"""
Write a program to calculate the sum of numbers from 1 to 100 using a for loop.
"""
total_sum = 0
for num in range(1, 101):
    total_sum += num
print(total_sum)  # Output the sum

# Task 4:
"""
Write a program using a for loop to print a multiplication table for numbers 1 to 10.
"""
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")  # Output the multiplication table

# Task 5:
"""
Using a nested for loop, print a pattern like this:
   *
   * *
   * * *
   * * * *
   * * * * *
"""
for i in range(1, 6):
    print('* ' * i)  # Output the pattern

# Task 6:
"""
Write a program using a while loop to reverse a given number.
"""
number = int(input("Enter a number to reverse: "))
reversed_number = 0
while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number //= 10
print(reversed_number)  # Output the reversed number

# Task 7:
"""
Create a program that keeps asking the user for a number until they enter a number greater than 100, using a while loop.
"""
while True:
    number = int(input("Enter a number greater than 100: "))
    if number > 100:
        break  # Exit the loop when number is greater than 100

# Task 8:
"""
Write a program using a while loop to print all prime numbers between 1 and 50.
"""
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = 2
while num <= 50:
    if is_prime(num):
        print(num)  # Output prime numbers
    num += 1

# Task 9:
"""
Use a while loop to simulate a basic countdown timer from 10 to 1, printing "Blastoff!" when it finishes.
"""
count = 10
while count > 0:
    print(count)
    count -= 1
print("Blastoff!")  # Output "Blastoff!" after countdown

# Task 10:
"""
Create a program using nested while loops to print this pattern:
   1
   2 2
   3 3 3
   4 4 4 4
"""
i = 1
while i <= 4:
    j = 1
    while j <= i:
        print(i, end=' ')
        j += 1
    print()  # New line after each row
    i += 1
