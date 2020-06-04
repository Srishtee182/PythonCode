""" File IO basics

  "r" - open file for read - default
 "w" - open file for write
 "x" - Creates file if not exists
 "a" - Add more content to file
 "t" - text mode>> your file is open as text file - default
 "b" - binary mode
 "+" - open file to update(read and write)
 """
print("func doc string read and print code")
f = open("file.txt") #open will return file pointer, also this file will open with default text mode
print(f.read(3)) # read first 3 character from file
print(f.read(4)) # read four character from file after first 3
print(f.read())
f.close()
print("")
print("read in binary mode")
f = open("file.txt", "rb")
print(f.read())
f.close()


print("Read line function")
f = open("file.txt")
print(f.readline(), end="")
print(f.readline(), end="")
f.close()

print("")
print("print line by line we need to iterate it")
f = open("file.txt") #open will return file pointer, also this file will open with default text mode
for line in f:
    print(line, end="")
f.close()

print("Read all lines together and print as a list")
f = open("file.txt")
print(f.readlines())

#Writing on file
# when we do this it will add the given data and remove the previous data from file
#f = open("file.txt", "w")
# if if you don't want to replace the content use apend
f = open("file.txt", "a")
noOfCharacterWrite =f.write("\nI am adding the first new line\n")
print(noOfCharacterWrite)# this will print number of character wrote by user
f.close()

#how to read and write both
f = open("file.txt", "r+")
print(f.read())

f.write("\nI am adding the second new line\n")

f.close()