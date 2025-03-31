Tree = [[1,9,2],[3,7,-1],[4,13,5],[-1,5,-1],[-1,12,-1],[-1,15,-1],[-1,7,-1],[-1,8,-1],[-1,9,-1],[-1,-1,-1]]
Rootpointer = 0
Freepointer = 6

def InsertTree(Num):
    global Tree, Freepointer, Rootpointer
    # Num = int(input("Data to add: "))
    if Freepointer != -1:
        Next = Tree[Freepointer][1] #temp for 7 from ([-1,7,-1])
        Tree[Freepointer][0] = -1
        Tree[Freepointer][1] = Num
        Tree[Freepointer][2] = -1

        if Rootpointer == -1: #means it will be the first item in the tree
            Rootpointer = 0
        currentpointer = Rootpointer #do not change rootp value so put in another varible
        
        Flag = True
        while Flag == True:
            if Num < Tree[currentpointer][1]: #go left
                if Tree[currentpointer][0] == -1:
                    Tree[currentpointer][0] = Freepointer
                    Flag = False
                    Freepointer = Next
                else:
                    currentpointer = Tree[currentpointer][0]
            if Num > Tree[currentpointer][1]:
                if Tree[currentpointer][2] == -1:
                    Tree[currentpointer][2] = Freepointer
                    Flag = False
                    Freepointer = Next
                else:
                    currentpointer = Tree[currentpointer][2]

    else:
        print("Tree is full")

InsertTree(16)
print(Tree)
print(Freepointer,Rootpointer)
InsertTree(8)
print(Tree)
print(Freepointer,Rootpointer)
