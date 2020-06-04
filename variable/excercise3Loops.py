# take any number, guess the number user input and guess that the number is greater

number = 18
print("enter the number")

inc = 1
while(inc<=5):
    userinput = input()
    if int(userinput)>18:
            print("Number is  greater")
    elif int(userinput)<18:
            print("Number is smaller")

    elif int(userinput)==18:
        print("Congratulation you won")
        print("You guess the number on", inc, " time")
        break
        if inc==5:
            print("Your chance is over")
        break
    inc = inc+1;

