# Parent Class
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"They serve {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Child Class
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type='Ice Cream', flavors=None):
        super().__init__(restaurant_name, cuisine_type)  # Pass parent parameters here
        self.flavors = flavors if flavors is not None else []  # Initialize flavors
    
    def display_flavors(self):
        print(f"Available flavors: {', '.join(self.flavors) if self.flavors else 'No flavors available.'}")

# Creating an instance of IceCreamStand
icecream_stand = IceCreamStand("Sweet Treats", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])

# Calling methods from both the parent and child classes
icecream_stand.describe_restaurant()  # Calls parent method
icecream_stand.open_restaurant()       # Calls parent method
icecream_stand.display_flavors()       # Calls child method
