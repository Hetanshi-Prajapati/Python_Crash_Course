class restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"They serve {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")
  
restaurant=restaurant('olive garden','Italian')  
# print(f"Restaurant Name: {restaurant.restaurant_name}")
# print(f"Cuisine Type: {restaurant.cuisine_type}")

# Call the methods
restaurant.describe_restaurant()
restaurant.open_restaurant()