#while loop break and continue

#take input from user till the input is not greater then 100
while(True):
    print("give a number")
    i= int(input())
    if i>=100:
           print("done with the program")
           break

j = 10
while j<20:
    if j>13:
        continue # execute this condition and return to loop
    print(j)
    j = j + 1
    if i==15:
        break # break the current execution

exit()
