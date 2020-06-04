 #dictionary is key value pair
d1= {}
print(type(d1))
d2 = {"Goal1":"Python","Goal2":"SQL","Goal3": {"A":"Manual Testing","B":"Automation Testing","C":"Java"}}
#value could be anything dictionary, list or tuple, keys should be immutable
print(d2["Goal1"])
print(d2["Goal3"])
print(d2["Goal3"]["B"])
d2["Goal4"] = "API postman" #can add more values, so key should be either number or string
d2[22] = "API automation"
print(d2)
del d2["Goal2"] #to remove any number
print(d2)
d3 =d2 #d3 is pointing to d2 but it is not copying d2 so if I remove or add any value in d2 it would also reflect in d3
d2["Goal5"]="Database Testing"
print(d2)
print(d3)
#but when we use copy function and copy the values of d2 in d3 then if you change something in d2 won't rrflect in d3
d3 =d2.copy()
d2["Goal6"]="Microservice Testing"
print("copy function")
print(d2)
print(d3)

d2.update({"Goal7" : "AWS"})
print(d2)
print(d2.keys())
print(d2.items())

