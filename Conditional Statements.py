# Conditional Statements in Python

"""
1. Introduction

Overview of Conditional Statements:
Conditional statements in Python allow you to execute different code blocks based on conditions.

Syntax:
    if condition:
        # code to execute if condition is true
"""

# 2. Basic Conditional Statements

# a) if Statement:
"""
Definition:
Executes a block of code if a specified condition is true.

Syntax:
    if condition:
        # code to execute if condition is true
"""

# Example:
age = 20
if age >= 18:
    print("You are eligible to vote.")  # Output if condition is true

# b) else Statement:
"""
Definition:
Executes a block of code if the if condition is false.

Syntax:
    if condition:
        # code if condition is true
    else:
        # code if condition is false
"""
# Example:
age = 16
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")  # Output if condition is false

# c) elif Statement:
"""
Definition:
Allows checking multiple conditions in sequence.

Syntax:
    if condition1:
        # code if condition1 is true
    elif condition2:
        # code if condition2 is true
    else:
        # code if none of the conditions is true
"""
# Example:
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")  # Output based on the condition

# 3. Advanced Conditional Statements

# a) Nested if Statements:
"""
Definition:
if statements inside another if statement.

Syntax:
    if condition1:
        if condition2:
            # code if both conditions are true
"""
# Example:
num = 10
if num > 0:
    if num % 2 == 0:
        print("Positive even number.")  # Output if both conditions are true

# b) Ternary Operator (Conditional Expression):
"""
Definition:
Short form of if-else in a single line.

Syntax:
    result = value_if_true if condition else value_if_false
"""
# Example:
age = 20
result = "Eligible" if age >= 18 else "Not Eligible"
print(result)  # Output based on the condition

# c) Multiple Conditions with and, or, not:
"""
Definition:
Used to combine multiple conditions.

and: All conditions must be true.
or: At least one condition must be true.
not: Negates the condition.
"""
# Examples:
# and
age = 20
is_registered = True
if age >= 18 and is_registered:
    print("You can vote.")  # Output if both conditions are true

# or
num = 5
if num < 0 or num > 10:
    print("Out of range.")  # Output if at least one condition is true
else:
    print("Within range.")  # Output if no conditions are true

# not
is_raining = False
if not is_raining:
    print("Go for a walk.")  # Output if the condition is negated

# d) Short-Circuit Evaluation:
"""
Definition:
The evaluation stops as soon as the result is determined.

Syntax:
    if condition1 and condition2:
        # execute only if both are true
"""
# Example:
a = 0
b = 10
if a != 0 and b / a > 2:
    print("This will not raise an error.")  # This will not execute due to short-circuit

# 4. Tasks and Exercises

# Task 1:
"""
Write a program to check if a number is positive, negative, or zero using if-elif-else.
"""
number = int(input("Enter a number: "))
if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")  # Output based on the number

# Task 2:
"""
Write a program to find the maximum of two numbers using an if statement.
"""
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("The maximum number is:", a)
else:
    print("The maximum number is:", b)

# Task 3:
"""
Write a program to check if a person is eligible for a driving license (age >= 18 and must pass a driving test).
"""
age = int(input("Enter your age: "))
has_passed_test = input("Have you passed the driving test? (yes/no): ").lower() == 'yes'
if age >= 18 and has_passed_test:
    print("You are eligible for a driving license.")
else:
    print("You are not eligible for a driving license.")

# Task 4:
"""
Write a grading system:
  - 90-100: A
  - 75-89: B
  - 60-74: C
  - Below 60: Fail
"""
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")

# Task 5:
"""
Use nested if statements to categorize a person's BMI:
  - BMI < 18.5: Underweight
  - 18.5 ≤ BMI < 25: Normal
  - 25 ≤ BMI < 30: Overweight
  - BMI ≥ 30: Obesity
"""
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))
bmi = weight / (height ** 2)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obesity")

# Task 6:
"""
Write a program using the ternary operator to check if a number is even or odd.
"""
number = int(input("Enter a number: "))
result = "Even" if number % 2 == 0 else "Odd"
print(result)

