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
  
restaurant1=restaurant('olive garden','Italian')  
restaurant2=restaurant('abc','def')  
restaurant3=restaurant('ghi','jkl') 
 
# print(f"Restaurant Name: {restaurant.restaurant_name}")
# print(f"Cuisine Type: {restaurant.cuisine_type}")

# Call the methods
restaurant1.describe_restaurant()
restaurant1.open_restaurant()

print("\n\n")

restaurant2.describe_restaurant()
restaurant2.open_restaurant()

print("\n\n")

restaurant3.describe_restaurant()
restaurant3.open_restaurant()