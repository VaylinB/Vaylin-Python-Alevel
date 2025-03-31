Queue = [None for i in range(5)]
front = 0
rear = -1
queuefull = len(Queue)
size = 0

def enqueue(item):
    global front,rear,size,queuefull

    if size == queuefull:
        return "Queue is full"
    else:
        rear = rear + 1
        size = size + 1

        if rear == queuefull:
            rear = 0
        
        Queue[rear] = item
        return f"Enqueue : {item}"

def dequeue():
    global front,rear,size,queuefull

    if size ==0:
        return -1

    else:
       value = Queue[front]
       front = front + 1
       size = size - 1
       if front == queuefull:
           front = 0

       return value
    

        
    
