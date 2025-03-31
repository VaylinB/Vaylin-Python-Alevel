#Inheritance in Object-Oriented Programming (OOP)
# Inheritance is a fundamental concept in OOP that allows a class (called the child class or subclass) 
# to inherit attributes and methods from another class (called the parent class or superclass). 
# This promotes code reuse and allows you to build upon existing functionality.

# Parent Class
class Car:
    # Constructor: Initializes the object with attributes
    def __init__(self, brand, year, colour):
        self.__brand = brand  # Private attribute for car brand
        self.__year = year    # Private attribute for manufacturing year
        self.__colour = colour  # Private attribute for car colour

    # Getter method for brand
    def get_brand(self):
        return self.__brand

    # Setter method for brand
    def set_brand(self, new_brand):
        self.__brand = new_brand

    # Getter method for year
    def get_year(self):
        return self.__year

    # Setter method for year
    def set_year(self, new_year):
        if new_year > 1885:  # Validation: Cars were invented after 1885
            self.__year = new_year
        else:
            print("Invalid year!")

    # Getter method for colour
    def get_colour(self):
        return self.__colour

    # Setter method for colour
    def set_colour(self, new_colour):
        self.__colour = new_colour

    # Method to display car details
    def display_details(self):
        return f"Brand: {self.__brand}, Year: {self.__year}, Colour: {self.__colour}"







# Child Class
#The child class can add new attributes and methods or 
# override existing ones to extend or modify the behavior of the parent class.

class ElectricCar(Car):
    # Constructor: Extends the parent class constructor
    def __init__(self, brand, year, colour, battery_capacity):
        super().__init__(brand, year, colour)  # Call the parent class constructor
    #super() Keyword:
    # Used to call the parent class's constructor or methods.
    # Example: super().__init__(brand, year, colour) initializes the attributes of the parent class.

        self.__battery_capacity = battery_capacity  # New attribute for battery capacity

    # Getter method for battery capacity
    def get_battery_capacity(self):
        return self.__battery_capacity

    # Setter method for battery capacity
    def set_battery_capacity(self, new_capacity):
        if new_capacity > 0:
            self.__battery_capacity = new_capacity
        else:
            print("Invalid battery capacity!")

    # Method to display electric car details
    def display_details(self):
        # Extend the parent class method
        parent_details = super().display_details()
        return f"{parent_details}, Battery Capacity: {self.__battery_capacity} kWh"
    
# Create an object of the parent class
car1 = Car("Toyota", 2020, "Red")
print(car1.display_details())  # Output: Brand: Toyota, Year: 2020, Colour: Red
    
# Create an object of the child class
electric_car1 = ElectricCar("Tesla", 2022, "White", 75)
print(electric_car1.display_details())  # Output: Brand: Tesla, Year: 2022, Colour: White, Battery Capacity: 75 kWh
    
# Access and modify attributes using getter and setter methods
print(electric_car1.get_battery_capacity())  # Output: 75
electric_car1.set_battery_capacity(100)
print(electric_car1.get_battery_capacity())  # Output: 100