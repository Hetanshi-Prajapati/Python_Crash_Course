#Accessing Elements in a list
#Index Positions Start at 0, Not 1
bicycles=['trek','connondale','redline','specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])
print("\n")
print(bicycles[-1])
print(bicycles[-2])
print(bicycles[-3])
print(bicycles[-4])
print("\n")

message = (f"My first bicycle was a {bicycles[0].title()}.")
print(message)