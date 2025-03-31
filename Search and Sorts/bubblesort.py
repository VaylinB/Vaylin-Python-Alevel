Array = [9,8,7,6,5]
swap = True
top = len(Array) - 1

while swap:
    swap = False

    for i in range(top):
        if Array[i] > Array[i+1]:
            Array[i],Array[i+1] = Array[i+1],Array[i]
            # temp = Array[i]
            # Array[i] = Array[i+1]
            # Array[i+1] = temp
            swap = True
    top = top -1
    print(Array)