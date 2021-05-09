li = ["House", "support", "willpower", "God"]
i = 1
for item in li:
    if i%2 is 0:
        print(item)
    i+=1

for index, item2 in enumerate(li): #this will return index and item both
    if index%2==0:
        print(item2)