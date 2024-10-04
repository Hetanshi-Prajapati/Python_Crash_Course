#Sorting a List Permanently with the sort() Method
    # store list of cars alphabetically
cars=['bmw','audi','toyota','subaru']
cars.sort()
print(cars)

print("\n")
    # store list of cars reverse-alphabetical order
cars=['bmw','audi','toyota','subaru']
cars.sort(reverse=True)
print(cars)
    #order of the list permanently changed
    
print("\n\n")
#Sorting a list Temporarily with the sorted() Function
cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

print("\nHere is the reverse sorted list:")
abc=sorted(cars,reverse=True)# sorted() function can also accept a reverse=True argument if you want to display a list in reverse-alphabetical order.
print(abc)

print("\nHere is the original list again:")
print(cars)

#Printing a list in Reverse Order
print("\n\n")
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

print("\n\n")
#Finding the length of string
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))
