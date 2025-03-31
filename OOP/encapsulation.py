
# Encapsulation : 
# You can make attributes private by prefixing them with __ (double underscores).
# By making attributes private (using double underscores __), 
# you can restrict direct access to them from outside the class.

# Access to private attributes is provided through getter and setter methods.
# Getter methods retrieve the value of private attributes.
# Setter methods modify the value of private attributes, often with validation.

class Car:
    # Constructor: Initializes the object with private attributes
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