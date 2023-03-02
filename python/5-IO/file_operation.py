# Reading Files in Python

file1 = open("text.txt", "r")
read_content = file1.read()
print(read_content)
file1.close()


# Use of with...open Syntax
with open("text.txt", "r") as file2:
    print(file2.read())
    file2.close()


# Writing to Files in Python
with open("demo.txt", "w") as file3:
    file3.write("this is a new file")
    file3.close()