# Polymorphism is one of the core concepts in object-oriented programming. It refers to the ability of different objects to respond to the same method call in a way that is appropriate for their type. Polymorphism allows us to define methods in the parent class and override them in the child class, so the child class can have its own behavior when the method is called.

'''
There are two types of polymorphism in Python:
1. Compile-time Polymorphism (Method Overloading) – Python doesn’t directly support method overloading (multiple methods with the same name in the same class), but we can simulate this by using default arguments or variable-length argument lists.
2. Run-time Polymorphism (Method Overriding) – This occurs when a method in a child class has the same name as a method in the parent class. The method of the object being called will be executed.
'''

### Example: Polymorphism in Python (Method Overriding)


# Parent class: Shape
class Shape:
    def area(self):
        print("Calculating area of shape")

    def perimeter(self):
        print("Calculating perimeter of shape")


# Child class: Circle (Polymorphism via Method Overriding)
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        # Overriding the parent class method
        print(f"Area of circle: {3.1416 * self.radius  **2}")
    
    def perimeter(self):
        # Overriding the parent class method
        print(f"Circumference of circle: {2 * 3.1416 * self.radius}")


# Child class: Rectangle (Polymorphism via Method Overriding)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        # Overriding the parent class method
        print(f"Area of rectangle: {self.length * self.width}")
    
    def perimeter(self):
        # Overriding the parent class method
        print(f"Perimeter of rectangle: {2 * (self.length + self.width)}")


# Polymorphism in action
def calculate_shape_properties(shape):
    shape.area()  # Polymorphic call
    shape.perimeter()  # Polymorphic call


# Create instances of different shapes
circle = Circle(5)
rectangle = Rectangle(4, 6)

# Pass the different objects to the same function
print("Circle properties:")
calculate_shape_properties(circle)

print("\nRectangle properties:")
calculate_shape_properties(rectangle)


### Explanation:
'''
- Parent class `Shape`: Defines two methods, `area()` and `perimeter()`, which are meant to be overridden by child classes.
- Child class `Circle`: Overrides the `area()` and `perimeter()` methods of the `Shape` class to calculate the area and perimeter (circumference) of a circle.
- Child class `Rectangle`: Similarly, this class overrides the `area()` and `perimeter()` methods to calculate these properties for a rectangle.
- The `calculate_shape_properties()` function demonstrates run-time polymorphism by calling the `area()` and `perimeter()` methods of whichever object (shape) it receives as an argument. The actual method executed depends on whether the object is a `Circle` or `Rectangle`.
'''
### Output:
'''
Circle properties:
Area of circle: 78.53999999999999
Circumference of circle: 31.416

Rectangle properties:
Area of rectangle: 24
Perimeter of rectangle: 20
'''

### Polymorphism with Built-in Functions:
'''
Polymorphism can also be seen with built-in Python functions that operate on different types of data in a consistent manner. For example:
'''

# Polymorphism with the len() function
print(len("Mahesh"))   # len() works with strings
print(len([1, 2, 3, 4]))  # len() works with lists
print(len({"name": "Mahesh", "age": 25}))  # len() works with dictionaries
'''
Output:

6
4
2
'''

# This shows how the same function, `len()`, can operate on different data types and return appropriate results.

### Key Points of Polymorphism:
'''
- Method Overriding is a primary example of polymorphism in Python.
- You can use the same method on objects of different types, and they will behave differently based on their class.
- Polymorphism increases flexibility and reusability in object-oriented programming, as functions can handle objects of different types with uniformity.
'''

### Conclusion:
'''
Polymorphism allows methods to be used in different ways, depending on the object that invokes them. This flexibility is a key benefit of object-oriented programming, making the code more maintainable and easier to extend.
'''












# ### Method Overriding in Python

# Method overriding occurs when a child class (subclass) defines a method with the same name as a method in its parent class (superclass). The method in the child class overrides the method in the parent class, allowing the child class to provide its own implementation.

# Here's a simple example to demonstrate method overriding:

# ### Example: Method Overriding

# python
# # Parent class: Animal
# class Animal:
#     def sound(self):
#         print("This is a generic animal sound")

# # Child class: Dog (inherits from Animal)
# class Dog(Animal):
#     def sound(self):
#         # Overriding the parent class method
#         print("Bark")

# # Child class: Cat (inherits from Animal)
# class Cat(Animal):
#     def sound(self):
#         # Overriding the parent class method
#         print("Meow")

# # Creating instances of each class
# generic_animal = Animal()
# dog = Dog()
# cat = Cat()

# # Calling the sound method on each instance
# print("Generic Animal Sound:")
# generic_animal.sound()  # Calls the parent class method

# print("\nDog Sound:")
# dog.sound()  # Calls the overridden method in the Dog class

# print("\nCat Sound:")
# cat.sound()  # Calls the overridden method in the Cat class


# ### Explanation:
# - Parent class `Animal`: Defines a `sound()` method that prints a generic animal sound.
# - Child class `Dog`: Overrides the `sound()` method to print "Bark".
# - Child class `Cat`: Overrides the `sound()` method to print "Meow".
# - When the `sound()` method is called on objects of the `Dog` and `Cat` classes, their respective implementations are executed, demonstrating method overriding.

# ### Output:

# Generic Animal Sound:
# This is a generic animal sound

# Dog Sound:
# Bark

# Cat Sound:
# Meow


# ### Key Points:
# - The `sound()` method is defined in the `Animal` class, but it's overridden in both the `Dog` and `Cat` classes to provide specific behavior.
# - Method overriding allows different classes to implement methods with the same name, providing class-specific functionality.
