# Class >  Set of variables and functions. It's like a blue print.
# Ex:1
class college:
    def study(self):
        print("Let's Study")
    def play(self):
        print("Let's Play")

murugesh = college()
mahesh = college()

murugesh.study()
mahesh.play()

# Ex:2
class work:
    name = ""
    age = ""
    def bro1(self):
        print("Brother1 Working in Erode")
    def bro2(self):
        print("Brother2 Working in Kerala")

brother1 = work()
brother2 = work()

brother1.name = "Murugesh"
brother2.name = "Mani"

print("1st Brother:", brother1.name)
print("2nd Brother:", brother2.name)
print()

brother1.age = 22
brother2.age = 20

print("1st Brother Age:", brother1.age)
print("2nd Brother Age:", brother2.age)
print()

brother1.bro1()
brother1.bro2()
print()


# Constructor and Self Keyword
# Constructor > A Constructor is a unique function that gets called automatically when an object is created of a class. The main purpose of a constructor is to initialize or assign values  to the data members of that class.

# Ex:1
class laptop:
    def display(self):
        print("Display")

HP = laptop()

HP.display()

# Ex:2
class laptop:
    def __init__(self):  #__init__  => Constructor 
        print("This is Constructor")
    def display(self):
        print("Just display")

hp = laptop()

# Ex:3 
class laptop:
    def __init__(self):
        self.price = ""
        self.processor = ""
        self.ram = ""
    def display(self):
        print(self.price)
        print(self.processor)
        print(self.ram)

hp = laptop()

hp.price = 30000
hp.processor = "i5"
hp.ram = "6GB"

hp.display()

# Ex:4 self > Denote current object.
class laptop:
    def __init__(self):
        self.price = ""
        self.processor = ""
        self.ram = ""
    def display(self):
        print(self.price)
        print(self.processor)
        print(self.ram)

hp=laptop()
dell=laptop()

hp.price=30000
hp.processor="i5"
hp.ram="6GB"

dell.price=50000
dell.processor="i7"
dell.ram="8GB"

hp.display()
print()
dell.display()


# The self Parameter >
# It is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:

# Example
# Use the words myobject and abc instead of self:

class Person:
  def __init__(myobject, name, age):
    myobject.name = name
    myobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("Mahesh", 25)
p1.myfunc()

# Ex:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Mahesh", 24)

print(p1.name)
print(p1.age)

# The __str__() Function:
# It controls what should be returned when the class object is represented as a string. If the __str__() function is not set, the string representation of the object is returned:

# Ex:1 The string representation of an object WITHOUT the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Mahesh", 24)

print(p1) #output <__main__.Person object at 0x000001D71B032290>

# Ex:2 The string representation of an object WITH the __str__() function:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"I am {self.name}. My age is {self.age})"

p1 = Person("Mahesh", 25)
print(p1)


# Modify Object Properties
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Mahesh", 15)

p1.age = 25

print(p1.age)

# Delete Object Properties:
# You can delete properties on objects by using the "del" keyword:
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("Mahesh", 25)

# del p1.age

print(p1.age)


# The pass Statement:
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Person:
  pass

# having an empty class definition like this, would raise an error without the pass statement


# Tasks
'''

Task 1:
 Create a class named `Student` with a constructor to initialize `name` and `register_number`. Implement a method `display()` to print the student's name and register number.

Task 2:
 Create a class named `Fruit`. Use the `__init__()` method to initialize the `color` variable. Create an object `apple` and pass the color as a parameter through the object.

Task 3:
 Create a class named `Teacher` with a constructor to initialize `name` and `register_number`. Implement a method `solve()` to display the teacher's name and register number. Create two objects `t1` and `t2`, passing the name and register number through the object.

Task 4:
 Create a class named `Calculator`. Define variables `a` and `b`. Implement methods `add()`, `sub()`, `mul()`, and `div()`, where each method performs the respective operation using `a` and `b` as parameters. 

Task 5:
 Create a class named `MyClass` with a class variable `x` set to 10. Create an object `p1` of `MyClass` and print the value of `x`.

Task 6:
 Create a class named `Person`. Use the `__init__()` method to assign values for `name` and `age`. Create an object `p1` and initialize it with your name and age. Print the values of `name` and `age`.

Task 7:
 Modify the `Person` class to include the `__str__()` method that returns the string representation of the object in the format `name(age)`. Create an object `p1` and print it to see the result.

Task 8:
 Create a class named `Person` with the `__init__()` method to initialize `name` and `age`. Rename `self` to `myobject` in the constructor and use `abc` in the method. Implement a method `myfunc()` that prints "Hello, my name is `name`". Create an object `p1` and call the method.

Task 9:
 Modify the `Person` class to include a method that modifies the `age` property. Create an object `p1`, change the `age` property, and print the new value.

Task 10:
 Create a class named `Person` and use the `del` keyword to delete the `age` property. Create an object `p1`, delete its `age` property, and handle the case when you try to print the deleted property.

Task 11:
 Create a class named `EmptyClass` with no methods or properties. Use the `pass` statement in the class definition to avoid errors. 

'''



