# Containment in Object-Oriented Programming (OOP)
# Containment (also known as composition) is a design principle in OOP where one class contains 
# an instance of another class as part of its attributes. It represents a "has-a" relationship between objects.

# Key Features of Containment:
# "Has-a" Relationship:

# Containment models a relationship where one object "has a" reference to another object.
# Example: A Car "has an" Engine.

# Class representing an Engine
class Engine:
    def __init__(self, horsepower, engine_type):
        self.horsepower = horsepower  # Attribute for engine horsepower
        self.engine_type = engine_type  # Attribute for engine type

    def get_details(self):
        return f"Horsepower: {self.horsepower}, Type: {self.engine_type}"


# Class representing a Car
class Car:
    def __init__(self, brand, year, colour, engine):
        self.brand = brand  # Attribute for car brand
        self.year = year  # Attribute for manufacturing year
        self.colour = colour  # Attribute for car colour
        self.engine = engine  # Containment: Car "has an" Engine

    def display_details(self):
        return (
            f"Brand: {self.brand}, Year: {self.year}, Colour: {self.colour}, "
            f"Engine: [{self.engine.get_details()}]"
        )


# Create an Engine object
engine1 = Engine(300, "V8")

# Create a Car object with the Engine object
car1 = Car("Toyota", 2020, "Red", engine1)

# Display car details
print(car1.display_details())
# Output: Brand: Toyota, Year: 2020, Colour: Red, Engine: [Horsepower: 300, Type: V8]