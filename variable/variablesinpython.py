var1="Hello python"
var2= 4
var3= 32.4
var4= ",target"
var5 = "22"
var6 = "22"
print(type(var1))
print(type(var2))
print(type(var3))
print(var2+var3)
print(var5+var6)
print(int(var5)+int(var6))
print(var1+var4)
print(10* var1)
print(10 *int(var5)+int(var6))
print(10 *str(int(var5)+int(var6)))

"""
Calculator to take number from user and add it
"""
print("Enter 1st number")
input1 = input()
print("Enter 2st number")
input2 = input()
print(int(input1)+int(input2))