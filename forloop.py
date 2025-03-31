# Syntax of range()
# start: The starting value of the sequence (inclusive). Default is 0.
# stop: The ending value of the sequence (exclusive). This is required.
# step: The difference between each number in the sequence. Default is 1.

# range(start, stop, step)

# 1. Basic Usage
for i in range(5):  # Generates numbers from 0 to 4
    print(i)

# 2. Specifying a Start and Stop
for i in range(2, 6):  # Generates numbers from 2 to 5
    print(i)

# 3. Using a Step
for i in range(0, 10, 2):  # Generates numbers from 0 to 8, stepping by 2
    print(i)
""
0
2
4 
6
8
""
