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
        
class Battery:
    """A simple attempt to model a battery for an electric car."""
    def __init__(self,battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size   
     
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.") 
     
    def get_range(self):
        """print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        
        print(f"This car can go about {range}  miles on a full charge.") 
     
    def upgrade_battery(self):
        if self.battery_size == 65:
            print("Battery is not ready.") 
                  
class ElectricCar(car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
       """Initialize attributes of the parent class."""
       super().__init__(make, model, year)
       self.battery=Battery()
       # In the ElectricCar class, we now add an attribute called self.battery 3. This line tells Python to create a new instance of Battery (with a default size of 40, because we’re not specifying a value) and assign that instance to the attribute self.battery.
       # any ElectricCar instance will now have a Battery instance created automatically.
       self.battery_size=100
       
my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
my_leaf.battery.upgrade_battery()
my_leaf.battery.get_range()
