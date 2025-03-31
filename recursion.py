Array = [1,2,3]

def sum(array):
    if len(array) ==0:
        return 0
    return array[0] + sum(array[1:]) #excluding first char

print(sum(Array))