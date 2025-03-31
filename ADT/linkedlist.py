data = [9,6,4,None,None,None]
pointer = [-1,0,1,4,5,-1]

HeapPointer = 3
StartPointer = 2

def FindElement(item):
    global HeapPointer,StartPointer
    i = StartPointer
    while i != -1:
        if data[i] == item:
            return i
        else:
            i = pointer[i]
    return -1

def InsertElement(item):
    global HeapPointer,StartPointer
    if HeapPointer == -1:
        return "Heap is full"
    else:
        # Rewrite 4 pointers:  heap, start, old data, and old pointer
        newindex = HeapPointer #temp
        data[newindex] = item
        HeapPointer = pointer[HeapPointer]
        pointer[newindex] = StartPointer
        StartPointer = newindex

def DeleteElement(item):
    global HeapPointer, StartPointer
    i = StartPointer  # Start traversing from the first node
    previous = -1  # Initialize previous to -1 (no previous node at the start)

    while i != -1:  # Traverse the linked list
        if data[i] == item:  # If the item is found
            if previous == -1:  # If the item is the first node
                StartPointer = pointer[i]  # Update StartPointer to skip the node
                #startpointer = 1

            else:  # If the item is in the middle or end
                pointer[previous] = pointer[i]  # Skip the node in the linked list

            # Add the deleted node to the free list
            pointer[i] = HeapPointer
            HeapPointer = i
            data[i] = None  # Clear the data
            print(data)
            return f"Deleted {item}"  # Return success message

        previous = i  # Update previous to the current node
        i = pointer[i]  # Move to the next node

    return "Element not found"  # Return failure message if list is empty

print(DeleteElement(9))
# Table: Deleting Element 9
"""
| Step | Action                          | i (current node) | previous (prev) | data                  | pointer                    |  HeapPointer | StartPointer |
|------|---------------------------------|------------------|-----------------|-----------------------|--------------------        |-   ------------|--------------|
| 1    | Start traversal                 | 2                | -1              | [9, 6, 4, None, None, None] | [-1, 0, 1, 4, 5, -1] | 3              | 2            |
| 2    | Move to next node               | 1                | 2               | [9, 6, 4, None, None, None] | [-1, 0, 1, 4, 5, -1] | 3              | 2            |
| 3    | Move to next node               | 0                | 1               | [9, 6, 4, None, None, None] | [-1, 0, 1, 4, 5, -1] | 3              | 2            |
| 4    | Found item 9                    | 0                | 1               | [9, 6, 4, None, None, None] | [-1, 0, 1, 4, 5, -1] | 3              | 2            |
| 5    | Update pointer[1] to -1         | 0                | 1               | [9, 6, 4, None, None, None] | [-1, -1, 1, 4, 5, -1] | 3             | 2            |
| 6    | Add node 0 to free list         | 0                | 1               | [None, 6, 4, None, None, None]| [3, -1, 1, 4, 5, -1]| 0           | 2            |
"""

# Final State:
# data = [None, 6, 4, None, None, None]
# pointer = [3, -1, 1, 4, 5, -1]
# HeapPointer = 0
# StartPointer = 2



