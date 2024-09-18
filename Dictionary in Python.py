## *Structure for Python Dictionaries*

### *1. Introduction to Dictionaries*
# Definition: A dictionary is an unordered, mutable collection of key-value pairs, where each key is unique.
# Syntax: 
my_dict = {key1: value1, key2: value2}

# Keys must be immutable (e.g., strings, numbers, tuples), while values can be of any data type.
# Example:
my_dict = {"name": "John", "age": 25, "city": "New York"}


---

### *2. Creating and Accessing Dictionaries*

#### a) *Creating a Dictionary*
# Example:
my_dict = {"name": "Alice", "age": 30, "profession": "Engineer"}


#### b) *Accessing Values by Key*
# Use the key to access a value.
# Example:
print(my_dict["name"])  # Outputs: Alice
print(my_dict.get("age"))  # Outputs: 30


---

### *3. Modifying Dictionaries*

#### a) *Adding or Updating Items*
# Example:
my_dict = {"name": "Alice", "age": 30}
my_dict["city"] = "London"  # Adding a new key-value pair
my_dict["age"] = 35  # Updating an existing key's value
print(my_dict)  # Outputs: {'name': 'Alice', 'age': 35, 'city': 'London'}


#### b) *Removing Items*
# pop(): Removes an item by its key and returns its value.
# del: Deletes an item by its key.
# clear(): Removes all items from the dictionary.
# Example:
my_dict = {"name": "Alice", "age": 30, "city": "London"}
my_dict.pop("city")
print(my_dict)  # Outputs: {'name': 'Alice', 'age': 30}

del my_dict["age"]
print(my_dict)  # Outputs: {'name': 'Alice'}

my_dict.clear()
print(my_dict)  # Outputs: {}


---

### *4. Dictionary Methods*

#### a) *Common Dictionary Methods*
# keys(): Returns a view object containing the dictionary's keys.
# values(): Returns a view object containing the dictionary's values.
# items(): Returns a view object containing the dictionary's key-value pairs.
# Example:
my_dict = {"name": "Alice", "age": 30}
print(my_dict.keys())  # Outputs: dict_keys(['name', 'age'])
print(my_dict.values())  # Outputs: dict_values(['Alice', 30])
print(my_dict.items())  # Outputs: dict_items([('name', 'Alice'), ('age', 30)])


#### b) *Copying a Dictionary*
# copy(): Returns a shallow copy of the dictionary.
# Example:
my_dict = {"name": "Alice", "age": 30}
new_dict = my_dict.copy()
print(new_dict)  # Outputs: {'name': 'Alice', 'age': 30}


---

### *5. Looping Through a Dictionary*

#### a) *Looping Through Keys*
# Example:
my_dict = {"name": "Alice", "age": 30}
for key in my_dict:
    print(key)


#### b) *Looping Through Values*
# Example:
for value in my_dict.values():
    print(value)


#### c) *Looping Through Key-Value Pairs*
# Example:
for key, value in my_dict.items():
    print(f"{key}: {value}")


---

### *6. Nested Dictionaries*

#### a) *Creating a Nested Dictionary*
# A dictionary can contain another dictionary as its value.
# Example:
nested_dict = {
    "person1": {"name": "John", "age": 25},
    "person2": {"name": "Alice", "age": 30}
}


#### b) *Accessing Nested Dictionary Elements*
# Example:
print(nested_dict["person1"]["name"])  # Outputs: John


---

### *7. Dictionary Comprehension*

#### a) *Basic Dictionary Comprehension*
# Syntax: {key: value for element in iterable}
# Example:
squares = {x: x**2 for x in range(5)}
print(squares)  # Outputs: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


#### b) *Conditional Dictionary Comprehension*
# Example:
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Outputs: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


---

### *8. Tasks and Exercises*

# Task 1: Create a dictionary that stores the names and ages of three people. 
# Add a new person's age to the dictionary and update one person's age.
people = {"Alice": 30, "Bob": 25, "Charlie": 35}
people["Diana"] = 28  # Adding a new person
people["Alice"] = 31  # Updating Alice's age
print(people)  # Outputs: {'Alice': 31, 'Bob': 25, 'Charlie': 35, 'Diana': 28}

# Task 2: Write a Python program to iterate through a dictionary and print all keys and values.
for key, value in people.items():
    print(f"Key: {key}, Value: {value}")

# Task 3: Write a Python function that takes a dictionary and returns a list of all the values.
def get_values(dictionary):
    return list(dictionary.values())

print(get_values(people))  # Outputs: [31, 25, 35, 28]

# Task 4: Create a nested dictionary that stores information about multiple people (name, age, and profession), 
# and write a function to retrieve the information about a specific person.
people_info = {
    "person1": {"name": "John", "age": 25, "profession": "Artist"},
    "person2": {"name": "Alice", "age": 30, "profession": "Engineer"}
}

def get_person_info(person_id):
    return people_info.get(person_id, "Person not found")

print(get_person_info("person1"))  # Outputs: {'name': 'John', 'age': 25, 'profession': 'Artist'}

# Task 5: Write a Python program to merge two dictionaries into one.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
merged_dict = {**dict1, **dict2}
print(merged_dict)  # Outputs: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Task 6: Write a Python program to count the number of times a word appears in a string using a dictionary.
sentence = "this is a test this is only a test"
word_count = {}
for word in sentence.split():
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)  # Outputs: {'this': 2, 'is': 2, 'a': 2, 'test': 2, 'only': 1}

# Task 7: Use dictionary comprehension to create a dictionary where the keys are numbers from 1 to 5 
# and the values are the cubes of the keys.
cubes = {x: x**3 for x in range(1, 6)}
print(cubes)  # Outputs: {1: 1, 2: 8, 3: 27, 4: 64, 5: 125}
