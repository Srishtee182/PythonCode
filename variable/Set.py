#Set is a collection of well defined object

s = set()
print(type(s))
set_from_list = set([1,2,3,4])
print(type(set_from_list))
print(set_from_list)
List = [2,3,5,6]
setList = (List)
print(List)
#difference between set and list is set append unique value
s.add(1)
print(s)
s.add(2)
s.add(1)
print(s)
s1=({1,2,3})
s2=({3,4,5})
print(s1.union(s2))
print(s1.intersection(s2))