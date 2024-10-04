"""class restaurant:
    def __init__(self,restaurant_name,cuisine_type,number_served):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
        
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"They serve {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        #Print a message indicating that the restaurant is open.
        print(f"{self.restaurant_name} is now open!")
  
    def number_seved(self,number):
        self.number_served=number
        
    def increment_number_served(self,additional_customers):
        self.number_served+=additional_customers
        
restaurant=restaurant('olive garden','Italian')  
# print(f"Restaurant Name: {restaurant.restaurant_name}")
# print(f"Cuisine Type: {restaurant.cuisine_type}")

# Call the methods
restaurant.describe_restaurant()
restaurant.number_seved=25
print(f"Updated number of customer served: {restaurant.number_seved}")

restaurant.number_seved=100
print(f"Updated number of customer served: {restaurant.number_seved}")

restaurant.number_seved=30
print(f"Updated number of customer served: {restaurant.number_seved}")
"""

class restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
        self.number_served=0
        
    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}.")
        print(f"They serve {self.cuisine_type} cuisine.")
        
    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")
  
    def number_serve(self):
        print(f"Restaurant served {self.number_served} customers.")
        
restaurant1=restaurant('olive garden','Italian')  
restaurant2=restaurant('abc','def')  
restaurant2=restaurant('ghi','jkl')  
# print(f"Restaurant Name: {restaurant.restaurant_name}")
# print(f"Cuisine Type: {restaurant.cuisine_type}")

# Call the methods
restaurant1.describe_restaurant()
restaurant1.open_restaurant()
restaurant1.number_served=55
restaurant1.number_serve()
print("\n\n")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant2.number_served=34
restaurant2.number_serve()
print("\n\n")
restaurant2.describe_restaurant()
restaurant2.open_restaurant()
restaurant2.number_served=20
restaurant2.number_serve()
print("\n\n")