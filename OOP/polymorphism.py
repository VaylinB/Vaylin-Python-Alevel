# POlymorphism : Polymorphism allows the same method name (display_details) to 
# behave differently depending on the object that calls it.
#  Parent Class
class Car:
    def __init__(self, brand, year, colour):
        self.__brand = brand
        self.__year = year
        self.__colour = colour

    def display_details(self):
        return f"Brand: {self.__brand}, Year: {self.__year}, Colour: {self.__colour}"

# Child Class
#The ElectricCar class overrides the display_details method
# to include additional information about the battery capacity.
class ElectricCar(Car):
    def __init__(self, brand, year, colour, battery_capacity):
        super().__init__(brand, year, colour)
        self.__battery_capacity = battery_capacity

    def display_details(self):
        parent_details = super().display_details()
        return f"{parent_details}, Battery Capacity: {self.__battery_capacity} kWh"
    
# Create an object of the parent class
car1 = Car("Toyota", 2020, "Red")
print(car1.display_details())  # Output: Brand: Toyota, Year: 2020, Colour: Red

# Create an object of the child class
electric_car1 = ElectricCar("Tesla", 2022, "White", 75)
print(electric_car1.display_details())  # Output: Brand: Tesla, Year: 2022, Colour: White, Battery Capacity: 75 kWh