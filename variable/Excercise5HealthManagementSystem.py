# harry rohan hamad - client
# total 6 file to log food and exercise

print("Welcome to health management system, please enter the name of client for whom you want to log data")
print("Option: harry rohan hamad")

def client():
    name = input()
    return name

clients = client()

def log():
    print("diet or excercise")
    log = input()
    return log
def getdate():
    import datetime
    return datetime.datetime.now()
date = getdate()
log = log()
if clients =="harry":
    print("What you want to log for harry? diet or excercise")
    if log == "excercise":
        f=open("files//harryexcercise","a")
        print("Enter excercise")
        ex=  input()
        f.write(str([str(date)])+ "  "+ex+"\n")
    elif log == "diet":
        f = open("files//harrydiet.txt", "a")
        print("Enter Diet")
        d=  input()
        f.write(str([str(date)])+ "  "+d+"\n")
elif clients == "rohan":
    print("What you want to log for rohan? diet or excercise")
    if log == "excercise":
        f=open("files//rohanexcercise","a")
        print("Enter excercise")
        ex=  input()
        f.write(str([str(date)])+ "  "+ex+"\n")
    elif log == "diet":
        f = open("files//rohandiet", "a")
        print("Enter Diet")
        d=  input()
        f.write(str([str(date)])+ "  "+d+"\n")
elif clients == "hamad":
    print("What you want to log for hamad? diet or excercise")
    if log == "excercise":
        f=open("files//hamadexcercise","a")
        print("Enter excercise")
        ex=  input()
        f.write(str([str(date)])+ "  "+ex+"\n")
    elif log == "diet":
        f = open("files//hamaddiet.txt", "a")
        print("Enter Diet")
        d=  input()
        f.write(str([str(date)])+ "  "+d+"\n")

exit()