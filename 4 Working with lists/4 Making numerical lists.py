#Using range function
for value in range(1,5):
    print(value)
    
#Using range() to Make a List of Numbers
numbers = list(range(1, 6))
print(numbers)

print("\n")

    # skip numbers in a given range. If you pass a third argument to range(), Python uses that value as a step size when generating numbers.
even_numbers = list(range(2, 11, 2))
print(even_numbers)
    # starts with the value 2 and then adds 2 to that value. It adds 2 repeatedly until it reaches or passes the end value, 11, 
    
    # make a list of the first 10 square numbers (that is, the square of each integer from 1 through 10). In Python, two asterisks (**) represent exponents.   
squares=[]
for value in range(1,10):
    square=value ** 2
    squares.append(square)
print(squares)

#Simple Statistics with a list of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))

print(max(digits))

print(sum(digits))

#List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)
    #combine the four lines in one line