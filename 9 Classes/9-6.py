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


class IceCreamStand(restaurant):
    def __init__(self,restaurant_name,cuisine_type,flavors):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors=flavors
    
    def display_flavors(self):
        print(f"Flavors: {self.flavors}")

icecream=IceCreamStand('olive garden','Italian','Sweet Treats')       

# Call the methods
icecream.describe_restaurant()
icecream.open_restaurant()
icecream.number_served=55
icecream.number_serve()
icecream.display_flavors()
print("\n\n")
