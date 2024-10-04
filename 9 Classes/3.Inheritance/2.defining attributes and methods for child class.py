class car:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
        
    def get_descriptive_name(self):
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self,mileage):
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("your can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
class ElectricCar(car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
       """Initialize attributes of the parent class."""
       super().__init__(make, model, year)
       self.battery_size=40
    
    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")
        
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()