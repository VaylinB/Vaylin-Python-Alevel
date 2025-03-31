NumberArray = [100,85,644,22,15,8,1] #integer


def RecursiveInsertion(IntegerArray, NumberElements):
    if NumberElements <= 1:
        return IntegerArray
    else:
        RecursiveInsertion(IntegerArray, NumberElements - 1)
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
    LoopAgain = True
    if CheckItem < 0:
        LoopAgain = False
    else:
        if IntegerArray[CheckItem] < LastItem:
            LoopAgain = False
    while LoopAgain:
        IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
        CheckItem = CheckItem -1
        if CheckItem <0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
    IntegerArray[CheckItem + 1] = LastItem
    return IntegerArray

SortedArray= RecursiveInsertion(NumberArray,len(NumberArray))
print("Recursive" , SortedArray)

def IterativeInsertion(IntegerArray, NumberElements):
    while NumberElements > 0:
        LastItem = IntegerArray[NumberElements - 1]
        CheckItem = NumberElements - 2
        LoopAgain = True
        if CheckItem < 0:
            LoopAgain = False
        else:
            if IntegerArray[CheckItem] < LastItem:
                LoopAgain = False
        while LoopAgain:
            IntegerArray[CheckItem + 1] = IntegerArray[CheckItem]
            CheckItem = CheckItem -1
            if CheckItem <0:
                LoopAgain = False
            else:
                if IntegerArray[CheckItem] < LastItem:
                    LoopAgain = False
        IntegerArray[CheckItem + 1] = LastItem
        NumberElements -= 1
    return IntegerArray

# print(IterativeInsertion(NumberArray,len(NumberArray)))

def BinarySearch(IntegerArray,First,Last,ToFind):
    if First > Last:  # Base case: If the range is invalid, the element is not found
        return -1
    
    mid = (First + Last) // 2
    midvalue = IntegerArray[mid]
    

    if ToFind == midvalue:
        return mid
    else:
        if ToFind< midvalue: #search fist half excluside midvalue
            # Last = mid - 1
        #     elif Array[mid] > Value:
        #        high = mid - 1
            return BinarySearch(IntegerArray,First, mid -1,ToFind)
        elif ToFind > midvalue: #search second half not includding mid value
            return BinarySearch(IntegerArray,mid + 1,Last,ToFind)
  

print(BinarySearch(SortedArray,0,6,100))
    
        