#create dictionary take input from user and return the meaning from it.

dictionary = {"beneficiaries":"a person who derives advantage from something, especially a trust, will, or life insurance policy","dissemination":"the action or fact of spreading something, especially information, widely."
              ,"vested":"entrust to","propaganda":"information"}
print("which word you like to search")
search = input()
print(dictionary.__getitem__(search))