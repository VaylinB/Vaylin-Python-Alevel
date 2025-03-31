Array = ['a','b','c']



Find = input("Enter value to find:")
Found = False


for i in range(len(Array)):
    if Array[i] == Find:
        Found = True

if Found == True:
    print("Item is found")
else:
    print("Item not found")