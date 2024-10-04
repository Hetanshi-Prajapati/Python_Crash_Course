"""When to use a list:
Mutability: Use a list when you need a collection that can be
modified (e.g., adding, removing, or changing elements).
code:
my_list = [1, 2, 3]
my_list[0] = 4  # List is mutable, so this is allowed

Homogeneous or heterogeneous data: Lists are ideal for storing
either homogeneous (all same type) or heterogeneous data 
(mixed types).
code:
my_list = [1, "apple", 3.5]  # List can contain different types of elements

Dynamic operations: Use lists if you need to frequently 
perform dynamic operations like appending, slicing, and 
updating.
code:
my_list.append(4)  # Add an element to the end of the list


When to use a tuple:
Immutability: Use a tuple when the collection of items should 
not be modified after creation. Tuples are immutable, meaning 
once you create a tuple, its values cannot be changed.
code:my_tuple = (1, 2, 3)
# my_tuple[0] = 4  # This will raise a TypeError

Fixed structure: If the data is constant and represents a fixed
collection of items, use a tuple.
code:
person_info = ("John", 25, "Engineer")  # Use tuple for fixed information

Hashable keys: Tuples can be used as keys in dictionaries 
(since they are hashable), whereas lists cannot.
code:
my_dict = {(1, 2): "Point A", (3, 4): "Point B"}  # Tuple as a key

Performance: Tuples can be faster than lists in certain situations 
because of their immutability and smaller memory footprint.

Summary:
Use lists when you need a mutable, dynamic data structure.
Use tuples when you need a fixed, immutable data structure 
or when you need to use it as a dictionary key.
"""
#Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Error
#dimensions[0] = 250

print("\n\n")
#Looping Through All Values in a Tuple
for dimension in dimensions:
   print(dimension)

print("\n\n")
#Writing Over a Tuple
print("Original dimensions:")
for dimension in dimensions:
   print(dimension)
   
dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
   print(dimension)