while True:
    age=input("Enter your age: ")
    if age=='quit':
        break
    else:
        if (int(age)<3):
            print("Ticket is free")
        elif (3<=int(age)<=12):
            print("Ticket is 10$")
        else:
            print("Ticket is 15$")

#in this user can enter only integer value and 
# if user enter quit then program will be terminate
#if user give any otherinput then it give error