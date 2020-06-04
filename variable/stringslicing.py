myStr = "srishtee learning python"
print(myStr[0:9])
"""
No error in 0 to 90 index because it will show the char available
"""
print(myStr[0:90])
print(len(myStr))
"""
If  want to skip 1 character the follow below method
if you keep 1st column blank it will consider by default 0
if you keep 2st column blank it will consider by default length of string
if you keep 3st column blank it will consider by default 1
When we write negative number the it will start from last and -1 will be the last character, i.e., n
"""
print(myStr[0:90:2])
print(myStr[::])
print(myStr[::3])
print(myStr[::3466])
print(myStr[-8::2])
"""
Best way to reverse the string
"""
print(myStr[::-1])
print(myStr.isalnum()) # as string contain space it is not alpha numeric
print(myStr.count("e"))
print(myStr.capitalize())# made index 0 to capital letter
print(myStr.find("learning"))# learning is starting from 9th index
print(myStr.upper())
print(myStr.replace("python","Java and python"))
