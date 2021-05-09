#decorate use to modify function functionality
def function1():
    print("I will make my own youtube channel soon")
func2 = function1

del function1
func2() # we already copied

def newfunc(num):
    if num == 0:
        return print
    if num !=0:
        return sum
a = newfunc(3) # you will get class
print(a)

#function as an argument
def funcarg(func2):
    func2("this")

funcarg(print)

#decortor
def dec1(func1):
    print("Execute now")
    func1()
    print("Executed")
    return funcarg
#first way to decorate
@dec1
def calling_function():
    print("this will be copied")
#second way to decorate
copied = dec1(calling_function)
calling_function()
