a= 9
b = 12
#built in function sum
print(sum((a,b)))
#user define function
def func1(a,b):
    print("hello built in function", a+b)

def func2(a,b):
    #docstrings: this is the comment line statement added inside the function which tells about it,and you can print it
    """This is the which calculate the average of two number"""
    average=(a+b)/2
    print(average)
    return average
func1(a,b)
v=func2(a,b)
print(func2.__doc__)
print(v)