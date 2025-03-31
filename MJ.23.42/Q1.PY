#1a Write program code to declare the global string array Animals to store 10 items.
global Animals  #array 10 elements string

#1b Write program code to store these animal names in the array.
Animals =[]
Animals.append("horse")
Animals.append("lion")
Animals.append("rabbit")
Animals.append("mouse")
Animals.append("bird")
Animals.append("deer")
Animals.append("whale")
Animals.append("elephant")
Animals.append("kangaroo")
Animals.append("tiger")

def SortDescending():
    ArrayLength = len(Animals)
    for x in range(0,ArrayLength-1):
        for y in range(0, ArrayLength-x-1):
            if Animals[y][0] < Animals[y+1][0]:
                Temp = Animals[y]
                Animals[y] = Animals[y+1]
                Animals[y+1] = Temp
SortDescending()
print("Sorted Contents of Animals array")
for line in range(len(Animals)):
    print(Animals[line])
    
        