# 1. Introduction to Functions
# A function is a reusable block of code that performs a specific action.
# It helps in modularity, code organization, and reusability.

# 2. Defining and Calling Functions

# a) Defining a function without parameters
# Syntax: def function_name():
#             # code block
def welcome():
    """This function prints a welcomeing message."""
    print("Hello, welcome to the course!")  # Function body

# Calling the function using its name
welcome()  # Outputs: Hello, welcome to the course!


# b) Defining a function with parameters
# Syntax: def function_name(param1, param2):
#             # code block
def welcome_with_name(name):
    """This function takes a parameter 'name' and prints a personalized welcomeing."""
    print(f"Hello, {name}!")  # Using the parameter in the function body

# Calling the function with an argument (passing the value 'Mahesh')
welcome_with_name("Mahesh")  # Outputs: Hello, Mahesh!


# 3. Return Statement

# a) Function returning a single value
# Syntax: def function_name(parameters):
#             # code block
#             return value
def add(a, b):
    """This function returns the sum of two numbers."""
    return a + b  # Returning the result

# Calling the function and storing the result
result = add(5, 3)
print(result)  # Outputs: 8


# b) Returning multiple values as a tuple
def arithmetic_operations(a, b):
    """This function returns the sum, difference, and product of two numbers."""
    return a + b, a - b, a * b  # Returning multiple values

# Receiving multiple values from the function as a tuple
result = arithmetic_operations(10, 5)
print(result)  # Outputs: (15, 5, 50)


# 4. Function Parameters

# a) Positional Arguments: The order in which arguments are passed matters.
def subtract(a, b):
    """This function returns the difference of two numbers based on their order."""
    return a - b

# Positional arguments are passed in order
print(subtract(10, 5))  # Outputs: 5

# b) Keyword Arguments: Arguments passed with the parameter name.
def welcome(name, message="Hello"):
    """This function uses keyword arguments and a default value for the 'message' parameter."""
    print(f"{message}, {name}!")

# Passing keyword arguments
welcome(name="Manick", message="Hi")  # Outputs: Hi, Manick!
welcome(name="Manick")  # Outputs: Hello, Manick! (using default message)


# c) Default Parameters: Parameters with default values, used when arguments are not provided.
def welcome_default(name, message="Hello"):
    """This function has a default message if the argument is not passed."""
    print(f"{message}, {name}!")

welcome_default("Mahesh")  # Outputs: Hello, Mahesh! (default message used)


# d) Arbitrary Arguments (*args): Allows passing an arbitrary number of positional arguments.
def add_multiple(*numbers):
    """This function takes multiple arguments and returns their sum."""
    return sum(numbers)  # Using sum() to add all arguments

# Passing multiple arguments to the function
print(add_multiple(1, 2, 3, 4))  # Outputs: 10


# e) Arbitrary Keyword Arguments (**kwargs): Allows passing arbitrary keyword arguments.
def print_details(**details):
    """This function accepts keyword arguments and prints them."""
    for key, value in details.items():  # Looping through the keyword arguments
        print(f"{key}: {value}")

# Passing keyword arguments
print_details(name="Mahesh", age=25, city="New York")


# 5. Lambda Functions (Anonymous Functions)

# Syntax: lambda arguments: expression
# Used for small functions that do not need a name

# Lambda function to square a number
square = lambda x: x * x
print(square(5))  # Outputs: 25

# Using lambda with map() to square numbers in a list
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))  # Applies lambda to each item in the list
print(squared)  # Outputs: [1, 4, 9, 16]


# 6. Scope of Variables

# a) Local Variables: Defined inside a function and only accessible within that function.
def local_example():
    """This function defines a local variable."""
    x = 10  # Local variable
    print(x)

local_example()  # Outputs: 10


# b) Global Variables: Defined outside all functions and accessible globally.
x = 5  # Global variable

def global_example():
    """This function can access a global variable."""
    print(x)  # Accessing the global variable

global_example()  # Outputs: 5


# c) Global Keyword: Used to modify global variables inside a function.
x = 5  # Global variable

def modify_global():
    """This function modifies a global variable using the 'global' keyword."""
    global x  # Declaring that we are modifying the global 'x'
    x = 10

modify_global()  # Modifying the global variable
print(x)  # Outputs: 10


# 7. Recursion

# Recursion: A function calling itself to solve smaller instances of the problem.
def factorial(n):
    """This function computes the factorial of a number using recursion."""
    if n == 1:  # Base case
        return 1
    else:
        return n * factorial(n - 1)  # Recursive case

print(factorial(5))  # Outputs: 120


# 8. Tasks and Exercises for Students

# Task 1: Write a function that takes two numbers as input and returns their sum.
def sum_of_two(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Task 2: Write a function to check if a given number is prime.
def is_prime(num):
    """Returns True if the number is prime, False otherwise."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Task 3: Write a function that accepts a string and returns the reversed version of the string.
def reverse_string(s):
    """Returns the reversed version of the input string."""
    return s[::-1]

# Task 4: Create a function to find the maximum number from a list of numbers.
def find_max(numbers):
    """Returns the maximum number in a list."""
    return max(numbers)

# Task 5: Write a recursive function to compute the nth Fibonacci number.
def fibonacci(n):
    """Returns the nth Fibonacci number."""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Task 6: Create a lambda function to find the square of a number, then use it with the map() function on a list.
square_lambda = lambda x: x * x
numbers = [1, 2, 3, 4]
squared_numbers = list(map(square_lambda, numbers))

# Task 7: Write a function with *args that returns the product of all arguments passed.
def product_of_args(*args):
    """Returns the product of all arguments."""
    product = 1
    for num in args:
        product *= num
    return product

# Task 8: Write a function using **kwargs to print the details of a student (name, age, grade, etc.).
def student_details(**kwargs):
    """Prints the student details passed as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Task 9: Write a function that accepts a list of numbers and uses filter() to return only the even numbers.
def filter_even(numbers):
    """Returns a list of even numbers."""
    return list(filter(lambda x: x % 2 == 0, numbers))

# Task 10: Write a function to calculate the sum of the first n natural numbers using recursion.
def sum_of_natural_numbers(n):
    """Returns the sum of the first n natural numbers using recursion."""
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers(n - 1)
