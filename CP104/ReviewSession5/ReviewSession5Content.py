# Files

# Opening a file
mode = "r" # read
mode = "w" # write
mode = "a" # append

file = open("filename", mode)

# Reading a file
file = open("filename", "r")
line = file.readline()
while line != "":
    print(line)
    line = file.readline()
file.close()

# Writing to a file
file = open("filename", "w")
file.write("Hello World")
file.close()

# Appending to a file
file = open("filename", "a")
file.write("Hello World")
file.close()

# 2D Lists

# Creating a 2D list
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] # 3x3 list

# Accessing a 2D list list[row][column]
print(lst[0][0]) # 1
print(lst[1][1]) # 5
print(lst[1][2]) # 6

# Modifying a 2D list
lst[0][0] = 10
print(lst)