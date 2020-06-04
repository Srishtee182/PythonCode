#create a faulty calculator, 45*3=555, 56+9=77, 56/6=4
print("enter 1st numbers")
a=  int(input())
print("enter 2st numbers")
b=  int(input())
print("enter operation you like to perform (+, - ,* ,+)")
c = input()
if a==45 and b==3 and c=="*":
    print(555)
elif c=="*":
    print(a*b)
if a==56 and b==9 and c=="+":
    print(77)
elif c == "+":
    print(a + b)
if a == 56 and b == 6 and c == "/":
    print(4)
elif c == "/":
    print(a / b)
elif c == "-":
    print(a - b)
else:
    print("Invalid number")