#Slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[0:3])
#returns 0,1,2 items

print(players[1:4])
#returns 1,2,3

print(players[:4])
#return 0,1,2,3

print(players[2:])
#2 to all

print(players[-3:])
#return last 3

print(players[:-3])
#return first 2

#Looping Through a Slice
print("Here are the first three players on my team:")
for player in players[:3]:
   print(player.title())#capital first letter
   
#Copying a list
my_foods=['pizza','falafel','carrot cake']
friend_foods=my_foods[:]

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n\n")

my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

print("\n\n")
friend_foodss = my_foods
print(friend_foodss)