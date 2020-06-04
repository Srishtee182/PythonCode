num1= input()
num2 = input()

try:
    print("please add this two number",int(num1)+int(num2))
except Exception as e:
    print(e)

print("No matter what print this")