tree = [[-1,i,-i] for i in range (1,11)]
tree[9][1] = -1 #last need to be -1
rootpointer = -1
heappointer = 0

for line in tree:
    print(line)