#2a
class Node:
    def __init__(self,PData):
        self.__LeftPointer = -1  #int
        self.__Data = PData       #int
        self.__RightPointer = -1  #int
    
    def GetLeft(self):
        return self.__LeftPointer
    
    def GetData(self):
        return self.__Data
    
    def GetRight(self):
        return self.__RightPointer
    
    def SetLeft(self,NewLeft):
        self.__LeftPointer = NewLeft

    def SetRight(self,NewRight):
        self.__RightPointer = NewRight
    
    def SetData(self,NewData):
        self.__Data = NewData

class TreeClass:
    def __init__(self):
        self.__Tree = [] #type of node 20 spaces
        self.__FirstNode = -1 #integer
        self.__NumberNodes = 0 #integer
        for i in range(20):
            self.__Tree.append(Node(-1))

    def InsertNode(self, NewNode):
        if self.__NumberNodes == 0:
            # Insert the first node
            self.__Tree[0] = NewNode
            self.__NumberNodes += 1
            self.__FirstNode = 0
        else:
            # Insert subsequent nodes
            self.__Tree[self.__NumberNodes] = NewNode

            NodeAccess = self.__FirstNode
            Direction = ""

            while NodeAccess != -1:
                Previous = NodeAccess
                if NewNode.GetData() < self.__Tree[NodeAccess].GetData():
                    Direction = "left"
                    NodeAccess = self.__Tree[NodeAccess].GetLeft()
                elif NewNode.GetData() > self.__Tree[NodeAccess].GetData():
                    Direction = "right"
                    NodeAccess = self.__Tree[NodeAccess].GetRight()

            if Direction == "left":
                self.__Tree[Previous].SetLeft(self.__NumberNodes)
            elif Direction == "right":
                self.__Tree[Previous].SetRight(self.__NumberNodes)

            # Increment the number of nodes
            self.__NumberNodes += 1

           
    def OutputTree(self):
        if self.__NumberNodes == 0:
            print("No nodes")
        else:
            for x in range(0,self.__NumberNodes):
                print(self.__Tree[x].GetLeft()," ", self.__Tree[x].GetData(), " ",self.__Tree[x].GetRight())


TheTree = TreeClass()
TheTree.InsertNode(Node(10))
TheTree.InsertNode(Node(11))
TheTree.InsertNode(Node(5))
TheTree.InsertNode(Node(1))
TheTree.InsertNode(Node(20))
TheTree.InsertNode(Node(15))
TheTree.OutputTree()


