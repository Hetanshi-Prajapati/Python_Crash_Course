class car:
    """A simple attempt to represent a car."""
    def __init__(self,make,model,year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reaading=0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
     
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reaading} miles on it.")
        
my_new_car = car('audi', 'a4', 2024)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reaading=23
my_new_car.read_odometer()