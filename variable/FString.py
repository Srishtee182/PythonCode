import math
#explore time module
me = "Srishtee"

me2= "pandey"

a = "This is %s"%me # this is not F string but an string formating
print(a)

c= "This is {1} {0}"

b=c.format(me, me2)
print(b)

#FString starts
d= f"this is {me} {me2} {4 * 6} {math.tan(90)}"
print(d)
