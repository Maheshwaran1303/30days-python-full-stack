# Introduction to Modules
# Definition: A module is a file containing Python definitions and statements.
# A module can define functions, classes, and variables, and can also include runnable code.
# Purpose: Code reuse and organization. It allows dividing large programs into small manageable and organized files.

# Syntax for Importing Modules
# import module_name

# Creating a Module
# A Python file (.py) containing functions or variables is considered a module.
# Example module: my_module.py

def greet(name):
    """
    Function to greet a person.
    Args:
    name (str): The name of the person to greet.

    Returns:
    str: A greeting message.
    """
    return f"Hello, {name}!"


# Using a Module
# Example: main.py

import my_module  # Import the module

# Print the greeting message
print(my_module.greet("Mahesh"))  # Outputs: Hello, Mahesh!


# Importing from a Module

# Importing Specific Functions or Variables
from my_module import greet  # Importing specific function

print(greet("Mahesh"))  # Outputs: Hello, Mahesh!

# Importing All Functions and Variables
# from my_module import *

# Aliasing a Module
import my_module as mm  # Alias for the module

print(mm.greet("Mahesh"))  # Outputs: Hello, Mahesh!


# Built-in Python Modules
# Example using math module

import math  # Importing the built-in math module

# Using math functions
print(math.sqrt(16))  # Outputs: 4.0
print(math.pi)  # Outputs: 3.141592653589793


# Example using random module
import random  # Importing the built-in random module

# Generate a random integer between 1 and 10
print(random.randint(1, 10))  # Outputs a random integer


# Packages
# A package is a directory that contains multiple Python modules.
# Purpose: To organize modules into directories (like a folder structure).
# Example structure of a package:
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# Creating a Package:
# Step 1: Create a directory called my_package.
# Step 2: Add a file called __init__.py to indicate it is a package.
# Step 3: Add modules (module1.py, module2.py).

# Importing from a Package
from my_package import module1  # Import module1 from the package

# Example function call from module1
print(module1.some_function())


# Relative Imports in Packages
# Within a package, you can use relative imports to refer to sibling modules.
# Example:
# from .module1 import some_function


# The __name__ Variable in Modules
# Each module has a __name__ variable that is set to "__main__" when the module is run as the main program.
# This allows code to run only when executed directly, not when imported.

def greet():
    """
    Function to greet the world.
    Prints a simple greeting message.
    """
    print("Hello, World!")

# Run this block only if this file is executed directly
if __name__ == "__main__":
    greet()


# The dir() Function
# Purpose: Returns a list of all the attributes (functions, variables, etc.) in a module.

# Example:
import math  # Importing math module
print(dir(math))  # Outputs a list of all functions and variables in the math module


# Installing External Modules

# Using pip to install modules:
# Command: pip install module_name

# Example: pip install requests

# Using External Module in Python
import requests  # Import the requests module

# Sending a request to a website
response = requests.get("https://api.github.com")
print(response.status_code)  # Outputs the status code of the response


# Tasks and Exercises

# Task 1: Create a module with a function that takes a list and returns the sum of its elements. Use this module in another file.

def list_sum(numbers):
    """
    Function to return the sum of elements in a list.
    Args:
    numbers (list): List of numbers.

    Returns:
    int: Sum of the numbers in the list.
    """
    return sum(numbers)


# Task 2: Write a Python program that uses the math module to calculate the factorial of a number.

def calculate_factorial(n):
    """
    Function to calculate the factorial of a number.
    Args:
    n (int): The number to calculate the factorial of.

    Returns:
    int: Factorial of the number.
    """
    return math.factorial(n)


# Task 3: Create a package named utilities with two modules: string_util.py and math_util.py
# Import and use these functions from the package.

# Task 4: Write a Python script that uses the os module to list all files and directories in a specified path.

import os  # Importing the os module

# List files and directories in the current path
def list_files_in_directory(path):
    """
    Function to list all files and directories in a specified path.
    Args:
    path (str): Path to list files and directories.

    Returns:
    list: List of files and directories in the path.
    """
    return os.listdir(path)


# Task 5: Create a Python script that checks if a website is reachable using the requests module.

def check_website_status(url):
    """
    Function to check if a website is reachable.
    Args:
    url (str): The URL of the website to check.

    Returns:
    int: Status code of the website.
    """
    response = requests.get(url)
    return response.status_code


# Task 6: Write a program that imports a module using an alias and demonstrates the use of two functions.

import random as rnd  # Alias for the random module

def generate_random_number():
    """
    Function to generate a random integer between 1 and 10.
    Returns:
    int: A random integer.
    """
    return rnd.randint(1, 10)


def choose_random_element(elements):
    """
    Function to choose a random element from a list.
    Args:
    elements (list): List of elements.

    Returns:
    any: A random element from the list.
    """
    return rnd.choice(elements)


# Task 7: Create two Python modules for basic math operations and advanced operations.

def add(a, b):
    """
    Function to add two numbers.
    Args:
    a (int): First number.
    b (int): Second number.

    Returns:
    int: Sum of the two numbers.
    """
    return a + b

def subtract(a, b):
    """
    Function to subtract one number from another.
    Args:
    a (int): First number.
    b (int): Second number.

    Returns:
    int: Result of the subtraction.
    """
    return a - b


# Advanced operations
def power(base, exp):
    """
    Function to calculate the power of a number.
    Args:
    base (int): The base number.
    exp (int): The exponent.

    Returns:
    int: Result of base raised to the power exp.
    """
    return base ** exp


def square_root(n):
    """
    Function to calculate the square root of a number.
    Args:
    n (int): The number to calculate the square root of.

    Returns:
    float: Square root of the number.
    """
    return math.sqrt(n)
