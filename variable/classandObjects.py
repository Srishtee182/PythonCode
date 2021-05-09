class student:
    board = "CBSE"

obj1 = student()
obj2 = student()

obj1.name = "Srishtee"
obj1.std = 12
obj1.sub = ["python", "Java", "SQL", "Selenium"]
obj2.name = "Mayank"
obj2.std = 10
obj2.sub = ["Digital marketing", "BPO", "Reports making"]

print("Obj1 and obj2 have different location in memory", obj2, obj1)

print(obj2.sub, obj1.sub,"\n")
print("Class template", obj1.board, obj2.board,student.board,"\n")

student.board = "UP"
print("Class template changed", obj1.board, obj2.board)

obj1.board = "Gujarat" #instance variable

print("Class template", obj1.board, obj2.board,student.board,"\n")

print("obj1 disc", obj1.__dict__)
