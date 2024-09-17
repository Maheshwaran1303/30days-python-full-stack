# Introduction to Functions in Python

"""
A function is a block of organized, reusable code that performs a single action.
Types of Functions:
1. Built-in functions (like print(), len())
2. User-defined functions
"""

# 1. Defining and Calling Functions

# Defining a basic function without parameters
def greet():
    """This function prints a welcome message."""
    print("Hello, welcome to the course!")

# Calling the function
greet()


# 2. Functions with Parameters

# Defining a function with a parameter
def greet(name):
    """This function takes a name as a parameter and greets the user."""
    print(f"Hello, {name}!")

# Calling the function with an argument
greet("Mahesh")


# 3. Returning Values from Functions

# Defining a function that returns a value
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b

# Calling the function and storing the result
result = add(5, 3)
print(result)  # Outputs: 8


# Returning multiple values as a tuple
def arithmetic_operations(a, b):
    """This function returns multiple arithmetic operations as a tuple."""
    return a + b, a - b, a * b

# Calling the function and unpacking the result
result = arithmetic_operations(10, 5)
print(result)  # Outputs: (15, 5, 50)


# 4. Function Parameters

# Positional arguments example
def subtract(a, b):
    """This function subtracts the second number from the first."""
    return a - b

print(subtract(10, 5))  # Outputs: 5


# Keyword arguments example
def greet(name, message="Hello"):
    """This function greets the user with a custom message."""
    print(f"{message}, {name}!")

greet(name="John", message="Hi")  # Outputs: Hi, John!


# Default parameter example
greet("Alice")  # Outputs: Hello, Alice!


# Arbitrary arguments (*args) example
def add(*numbers):
    """This function adds an arbitrary number of numbers."""
    return sum(numbers)

print(add(1, 2, 3))  # Outputs: 6


# Keyword Arbitrary arguments (**kwargs) example
def print_details(**details):
    """This function prints key-value pairs passed as keyword arguments."""
    for key, value in details.items():
        print(f"{key}: {value}")

print_details(name="Alice", age=25, city="New York")


# 5. Lambda Functions (Anonymous Functions)

# Lambda function to find the square of a number
square = lambda x: x * x
print(square(5))  # Outputs: 25


# Using lambda with map() to square each number in a list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Outputs: [1, 4, 9, 16]


# 6. Scope of Variables

# Local variable example
def example_local():
    """This function demonstrates local variables."""
    x = 10  # Local variable
    print(x)

example_local()


# Global variable example
x = 5  # Global variable

def example_global():
    """This function accesses a global variable."""
    print(x)  # Accessing global variable

example_global()  # Outputs: 5


# Modifying global variable using the global keyword
def modify_global():
    """This function modifies a global variable."""
    global x
    x = 10

modify_global()
print(x)  # Outputs: 10


# 7. Recursion

# Recursive function to compute factorial of a number
def factorial(n):
    """This function calculates factorial using recursion."""
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Outputs: 120


# 8. Tasks and Exercises

# Task 1: Function to return the sum of two numbers
def sum_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b


# Task 2: Function to check if a number is prime
def is_prime(num):
    """Returns True if the number is prime, otherwise False."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Task 3: Function to reverse a string
def reverse_string(s):
    """Returns the reversed string."""
    return s[::-1]


# Task 4: Function to find the maximum number in a list
def find_max(numbers):
    """Returns the maximum number in a list."""
    return max(numbers)


# Task 5: Recursive function to compute the nth Fibonacci number
def fibonacci(n):
    """Returns the nth Fibonacci number using recursion."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Task 6: Lambda function to find square of a number with map()
square_lambda = lambda x: x * x
numbers = [1, 2, 3, 4]
squared_numbers = list(map(square_lambda, numbers))


# Task 7: Function with *args to return the product of all arguments
def product(*args):
    """Returns the product of all arguments."""
    result = 1
    for num in args:
        result *= num
    return result


# Task 8: Function using **kwargs to print student details
def print_student_details(**kwargs):
    """Prints student details using keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Task 9: Function using filter() to return even numbers from a list
def get_even_numbers(numbers):
    """Returns a list of even numbers from the input list."""
    return list(filter(lambda x: x % 2 == 0, numbers))


# Task 10: Recursive function to calculate the sum of the first n natural numbers
def sum_natural_numbers(n):
    """Returns the sum of the first n natural numbers using recursion."""
    if n == 1:
        return 1
    else:
        return n + sum_natural_numbers(n - 1)

