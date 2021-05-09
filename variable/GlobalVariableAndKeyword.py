#we cannot change the value of global variable in function, so for that we need global keyword to change global variable
globalvar = 5

def function1(n):
    local = 5
    global globalvar
    globalvar = globalvar + 10
    print(local,globalvar, n )

function1("Done")

print(globalvar)

#x = 88 if we write function under function and make global x for the inner function it will check the upper function it will check global part
# if that is not there it will print value of x for its.
def outerfunc():
    x = 20
    def innerfunc():
        global x
        x= 55
        print("inner function", x)
    innerfunc()
    print("outer function", x)

outerfunc()