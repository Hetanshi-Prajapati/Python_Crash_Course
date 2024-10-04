cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
       print(car.upper())
    else:
       print(car.title())

print("\n\n")
car = 'bmw'
car == 'bmw'
print(True)

print("\n\n")

car = 'audi'
car == 'bmw'
print(False)

# Ignoring Case When Checking for Equalitly
car = 'Audi'
car == 'audi'

#Checking for Inequality
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
   print("Hold the anchovies!")
   
print("\n\n")

#Numerical Comparisons
answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")