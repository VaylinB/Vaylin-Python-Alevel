Array = [3,5,7,9,10]

Value = int(input("Enter value to find:"))
Found = False
Flag = True
low = 0 
high = len(Array)-1


while Flag == True:
    mid = (high + low) // 2  # // makes the mid value returned as integer
    
    if Array[mid] == Value:
        Found = True
        Flag = False
    elif Array[mid] > Value:
        high = mid - 1
    
    elif Array[mid] < Value:
        low = mid + 1
    
    if low > high:
        Flag = False

if Found:
    print("Item is found")
else:
    print("Item not found")


