import time

#to know the execution time of program, it have the time function which give no. of tick
initial = time.time()
# basically while and forloop run at same time
k=0
while(k<10):
    print("THis is Srishtee")
    k+=1
print("While loop time", time.time() - initial, " Seconds")
initial2 = time.time() # to reset time

for i in range(10):
    print("THis is Srishtee")
#    time.sleep(2) wait for 2 second same as thread.sleep
print("For loop time", time.time() - initial2, " Seconds")

localtime = time.asctime()
localtime2 = time.asctime(time.localtime(time.time()))#time.time return ticks from some particcular time, time.localtime convert it into local time and asc time convert it into presentable time
print(localtime)
print(localtime2)