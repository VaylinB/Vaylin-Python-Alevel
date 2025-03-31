Array = [9, 8, 7, 6, 5]

for i in range(1,len(Array)):
    current = Array[i]
    j = i -1

    while j >=0 and Array[j] > current:
        # Shift the element to the right
        Array[j + 1] = Array [j] 
        j = j - 1

    # Insert the current element into its correct position
    Array[j+1] = current
    print(f"Pass {i} : {Array}")

#first pass
# Step	Array State	        j	Action
# 1	    [9, 8, 7, 6, 5]	    0	Compare 9 > 8
# 2	    [9, 9, 7, 6, 5]	    -1	Shift 9 to the right
# 3	    [8, 9, 7, 6, 5]	    -1

#second pass
# Step	Array State     	j	Action
# 1	    [ 8, 9, 7, 6, 5]	1	Compare 9 > 7, shift 9
# 2	    [8, 9, 9, 6, 5]	    0	Compare 8 > 7, shift 8
# 3	    [8, 8, 9, 6, 5]	    -1	Exit loop
# 4	    [7, 8, 9, 6, 5]	    -1	Insert 7 at j+1 = 0