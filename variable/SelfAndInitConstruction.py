class student:
    board = "CBSE"
    def __init__(self, name, std, sub): #python constructor
        self.name = name
        self.std = std
        self.sub = sub
    def printdetail(self): #self is the instance where this funtion is getting implement, if self have arg it will not get printed
        return f"Name is {self.name}, std is {self.std}"
#obj1 = student()
#obj2 = student()

# obj1.name = "Srishtee"
# obj1.std = 12
# obj1.sub = ["python", "Java", "SQL", "Selenium"]
# obj2.name = "Mayank"
# obj2.std = 10
# obj2.sub = ["Digital marketing", "BPO", "Reports making"]
#
# print(obj1.printdetail())

obj3 = student("nistha", "8", ["social science", "science","math"])
print(obj3.sub) 