# Task 7:
"""
Write a program to check if a year is a leap year:
  - Leap years are divisible by 4.
  - Centuries must be divisible by 400.
"""
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


# Tasks
# 1. *Check Positive or Negative:*
#    Write a program that checks if a number is positive or negative.

# number = float(input("Enter a number:"))
# 
# if number > 0 :
#     print(f"The number {number} is positive")
# elif number < 0:
#     print(f"The number {number} is negative")
# else:
#     print(f"The number {number} is Zero")

# 2. *Odd or Even:*
#    Write a program to check if a number is odd or even.

# number = int(input("Enter a number:"))
# 
# if number % 2 == 0:
#     print(f"The number {number} is even")
# else:
#     print(f"The number {number} is odd")

# 3. *Grade Calculator:*
#    Take an input of a student's score and print their grade based on the following criteria:
#    - 90-100: A
#    - 80-89: B
#    - 70-79: C
#    - Below 70: Fail

# score = int(input("Enter your score 0-100:"))
# 
# if score > 100 or score < 0:
#     print("Invalid input")
# elif score >= 90 and score < 100:
#     print("Grade: A")
# elif score >= 80 and score < 89:
#     print("Grade: B")
# elif score >= 70 and score < 79:
#     print("Grade: C")
# else:
#     print("Fail")

# 4. *Leap Year:*
#    Write a program to check if a year is a leap year or not.

# year = int(input("Enter a year:"))
# 
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} is a Leap year")
# else:
#     print(f"{year} is not a Leap year")

# 5. *Greater of Two Numbers:*
#    Write a program to find the greater of two numbers.

# num1 = float(input("Enter first number:"))
# num2 = float(input("Enter second number:"))
# 
# if num1 > num2:
#     print(f"{num1} is greater")
# elif num2 > num1:
#     print(f"{num2} is greater")
# else:
#     print("Both numbers are equal")

# 6. *Smallest of Three Numbers:*
#    Write a program to find the smallest of three numbers.

# num1 = float(input("Enter first number:"))
# num2 = float(input("Enter second number:"))
# num3 = float(input("Enter third number:"))
# 
# if (num1 == num2 == num3):
#     print("Three numbers are equal")
# elif (num1 < num2) and (num1 < num3):
#     print(f"{num1} is smallest")
# elif(num2 < num1) and (num2< num3):
#     print(f"{num2} is smallest")
# else:
#     print(f"{num3} is smallest")

# 7. *Voting Eligibility:*
#    Write a program to check if a person is eligible to vote (18 years or older).

# age = int(input("Enter your age:"))
# 
# # if age >= 18 and age <= 100:
# if 100 >= age >= 18:
#     print("You are eligible to vote")
# elif 18 > age > 0:
#     print("You are not eligible to vote")
# else:
#     print("Invalid input")

# 8. *Check Character Case:*
#    Write a program to check if an input character is uppercase, lowercase, or not a letter.

# char = input("Enter a characer:")
# 
# if char.isupper():
#     print(f"{char} is UPPERCASE")
# elif char.islower():
#     print(f"{char} is lowercase")
# else:
#     print(f"{char} is not an alphabet character")

# 9. *Divisibility Check:*
#    Write a program to check if a number is divisible by 3 and 5.

# number = int(input("Enter a number:"))
# 
# if number % 3 == 0 and number % 5 == 0:
#     print(f"{number} is divisible by 3 and 5")
# elif number % 3 == 0:
#     print(f"{number} is divisible by 3")
# elif number % 5 == 0:
#     print(f"{number} is divisible by 5")
# else:
#     print(f"{number} is not divisible by 3 and 5")

# 10. *Temperature Check:*
#     Write a program that prints "Cold" if the temperature is below 20°C, and "Warm" otherwise.

# temp = float(input("Enter the temparature in Celcius:"))
# 
# if temp < 20:
#     print("Cold")
# else:
#     print("Warm")