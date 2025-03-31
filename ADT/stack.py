Stack = [None for i in range(10)]
StackFull = len(Stack)-1
top = -1

def push(item):
    global top
    if top ==  StackFull:
        print("Stack is full")
    else:
        #top = top + 1
        top += 1 
        Stack[top] = item

def pop():
    global top
    if top == -1:
        print("Stack is empty")
        return -1
    else:
        value = Stack[top]
        top -= 1
        return value