# Task Solutions

# Task 1: Create a class named Student with name and register_number
class Student:
    def __init__(self, name, register_number):
        self.name = name
        self.register_number = register_number

    def display(self):
        print(f"Name: {self.name}")
        print(f"Register Number: {self.register_number}")

# Creating objects and displaying information
student1 = Student("Alice", "S001")
student2 = Student("Bob", "S002")

student1.display()
student2.display()
print()

# Task 2: Create a class named Fruit with color
class Fruit:
    def __init__(self, color):
        self.color = color

# Creating an object and passing the color parameter
apple = Fruit("Red")
print(f"Apple Color: {apple.color}")
print()

# Task 3: Create a class named Teacher with name and register_number
class Teacher:
    def __init__(self, name, register_number):
        self.name = name
        self.register_number = register_number

    def solve(self):
        print(f"Name: {self.name}")
        print(f"Register Number: {self.register_number}")

# Creating objects and passing the name and register_number
t1 = Teacher("Mr. Smith", "T001")
t2 = Teacher("Ms. Johnson", "T002")

t1.solve()
t2.solve()
print()

# Task 4: Create a class named Calculator with add, sub, mul, div methods
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Cannot divide by zero"

# Creating objects and performing calculations
calc = Calculator(10, 5)

print(f"Addition: {calc.add()}")
print(f"Subtraction: {calc.sub()}")
print(f"Multiplication: {calc.mul()}")
print(f"Division: {calc.div()}")
print()

# Task 5: Create a class named MyClass with a variable x
class MyClass:
    x = 10

p1 = MyClass()
print(f"Value of x: {p1.x}")
print()

# Task 6: Create a class named Person with __init__() to assign name and age
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Mahesh", 24)
print(f"Name: {p1.name}")
print(f"Age: {p1.age}")
print()

# Task 7: Modify the Person class to include __str__() method
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("Mahesh", 24)
print(p1)
print()

# Task 8: Use different names instead of self
class Person:
    def __init__(myobject, name, age):
        myobject.name = name
        myobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("Mahesh", 24)
p1.myfunc()
print()

# Task 9: Modify the Person class to change age property
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.age = 40  # Changing the age property
print(f"New Age: {p1.age}")
print()

# Task 10: Delete the age property from the Person class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
del p1.age  # Deleting the age property

# Handling the case when trying to print the deleted property
try:
    print(p1.age)
except AttributeError:
    print("Age property has been deleted")
print()

# Task 11: Create an empty class using pass statement
class EmptyClass:
    pass

# Creating an object of the empty class
empty_obj = EmptyClass()
print("EmptyClass object created successfully")


