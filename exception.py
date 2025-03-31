try:
    num1 = int(input("Enter number:"))
    num2 = int(input("Enter number:"))
    print("division value is:",num1/num2)

    file = open("fileHandling.txt")
except ZeroDivisionError:
    print("llegal division by zero")
except IndexError:
    print("Index out of bounds")
except FileNotFoundError:
    print("File not found")