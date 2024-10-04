pizzas=['A','B','C']
friend_pizzas=['A','B','C']

pizzas.append('D')
friend_pizzas.append('E')

print(pizzas)
print(friend_pizzas)

for pizza in pizzas:
    print(pizza)
    
print("\n\n")

for fpizza in friend_pizzas:
    print(fpizza)
    
# for pizza in pizzas:
#     print("\n")
#     print(pizza)
#     print(f"I like pizza {pizza}")
    
# print("\nI really very much like pizza")