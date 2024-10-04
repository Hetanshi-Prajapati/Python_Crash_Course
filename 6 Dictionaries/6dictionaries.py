alien_o={'color':'green', 'points':5}
print(alien_o['color'])
print(alien_o['points'])

print("\n\n")
# alien_o={'color':'green,red,yellow', 'points':'5,6,7'}
# print(alien_o['color'])
# print(alien_o['points'])


#in list:more then one value in a key
my_dict={
    'fruits':['apple','banana','cherry'],
    'vagetables':['carrot','broccoli','spinach']
}
print(my_dict['fruits'])

#in tuple: mre then one value in a key
my_dict={
    'fruits':['apple','banana','cherry'],
    'vagetables':['carrot','broccoli','spinach']
}
print(my_dict['fruits'])

print("\n\n")

# Accessing Values in a Dictionary
new_points=alien_o['points']
print(f"You just eaarned {new_points} points!")

print("\n\n")

#Adding new key-value pairs
alien_o['x_position']=0
alien_o['y_position']=25
print(alien_o)

print("\n\n")

#starting with empty dictionary
blien_o={}

blien_o['color']='green'
blien_o['points']=5

print(blien_o)

#Modifying values in a Dictionary
clian_o={'color':'green'}
print(f"The clian is {clian_o['color']}.")

clian_o['color']='yellow'
print(f"The clian is now {clian_o['color']}.")


print("\n\n")
#Another example

dlien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {dlien_0['x_position']}")
# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if dlien_0['speed'] == 'slow':
   x_increment = 1
elif dlien_0['speed'] == 'medium':
   x_increment = 2
else:
   # This must be a fast alien.
   x_increment = 3
# The new position is the old position plus the increment.
dlien_0['x_position'] = dlien_0['x_position'] + x_increment
print(f"New position: {dlien_0['x_position']}")


print("\n\n")
#Removing Key-Value Pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)
del alien_0['points']
print(alien_0)

print("\n\n")
#Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")


print("\n\n")
#Using get() to access values
alien_0 = {'color': 'green', 'speed': 'slow'}
#print(alien_0['points'])#error
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)