#recursion means using funtion inside funtion

def print2(str):
    #print2(str) this is recursion if I will run this it will give an error "Recursion depth exceed"
    print("This is "+str)

print2("Srishtee")

def factorial(n): #itterative
    total = 1;
    for i in range(n):
        total= total*(i+1);
    print(total)
    return total;

def factorial_reccursive(n):
    if n==1:
        return 1;
    else:
        return n * factorial_reccursive(n-1)

number = int(input("Enter the number"));
factorial(number)
num=factorial_reccursive(number)
print(num)

def fibonaci_recursive(n): #itterative
    if n==1:
        return 1
    else:
        return n + fibonaci_recursive(n-1)
print(fibonaci_recursive(5))