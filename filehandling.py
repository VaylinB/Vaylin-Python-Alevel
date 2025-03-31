#read file and store in array
file = open("Number.txt",'r')
numberarray = [int(file.readline().strip()) for i in range(10)]
print(numberarray)
file.close

#USE THIS IN EXAM

file = open("Number.txt","r")
numArray = []
for line in file:
    numArray.append(line.rstrip())
print(numArray)
file.close


#read everything in file output one by one
file = open("Number.txt","r")
text= file.read()
print(text)
file.close

#if text = file.read(2) it prints 1 and \n

# print 1 then 2
file = open("Number.txt","r")
text2 = file.readline()
print(text2)
text2 = file.readline()
print(text2)
file.close


name = "   shuaib  "

#to remove spaces

print(name.strip())         #all spaces
print(name.lstrip())        #at the left
print(name.rstrip())        #at the right

# Example array
numArray = [1, 2, 3]

# Append a single value
numArray.append(4)
print(numArray)  # [1, 2, 3, 4]

# Insert at a specific index
numArray.insert(1, 10)  # Inserts 10 at index 1
print(numArray)  # [1, 10, 2, 3, 4]

# Extend with multiple values
numArray.extend([5, 6, 7])
print(numArray)  # [1, 10, 2, 3, 4, 5, 6, 7]