'''

 Task 1: Create a Class `Book`
Create a class called `Book` with the following attributes and methods:
- Attributes: `title`, `author`, `price`
- Methods: `display_details()` which prints the details of the book

Create three objects of this class with different values and call the `display_details()` method for each object.

 Task 2: Create a Class `Car`
Create a class called `Car` with the following attributes and methods:
- Attributes: `make`, `model`, `year`, `price`
- Methods: `display_info()` which prints the information of the car

Create two objects of this class with different values and call the `display_info()` method for each object.

 Task 3: Create a Class `Student`
Create a class called `Student` with the following attributes and methods:
- Attributes: `name`, `age`, `grade`
- Methods: `display_student_info()` which prints the information of the student

Create three objects of this class with different values and call the `display_student_info()` method for each object.

 Task 4: Implement a Constructor
Modify the `Book` class to include a constructor that initializes the attributes `title`, `author`, and `price` when an object is created.

 Task 5: Modify the `Car` Class to Include a Constructor
Modify the `Car` class to include a constructor that initializes the attributes `make`, `model`, `year`, and `price` when an object is created.

 Task 6: Modify the `Student` Class to Include a Constructor
Modify the `Student` class to include a constructor that initializes the attributes `name`, `age`, and `grade` when an object is created.

 Task 7: Create a Class `Employee`
Create a class called `Employee` with the following attributes and methods:
- Attributes: `name`, `id`, `department`, `salary`
- Methods: `display_employee_info()` which prints the information of the employee

Create three objects of this class with different values, initialize them using a constructor, and call the `display_employee_info()` method for each object.

 Task 8: Create a Class `Library`
Create a class called `Library` with the following attributes and methods:
- Attributes: `name`, `location`, `books` (a list of `Book` objects)
- Methods: `add_book(book)`, `display_books()`

Create a few `Book` objects and add them to the `Library` object. Call the `display_books()` method to show all books in the library.

 Task 9: Create a Class `BankAccount`
Create a class called `BankAccount` with the following attributes and methods:
- Attributes: `account_number`, `holder_name`, `balance`
- Methods: `deposit(amount)`, `withdraw(amount)`, `display_balance()`

Create an object of this class, perform some deposit and withdrawal operations, and call the `display_balance()` method to show the current balance.

 Task 10: Create a Class `Restaurant`
Create a class called `Restaurant` with the following attributes and methods:
- Attributes: `name`, `cuisine_type`, `rating`
- Methods: `describe_restaurant()`, `open_restaurant()`

Create two objects of this class with different values and call the `describe_restaurant()` and `open_restaurant()` methods for each object.

 Task 11: Create a Class `Person` with Nested Classes
Create a class called `Person` with the following attributes and methods:
- Attributes: `name`, `age`, `address` (a nested class with attributes `street`, `city`, `zip_code`)
- Methods: `display_person_info()`

Create an object of this class, initialize the nested class attributes, and call the `display_person_info()` method to show the person's details.

 Task 12: Create a Class `Mobile`
Create a class called `Mobile` with the following attributes and methods:
- Attributes: `brand`, `model`, `price`
- Methods: `show_mobile_info()`

Create three objects of this class with different values, initialize them using a constructor, and call the `show_mobile_info()` method for each object.

'''


# Solutions

# Task 1: Create a Class `Book`
# Create a class called `Book` with the following attributes and methods:
# - Attributes: `title`, `author`, `price`
# - Methods: `display_details()` which prints the details of the book

# Solution:
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

book1 = Book("Python Programming", "John Doe", 29.99)
book2 = Book("Learning Django", "Jane Smith", 35.00)
book3 = Book("Data Science with Python", "Jim Brown", 45.00)

book1.display_details()
book2.display_details()
book3.display_details()

print()

# Task 2: Create a Class `Car`
# Create a class called `Car` with the following attributes and methods:
# - Attributes: `make`, `model`, `year`, `price`
# - Methods: `display_info()` which prints the information of the car

# Solution:
class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: {self.price}")

car1 = Car("Toyota", "Corolla", 2020, 20000)
car2 = Car("Honda", "Civic", 2019, 22000)

car1.display_info()
car2.display_info()

print()

# Task 3: Create a Class `Student`
# Create a class called `Student` with the following attributes and methods:
# - Attributes: `name`, `age`, `grade`
# - Methods: `display_student_info()` which prints the information of the student

# Solution:
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_student_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")

student1 = Student("Alice", 20, "A")
student2 = Student("Bob", 22, "B")
student3 = Student("Charlie", 21, "A+")

student1.display_student_info()
student2.display_student_info()
student3.display_student_info()

print()

# Task 4: Implement a Constructor for `Book`
# Modify the `Book` class to include a constructor that initializes the attributes `title`, `author`, and `price` when an object is created.

# Solution: (Already done in Task 1)

# Task 5: Modify the `Car` Class to Include a Constructor
# Modify the `Car` class to include a constructor that initializes the attributes `make`, `model`, `year`, and `price` when an object is created.

# Solution: (Already done in Task 2)

# Task 6: Modify the `Student` Class to Include a Constructor
# Modify the `Student` class to include a constructor that initializes the attributes `name`, `age`, and `grade` when an object is created.

