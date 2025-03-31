
class Car:
    # Constructor: Initializes the object with attributes
    def __init__(self, brand, year, colour):
        self.brand = brand  # Attribute for car brand
        self.year = year    # Attribute for manufacturing year
        self.colour = colour  # Attribute for car colour

    # Method to display car details
    def display_details(self):
        return f"Brand: {self.brand}, Year: {self.year}, Colour: {self.colour}"

    # Method to change the car's colour
    def change_colour(self, new_colour):
        self.colour = new_colour
        return f"Colour changed to {self.colour}"
    
# Create objects (instances) of the Car class
car1 = Car("Toyota", 2020, "Red")
car2 = Car("Honda", 2018, "Blue")

# Access attributes
print(car1.brand)  # Output: Toyota
print(car2.year)   # Output: 2018

# Call methods
print(car1.display_details())  # Output: Brand: Toyota, Year: 2020, Colour: Red
print(car2.display_details())  # Output: Brand: Honda, Year: 2018, Colour: Blue

# Change the colour of car1
print(car1.change_colour("Black"))  # Output: Colour changed to Black
print(car1.display_details())       # Output: Brand: Toyota, Year: 2020, Colour: Black

