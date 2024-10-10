# Operators in Python

"""
1. Introduction to Operators

Definition: Operators are special symbols in Python that perform arithmetic or logical operations on values or variables.
Types of Operators:
  1. Arithmetic Operators 
  2. Comparison (Relational) Operators
  3. Logical Operators
  4. Bitwise Operators
  5. Assignment Operators
  6. Identity Operators
  7. Membership Operators
"""

# 1. Arithmetic Operators

"""
a) Definition: Used to perform basic mathematical operations.
Operators:
  + : Addition
  - : Subtraction
  * : Multiplication
  / : Division (returns float)
  // : Floor division (returns integer)
  % : Modulus (returns remainder)
  ** : Exponentiation
"""

# Example:
a = 10
b = 3
print(a + b)  # Outputs: 13
print(a - b)  # Outputs: 7
print(a * b)  # Outputs: 30
print(a / b)  # Outputs: 3.33
print(a // b)  # Outputs: 3
print(a % b)  # Outputs: 1
print(a ** b)  # Outputs: 1000

# 2. Comparison (Relational) Operators

"""
a) Definition: Used to compare two values, resulting in a boolean value (True or False).
Operators:
  == : Equal to
  != : Not equal to
  > : Greater than
  < : Less than
  >= : Greater than or equal to
  <= : Less than or equal to
"""

# Example:
a = 5
b = 3
print(a == b)  # Outputs: False
print(a != b)  # Outputs: True
print(a > b)   # Outputs: True
print(a < b)   # Outputs: False

# 3. Logical Operators

"""
a) Definition: Used to combine conditional statements.
Operators:
  and : Returns True if both statements are true
  or : Returns True if one of the statements is true
  not : Reverses the result; returns False if the result is true
"""

# Example:
a = True
b = False
print(a and b)  # Outputs: False
print(a or b)   # Outputs: True
print(not a)    # Outputs: False

# 4. Bitwise Operators

"""
a) Definition: Used to perform bit-level operations on integers.
Operators:
  & : Bitwise AND
  | : Bitwise OR
  ^ : Bitwise XOR
  ~ : Bitwise NOT
  << : Left shift
  >> : Right shift
"""

# Example:
a = 5  # In binary: 101
b = 3  # In binary: 011
print(a & b)  # Outputs: 1 (binary: 001)
print(a | b)  # Outputs: 7 (binary: 111)
print(a ^ b)  # Outputs: 6 (binary: 110)
print(~a)     # Outputs: -6 (bitwise inversion of 101)
print(a << 1) # Outputs: 10 (binary: 1010)
print(a >> 1) # Outputs: 2 (binary: 10)

# 5. Assignment Operators

"""
a) Definition: Used to assign values to variables.
Operators:
  = : Assign
  += : Add and assign
  -= : Subtract and assign
  *= : Multiply and assign
  /= : Divide and assign
  //= : Floor divide and assign
  %= : Modulus and assign
  **= : Exponent and assign
"""

# Example:
a = 10
a += 5  # Equivalent to a = a + 5
print(a)  # Outputs: 15
a -= 2   # Equivalent to a = a - 2
print(a)  # Outputs: 13

# 6. Identity Operators

"""
a) Definition: Used to compare the memory locations of two objects.
Operators:
  is : Returns True if both variables are the same object
  is not : Returns True if both variables are not the same object
"""

# Example:
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print(a is b)  # Outputs: False (different memory locations)
print(a is c)  # Outputs: True (same memory location)
print(a is not b)  # Outputs: True

# 7. Membership Operators

"""
a) Definition: Used to test if a sequence contains a certain value.
Operators:
  in : Returns True if a value is found in the sequence
  not in : Returns True if a value is not found in the sequence
"""

# Example:
a = [1, 2, 3, 4]
print(2 in a)  # Outputs: True
print(5 not in a)  # Outputs: True

"""
Tasks and Exercises:

Task 1: Write a program that takes two numbers from the user and uses all the arithmetic operators to show the results.
Task 2: Write a program to check if a number is greater than or equal to 10 using a comparison operator.
Task 3: Use logical operators to check if a number is both even and positive.
Task 4: Write a program that takes two integers and performs bitwise operations (AND, OR, XOR, left shift, right shift) on them.
Task 5: Write a program to calculate the sum of a list of numbers using a loop and the += assignment operator.
Task 6: Write a program to check if two variables point to the same object using identity operators.
Task 7: Create a program that checks if a specific character is in a string using membership operators.
Task 8: Write a function that accepts two lists and returns True if both lists share at least one common element, using membership operators.
Task 9: Create a program to perform basic operations on a given number using assignment operators (+=, -=, *=, etc.).
Task 10: Write a program to check if a given list of numbers contains only even numbers using the all() function and logical operators.
"""
