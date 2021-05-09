#Map funtion - it will apply a particular funtion in list
num = ["2", "44", "22", "33"]# string format
num2 = ["2", "44", "22", "33"]# string format

#num[2] = num[2] + 1 this will not work as number is in string format

#tough method
for item in range(len(num)):
    num[item] = int(num[item])
num[2] = num[2] + 1

print(num[2])

#map function
num2 = list(map(int, num2))
print(num2[2]+1)

squarethem = [1,2,3,4,5,6,7,8,9,10]
def sqfunc(a):
    return a*a
square = list(map(sqfunc, squarethem))
print(square)
add = list(map(lambda x:x+x,squarethem))
print(add)

def sq2(a):
    return a*a
def cube(a):
   return a*a*a

func =[sq2, cube]
for i in range(7):
    var = list(map(lambda x:x(i), func))
    print(var)

#filter funtion
list_1 = [1,2,3,4,5,6,7,8,9]
def is_greater_5(num):
    return num>5
gr_then_5 = list(filter(is_greater_5,list_1))
print(gr_then_5)

#reduce function
from functools import reduce
reducelist = [1,2,3,4,5]
#to add number of list
reduceadd= reduce(lambda x,y:x+y, reducelist)
print(reduceadd)