# Solution: (Already done in Task 3)

# Task 7: Create a Class `Employee`
# Create a class called `Employee` with the following attributes and methods:
# - Attributes: `name`, `id`, `department`, `salary`
# - Methods: `display_employee_info()` which prints the information of the employee

# Solution:
class Employee:
    def __init__(self, name, id, department, salary):
        self.name = name
        self.id = id
        self.department = department
        self.salary = salary

    def display_employee_info(self):
        print(f"Name: {self.name}, ID: {self.id}, Department: {self.department}, Salary: {self.salary}")

employee1 = Employee("Dave", 101, "Engineering", 70000)
employee2 = Employee("Eve", 102, "Marketing", 65000)
employee3 = Employee("Frank", 103, "HR", 60000)

employee1.display_employee_info()
employee2.display_employee_info()
employee3.display_employee_info()

print()

# Task 8: Create a Class `Library`
# Create a class called `Library` with the following attributes and methods:
# - Attributes: `name`, `location`, `books` (a list of `Book` objects)
# - Methods: `add_book(book)`, `display_books()`

# Solution:
class Library:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(f"Library: {self.name}, Location: {self.location}")
        for book in self.books:
            book.display_details()

library = Library("City Library", "Downtown")

book1 = Book("Python Programming", "John Doe", 29.99)
book2 = Book("Learning Django", "Jane Smith", 35.00)
book3 = Book("Data Science with Python", "Jim Brown", 45.00)

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

library.display_books()

print()

# Task 9: Create a Class `BankAccount`
# Create a class called `BankAccount` with the following attributes and methods:
# - Attributes: `account_number`, `holder_name`, `balance`
# - Methods: `deposit(amount)`, `withdraw(amount)`, `display_balance()`

# Solution:
class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}, New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New Balance: {self.balance}")

    def display_balance(self):
        print(f"Account Number: {self.account_number}, Holder Name: {self.holder_name}, Balance: {self.balance}")

account = BankAccount(123456, "Alice")
account.display_balance()
account.deposit(500)
account.withdraw(200)
account.display_balance()

print()

# Task 10: Create a Class `Restaurant`
# Create a class called `Restaurant` with the following attributes and methods:
# - Attributes: `name`, `cuisine_type`, `rating`
# - Methods: `describe_restaurant()`, `open_restaurant()`

# Solution:
class Restaurant:
    def __init__(self, name, cuisine_type, rating):
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"Restaurant: {self.name}, Cuisine Type: {self.cuisine_type}, Rating: {self.rating}")

    def open_restaurant(self):
        print(f"{self.name} is now open!")

restaurant1 = Restaurant("The Food Place", "Italian", 4.5)
restaurant2 = Restaurant("Spicy Delights", "Indian", 4.7)

restaurant1.describe_restaurant()
restaurant1.open_restaurant()

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

print()

# Task 11: Create a Class `Person` with Nested Classes
# Create a class called `Person` with the following attributes and methods:
# - Attributes: `name`, `age`, `address` (a nested class with attributes `street`, `city`, `zip_code`)
# - Methods: `display_person_info()`

# Solution:
class Person:
    class Address:
        def __init__(self, street, city, zip_code):
            self.street = street
            self.city = city
            self.zip_code = zip_code

    def __init__(self, name, age, street, city, zip_code):
        self.name = name
        self.age = age
        self.address = self.Address(street, city, zip_code)

    def display_person_info(self):
        print(f"Name: {self.name}, Age: {self.age}")
        print(f"Address: {self.address.street}, {self.address.city}, {self.address.zip_code}")

person = Person("Charlie", 30, "123 Main St", "Springfield", "12345")
person.display_person_info()

print()

# Task 12: Create a Class `Mobile`
# Create a class called `Mobile` with the following attributes and methods:
# - Attributes: `brand`, `model`, `price`
# - Methods: `show_mobile_info()`

# Solution:
class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def show_mobile_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Price: {self.price}")

mobile1 = Mobile("Samsung", "Galaxy S21", 799)
mobile2 = Mobile("Apple", "iPhone 13", 999)
mobile3 = Mobile("OnePlus", "9 Pro", 969)

mobile1.show_mobile_info()
mobile2.show_mobile_info()
mobile3.show_mobile_info()
