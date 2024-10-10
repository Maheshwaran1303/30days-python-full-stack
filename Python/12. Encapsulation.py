# Encapsulation:

'''
# It refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, typically a class, and restricting access to some of the object's components.
# In Python, encapsulation is achieved using access modifiers for attributes and methods. The primary access modifiers in Python are:
'''

'''
1. Public: Attributes and methods that are accessible from outside the class.

2. Protected: Attributes and methods that should not be accessed directly from outside the class, but can be accessed in subclasses. In Python, these are indicated by a single underscore prefix (e.g., _protected_attr).

3. Private: Attributes and methods that cannot be accessed from outside the class. These are indicated   by a double underscore prefix (e.g., __private_attr).
'''

# Public
# Ex:1 

class MyClass: 
    def __init__(self):
      self.public_var = "I am public" 
      
obj = MyClass() 
print(obj.public_var)

# Ex:2
class company:
    def __init__(self):
        self.company_name = "VTS"
        
c1 = company()
print(c1.company_name)


# Private
# Ex:3
class Myclass:
    def __init__(self):
        self.__private_var = "I am private"
        
obj = Myclass()
print(obj.__private_var)    # This will raise an AttributeError

# Ex: 4 
class company:
    def __init__(self):
        self.__company_name = "VTS"

c1 = company()
print(c1.__company_name)    # This will raise an AttributeError

# Ex:5
class MyClass:
    def __init__(self):
        self.__private_var = "I am private"

    def get_private_var(self):
        print(self.__private_var)

obj = MyClass()
obj.get_private_var()  
print(obj.__private_var)  # This will raise an AttributeError

# Ex:6
class company:
    def __init__(self):
        self.__company_name = "VTS"
    def get_company_name(self):
        print(self.__company_name)

c1 = company()
c1.get_company_name()
print(c1.__company_name)    # This will raise an AttributeError

# Protect
# Ex:7
class MyClass:
    def __init__(self):
        self._protected_variable = "I am protected"

obj = MyClass()
print(obj._protected_variable)

# ex: 8
class MyClass:
  def __init__(self):
    self._protected_var = "I am protected" 

class ChildClass(MyClass):
  pass

child = ChildClass()
print(child._protected_var)

# Ex:9
class MyClass:
    def __init__(self):
        self._company_name = "I am protected"

obj = MyClass()
print(obj._company_name)

# Ex: 10
class company:
    def __init__(self):
        self._company_name = "VTS"

class academy(company):
    pass
        
vetri = academy()
print(vetri._company_name)


