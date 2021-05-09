f1 = open("file2.txt")
print(f1.tell()) #this will tell the location of the pointer on which caracter it is.
print(f1.readline())
print(f1.tell())
print(f1.seek(2)) #to reset file pointer
print(f1.readline())
f1.close()

# With block to open python files the pros of using this is with block handle the close file function
with open("file2.txt") as f:
    r =f.read(12)
    print(r)
print(f.readlines())