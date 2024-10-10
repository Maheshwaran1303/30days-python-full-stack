### Inheritance in Python

# Inheritance is one of the core concepts of Object-Oriented Programming (OOP) that allows a class to inherit properties and behaviors (attributes and methods) from another class. The main purpose of inheritance is code reusability and to create a logical relationship between different classes.

# In Python, a class that inherits from another class is called a subclass (child class), and the class being inherited from is called a superclass (parent class).

### Key Concepts of Inheritance:
'''
1. Parent (Base) Class: The class whose properties and methods are inherited by the child class.
2. Child (Derived) Class: The class that inherits properties and methods from the parent class.
3. Overriding: A child class can override (provide a new implementation for) a method inherited from the parent class.
4. Super() Function: Used to call a method from the parent class inside the child class.
'''
### Types of Inheritance:
'''
1. Single Inheritance: A child class inherits from a single parent class.
2. Multiple Inheritance: A child class inherits from more than one parent class.
3. Multilevel Inheritance: A child class inherits from a parent class, and another class inherits from this child class.
4. Hierarchical Inheritance: Multiple child classes inherit from the same parent class.
5. Hybrid Inheritance: A combination of two or more types of inheritance.
'''

### 1. Single Inheritance

# A child class inherits from one parent class.

# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} is making a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print(f"{self.name} is barking.")

# Creating an object of the Dog class
dog = Dog("Buddy")
dog.speak()  # Inherited method from Animal
dog.bark()   # Method from Dog class
'''
Output:
Buddy is making a sound.
Buddy is barking.
'''

### 2. Multiple Inheritance

# A child class inherits from multiple parent classes.

# Parent class 1
class Father:
    def paint(self):
        print("Father is good at painting.")

# Parent class 2
class Mother:
    def cook(self):
        print("Mother is good at cooking.")

# Child class inheriting from both Father and Mother
class Child(Father, Mother):
    def skills(self):
        print("Child is good at coding.")

# Creating an object of the Child class
child = Child()

child.skills()
child.paint()
child.cook()

'''
class Child(Father, Mother):
    def skills(self):
        Father.skills(self)  # Calling Father's skills method
        Mother.skills(self)  # Calling Mother's skills method
        print("Child is good at coding.")

# Creating an object of the Child class
child = Child()
child.skills()  # Accessing methods from both parents
'''

'''
Output:

Father is good at carpentry.
Mother is good at painting.
Child is good at coding.
'''

### 3. Multilevel Inheritance

# A child class inherits from a parent class, and another class inherits from the child class, forming a chain.


# Grandparent class
class Vehicle:
    def start(self):
        print("Vehicle is starting.")

# Parent class inheriting from Vehicle
class Car(Vehicle):
    def drive(self):
        print("Car is driving.")

# Child class inheriting from Car
class SportsCar(Car):
    def race(self):
        print("Sports car is racing.")

# Creating an object of the SportsCar class
sports_car = SportsCar()
sports_car.start()  # Inherited from Vehicle
sports_car.drive()  # Inherited from Car
sports_car.race()   # Method from SportsCar

'''
Output:

Vehicle is starting.
Car is driving.
Sports car is racing.
'''

### 4. Hierarchical Inheritance

# Multiple child classes inherit from a single parent class.

# Parent class
class Animal:
    def eat(self):
        print("Animal is eating.")

# Child class 1
class Dog(Animal):
    def bark(self):
        print("Dog is barking.")

# Child class 2
class Cat(Animal):
    def meow(self):
        print("Cat is meowing.")

# Creating objects of Dog and Cat
dog = Dog()
dog.eat()  # Inherited from Animal
dog.bark()  # Dog's own method

cat = Cat()
cat.eat()  # Inherited from Animal
cat.meow()  # Cat's own method

'''
Output:

Animal is eating.
Dog is barking.
Animal is eating.
Cat is meowing.
'''

### 5. Hybrid Inheritance

# A combination of two or more types of inheritance. For example, combining hierarchical and multiple inheritance.

# Base class
class A:
    def method_A(self):
        print("Method A")

# Class B inheriting from class A
class B(A):
    def method_B(self):
        print("Method B")

# Class C inheriting from class A
class C(A):
    def method_C(self):
        print("Method C")

# Class D inheriting from both B and C
class D(B, C):
    def method_D(self):
        print("Method D")

# Creating an object of class D
obj = D()
obj.method_A()  # Inherited from A
obj.method_B()  # Inherited from B
obj.method_C()  # Inherited from C
obj.method_D()  # Method from class D
'''
Output:

Method A
Method B
Method C
Method D
'''

# Polymorphism in Python
'''
Polymorphism is one of the core concepts in object-oriented programming. It refers to the ability of different objects to respond to the same method call in a way that is appropriate for their type. Polymorphism allows us to define methods in the parent class and override them in the child class, so the child class can have its own behavior when the method is called.
'''
### Method Overriding

# When a child class provides a specific implementation for a method that is already defined in its parent class, this is called method overriding. It allows the child class to provide its own version of the method.


class Animal:
    def speak(self):
        print("Animal is making a sound.")

# Dog class overriding the speak method of Animal
class Dog(Animal):
    def speak(self):
        print("Dog is barking.")

# Creating an object of Dog
dog = Dog()
dog.speak()  # Dog's overridden speak method is called

'''
Output:
Dog is barking.
'''

### The `super()` Function

# The `super()` function allows you to call methods from the parent class inside the child class. This is useful when you want to extend or customize the behavior of inherited methods.

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} is making a sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the parent class constructor
        self.breed = breed

    def speak(self):
        super().speak()  # Call the parent class method
        print(f"{self.name} is a {self.breed} and is barking.")

# Creating an object of Dog
dog = Dog("Buddy", "Golden Retriever")
dog.speak()

'''
Output:

Buddy is making a sound.
Buddy is a Golden Retriever and is barking.
'''

### Summary:
'''
- Inheritance allows one class (child) to inherit attributes and methods from another class (parent).
- Types of inheritance:
  - Single, Multiple, Multilevel, Hierarchical, and Hybrid inheritance.
- Method Overriding allows a child class to redefine a method from the parent class.
- The `super()` function helps in calling methods from the parent class in a child class.

Inheritance promotes code reuse and enables a hierarchical organization of classes, making it easier to extend and maintain your code.
'''