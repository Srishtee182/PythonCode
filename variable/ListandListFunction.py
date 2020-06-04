target = ["manual", "java", "sql", "aws", "python"]
print(target)
number=[44,9,66,8,54]
number.sort()
print(number)
number.reverse()
print(number)
print(len(number))
print(max(number))
print(min(number))
number.append(9)
print(number)
number.insert(2,3)
print(number)
number.pop()
print(number)
number[1] = [2]
# we have list and tuple, list is mutable and tuple is immutable
tp=(1,2,3,2)
#tp[1] = 5 will not work
print(tp)
tp2=[1]
print(tp2)
tp3=(1,) #if you are making tuple comma is important
print(tp3)
#swapping in python
a= 4
b=6
a,b=b,a
print (a, b)

list1 = [2,5,3,1]
list2 = [4,6,2,5]
list1.extend(list2)
print(list1)