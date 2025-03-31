#2a  declare a record structure, SaleData, to store the data about each sale.

class SaleData:
    def __init__(self,PSaleID,PQuantity):
        self.SaleID = PSaleID #string
        self.Quantity = PQuantity#integer


global Head #int
global Tail #int
global NumberOfItems #int
CircularQueue= [ ["",-1] for i in range(5)] #SaleData, 5 items
Head= 0
Tail= 0
NumberofItems =0


def Enqueue(NewRecord):
    global NumberofItems,Head,Tail #int
    if NumberofItems == len(CircularQueue):
        return -1
    else:
        NumberofItems += 1
        CircularQueue[Tail] = NewRecord
        Tail = Tail + 1
        if Tail == len(CircularQueue):
            Tail = 0
        return 1
    
def Dequeue():
    global NumberofItems,Head,Tail #int
    if NumberofItems == 0 :
        return ["",-1]
    else:
        Head += 1
        if Head == 5: #len(CircularQueue)
            Head = 0
        NumberofItems -= 1
        return CircularQueue[Head]

#2e
def EnterRecord():
    pID= input("Enter ID:")
    Quantity = int(input("Enter Quantity"))
    SaleRecord = SaleData(pID,Quantity) #record
    Value= Enqueue(SaleRecord)

    if Value == -1:
        print("Full")
    else:
        print("Stored")

#2f
for i in range(6):
    EnterRecord()
ReturnVal = Dequeue()
if ReturnVal == ["",-1]:
    print("Circular queue is empty")
else:
    print(ReturnVal.SaleID," ",ReturnVal.Quantity)
EnterRecord()
for i in range(len(CircularQueue)):
    print(CircularQueue[i].SaleID," ",CircularQueue[i].Quantity)
