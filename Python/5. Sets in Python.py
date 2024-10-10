# Structure for Python Sets

"""
1. Introduction to Sets
- Definition: A set is an unordered, mutable collection of unique elements.
  Duplicate elements are automatically removed.
- Syntax: my_set = {element1, element2, element3}
"""

# Example
my_set = {1, 2, 3, 4}
print(my_set)  # Outputs: {1, 2, 3, 4}

# a) Creating an Empty Set
# Note: Use set() to create an empty set, not {}, which creates an empty dictionary.

# Example
empty_set = set()
print(empty_set)  # Outputs: set()

# -------------------------------------

"""
2. Accessing Set Elements
- Sets do not support indexing or slicing because they are unordered.
- You can loop through the elements in a set.
"""

# Example
my_set = {1, 2, 3, 4}
for item in my_set:
    print(item)

# -------------------------------------

"""
3. Adding and Removing Elements in Sets
a) Adding Elements
- Method: add()
"""

# Example
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Outputs: {1, 2, 3, 4}

"""
b) Removing Elements
- Methods: remove() or discard().
- remove() raises an error if the element doesn't exist
-discard() doesn't raise an error if the element doesn't exist
"""

# Example
my_set.remove(2)
my_set.discard(5)  # No error if element doesn't exist

"""
c) Using pop() to Remove and Return an Arbitrary Element
"""

# Example
my_set = {1, 2, 3, 4}
my_set.pop()  # Removes and returns an arbitrary element
print(my_set)  # Outputs remaining elements

# -------------------------------------

"""
4. Set Operations
a) Union of Sets
- Combines all elements from both sets (no duplicates).
"""

# Example
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Outputs: {1, 2, 3, 4, 5}

"""
b) Intersection of Sets
- Returns elements common to both sets.
"""

# Example
intersection_set = set1.intersection(set2)
print(intersection_set)  # Outputs: {3}

"""
c) Difference of Sets
- Returns elements in set1 but not in set2.
"""

# Example
difference_set = set1.difference(set2)
print(difference_set)  # Outputs: {1, 2}

"""
d) Symmetric Difference of Sets (Elements in set1 or set2 but not in both)
- Returns elements in either set1 or set2 but not both.
"""

# Example
symmetric_diff_set = set1.symmetric_difference(set2)
print(symmetric_diff_set)  # Outputs: {1, 2, 4, 5}

# -------------------------------------

"""
5. Set Comparisons
a) Subset: set1.issubset(set2) -> Returns True if all elements of set1 are in set2.
"""

# Example
set1 = {1, 2}
set2 = {1, 2, 3, 4}
print(set1.issubset(set2))  # Outputs: True

"""
b) Superset: set1.issuperset(set2) -> Returns True if set1 contains all elements of set2.
"""

# Example
print(set2.issuperset(set1))  # Outputs: True

"""
c) Disjoint Sets: set1.isdisjoint(set2) -> Returns True if set1 and set2 have no common elements.
"""

# Example
set3 = {5, 6}
print(set1.isdisjoint(set3))  # Outputs: True

# -------------------------------------

"""
6. Frozen Sets
- Definition: A frozen set is an immutable version of a set.
- Syntax: frozenset([iterable])
"""

# Example
my_frozenset = frozenset([1, 2, 3, 4])
print(my_frozenset)

# -------------------------------------

"""
7. Set Comprehension
- Syntax: {expression for item in iterable}
"""

# Example
squares = {x**2 for x in range(5)}
print(squares)  # Outputs: {0, 1, 4, 9, 16}

# -------------------------------------

"""
8. Tasks and Exercises
Task 1: Create a set of unique numbers from a list containing duplicates.
"""
# Task 1 Example
num_list = [1, 2, 2, 3, 4, 4, 5]
unique_nums = set(num_list)
print(unique_nums)  # Outputs: {1, 2, 3, 4, 5}

"""
Task 2: Write a Python program that takes two sets of numbers and returns their union, intersection, and difference.
"""
# Task 2 Example
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.union(set_b))        # Union: {1, 2, 3, 4, 5, 6}
print(set_a.intersection(set_b)) # Intersection: {3, 4}
print(set_a.difference(set_b))   # Difference: {1, 2}

"""
Task 3: Given a set of student names, write a program that removes a specified name if it exists.
"""
# Task 3 Example
students = {"Alice", "Bob", "Charlie", "David"}
student_to_remove = "Bob"
students.discard(student_to_remove)
print(students)  # Outputs: {'Alice', 'Charlie', 'David'}

"""
Task 4: Write a Python function to return the symmetric difference between two sets of strings.
"""
# Task 4 Example
def symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "date", "fig"}
print(symmetric_difference(set1, set2))  # Outputs: {'apple', 'cherry', 'date', 'fig'}

"""
Task 5: Create two sets: one with even numbers and another with multiples of 3.
         Find the union, intersection, and difference between these sets.
"""
# Task 5 Example
evens = {2, 4, 6, 8, 10}
multiples_of_3 = {3, 6, 9, 12}
print(evens.union(multiples_of_3))        # Union
print(evens.intersection(multiples_of_3)) # Intersection
print(evens.difference(multiples_of_3))   # Difference

"""
Task 6: Write a Python program that checks if one set is a subset or superset of another set.
"""
# Task 6 Example
small_set = {1, 2}
large_set = {1, 2, 3, 4}
print(small_set.issubset(large_set))  # True
print(large_set.issuperset(small_set)) # True

"""
Task 7: Use set comprehension to generate a set of the squares of numbers between 1 and 10, but only include numbers that are even.
"""
# Task 7 Example
squares_of_even = {x**2 for x in range(1, 11) if x % 2 == 0}
print(squares_of_even)  # Outputs: {4, 16, 36, 64, 100}
