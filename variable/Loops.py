list1 = ["Srishtee","Vinay","Saroj","Mayank"]
#list and tuple,dictionary can be iterated
for item in  list1:
    print(item)
list2 = [["Srishtee",24],["Vinay",51] ,["Saroj", 47],["Mayank",22]] #list of list

for  name, age in list2:
    print(name, "is", age, "year old")
tp = ("Srishtee","Vinay","Saroj","Mayank")
for family in tp:
    print(family, "is family")

dictionary = dict(list2)
print("fetch dictionary")
for name, age in dictionary.items():
    print(name, age)
for item in dictionary:
    print(item)
for  name, age in list2:
    if age>40:
        print(name)
#Quiz:
print("print a number from the item from the list which is number and greater then  6")
list3 = ["22", 333, 4,"test"]

for number in list3:
    if type(number)== int and number>6:
        print(number)

