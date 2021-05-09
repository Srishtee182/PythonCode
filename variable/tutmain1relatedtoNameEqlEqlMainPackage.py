def printxyz(string):
    return (f"This is {string}")

def defwrongadd(num1, num2):
    return (f"this is wrong answer of {num1} and {num2} ", num1+num2+5)
# if you will import like this then it will take the all contain related to the function so to avoid
# it we need to create main funtion
print("And the name is", __name__)#here it will show main and in other file it will show the class name
if __name__ == '__main__':
#IndentationError: expected an indented block, this error will occur if you will not keep the content in it with one tab gap
    print(printxyz("Srishtee"))
    additon = defwrongadd(2, 3)
    print(additon)
