### Abstraction in Python 
# Abstraction means hiding the unnecessary details

from abc import ABC, abstractmethod
class car(ABC):
    def start(self):
        pass
    def stop(self):
        pass
    @abstractmethod
    def accelerate(self):
        pass
    @abstractmethod
    def brake(self):
        pass

class TATA(car):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
    def accelerate(self):
        print("Speed up 120kmph")
    def brake(self):
        print("Speed down fastly")

class Maruti(car):
    def start(self):
        print("Car started")
    def stop(self):
        print("Car stopped")
    def accelerate(self):
        print("Speed up 130kmph")
    def brake(self):
        print("Speed down slowly")

car1 = TATA()
car1.start()
car1.stop()
car1.accelerate()
car1.brake()

car2 = Maruti()
car2.start()
car2.stop()
car2.accelerate()
car2.brake()

'''
Abstraction is another fundamental concept in object-oriented programming (OOP). It refers to hiding the complex implementation details and showing only the necessary functionality to the user. It allows the user to interact with an object or system without needing to understand the intricate workings behind it.

In simpler terms, abstraction helps us to focus on what an object does instead of how it does it. It provides a simplified interface while keeping the complex background processes hidden.

'''

### Why is Abstraction Important?
'''
1. Simplification: Users don’t need to know the internal workings of a system or class. They just need to know how to interact with it.
2. Reduced Complexity: By hiding complex details, abstraction reduces the complexity of the system.
3. Code Reusability: Abstraction helps to organize code by focusing on behavior that can be reused across multiple parts of a program.
4. Improved Maintenance: By hiding the implementation details, future changes to the internal workings won't affect the rest of the system.
'''


### Abstraction Example in Real Life
'''
Think of driving a car. You don't need to know how the engine works, how the fuel ignites, or how the gears function internally. All you care about is that pressing the accelerator makes the car go faster, and pressing the brake slows it down. The complex engine mechanisms are abstracted away, and you only interact with the necessary controls.
'''


### Abstraction in Python

# Python supports abstraction using abstract classes and abstract methods.
'''
1. Abstract Class: An abstract class is a class that cannot be instantiated directly. It can have abstract methods, which are methods declared but contain no implementation (just a signature).
2. Abstract Method: An abstract method is a method that is declared in the abstract class but doesn't have a body. It must be implemented by any subclass that inherits from the abstract class.

Python provides the `abc` module to create abstract classes and methods. The `@abstractmethod` decorator is used to define an abstract method.
'''

### Example of Abstraction
'''
Let's create an abstract class `Vehicle` that defines abstract methods, and then we’ll create concrete subclasses that implement these methods.
'''

from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    # Abstract method (must be implemented by subclasses)
    @abstractmethod
    def start_engine(self):
        pass

    # Abstract method
    @abstractmethod
    def stop_engine(self):
        pass

# Concrete class inheriting from Vehicle
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")

    def stop_engine(self):
        print("Car engine stopped")

# Concrete class inheriting from Vehicle
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Motorcycle engine started")

    def stop_engine(self):
        print("Motorcycle engine stopped")

# Now let's create instances and use them
car = Car()
car.start_engine()  # Output: Car engine started
car.stop_engine()   # Output: Car engine stopped

motorcycle = Motorcycle()
motorcycle.start_engine()  # Output: Motorcycle engine started
motorcycle.stop_engine()   # Output: Motorcycle engine stopped

### Explanation:
'''
1. Abstract Class (`Vehicle`): The `Vehicle` class is abstract, meaning it defines a blueprint for what a vehicle should do, like starting and stopping an engine. However, it does not implement how the engine starts or stops.
   
2. Abstract Methods (`start_engine` and `stop_engine`): These methods are abstract, meaning that the `Vehicle` class only declares that vehicles should have these methods, but it doesn’t define the actual behavior.

3. Concrete Classes (`Car` and `Motorcycle`): These classes inherit from the `Vehicle` class and implement the abstract methods. Each subclass provides its own implementation of starting and stopping the engine.

4. Instantiation: You cannot create an object of the abstract class `Vehicle`, but you can create objects of the concrete classes `Car` and `Motorcycle`, which provide the actual implementations of the abstract methods.
'''


### Key Points About Abstraction:
'''
1. Abstract Class: It cannot be instantiated and is meant to be inherited. It defines common behavior that can be shared across multiple subclasses.
   
2. Abstract Method: Declares a method without implementation. Subclasses are responsible for providing the concrete implementation.

3. Concrete Class: A subclass that provides an implementation for all abstract methods defined in its abstract parent class.

4. Separation of Concerns: Abstraction helps in separating what something does (interface) from how it does it (implementation).
'''

### Full Example with More Details

from abc import ABC, abstractmethod

# Abstract base class
class Appliance(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Concrete class for a Fan
class Fan(Appliance):
    def turn_on(self):
        print("Fan is turned on")

    def turn_off(self):
        print("Fan is turned off")

# Concrete class for a Light
class Light(Appliance):
    def turn_on(self):
        print("Light is turned on")

    def turn_off(self):
        print("Light is turned off")

# Creating objects of concrete classes
fan = Fan()
light = Light()

# Interacting with the objects
fan.turn_on()    # Output: Fan is turned on
fan.turn_off()   # Output: Fan is turned off

light.turn_on()  # Output: Light is turned on
light.turn_off() # Output: Light is turned off

'''
In this example:
- We have an abstract class `Appliance` with two abstract methods `turn_on` and `turn_off`.
- The `Fan` and `Light` classes implement these abstract methods with their own specific behavior.

### Benefits of Abstraction:
- Hides Complexity: The user doesn't need to know how the class works internally, just how to use it.
- Promotes Reusability: You can create different classes (like `Fan`, `Light`, etc.) based on a shared abstract interface (`Appliance`).
- Flexibility: You can easily add new classes (like `Heater` or `AirConditioner`) that adhere to the same interface.
'''


### Conclusion:
'''
- Abstraction allows you to focus on what the object does without worrying about how it does it.
- Python achieves abstraction using abstract classes and abstract methods from the `abc` module.
- By forcing subclasses to implement abstract methods, you can ensure that all objects of that type will behave in a consistent way, making your code more maintainable and flexible.
'''