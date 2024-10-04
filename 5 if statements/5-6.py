age=int(input("Enter age: "))
if (age<2):
    print("\n a baby")
#elif (age>=2)and(age<4):
elif 2<=age<4:
    print("\n a toddler")
elif 4<=age<13:
    print("\n a kid")
elif 13<=age<20:
    print("\n a teenager")
elif 20<=age<65:
    print("\n an adult")
elif age>=65:
    print("\nan elder")
else:
    print("\nInvalid input")