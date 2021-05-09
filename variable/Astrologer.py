#pattern prining

print("Enter a number")
input1 = int(input())
print("Enter a yes(1) or no(0)")
input2 = int(input())
if input2==1:
    for i in range(0,input1):
        for j in range(0,i+1):
            print("* ",end='')
        print()
elif input2==0:
    for i in range(0,input1):
        for j in range(0,input1-i):
            print("* ",end='')
        print()


