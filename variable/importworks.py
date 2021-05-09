#import sklearn as sk
import sys
from sklearn.ensemble import RandomForestClassifier
print(RandomForestClassifier())
#print(sk.__version__)

print(sys.path)

#make another file and import content of file2 in file1
#from file2 import a
#print(file2.a) this is a good practice so that we can avoid ambiquity if we have 2 files imported and both have a this will help
#file2.printjoke("This is a argument of funtion contains file2")

#why not to keep the file name on the name of module or keyword because then if you import module somewhere of that name it will go and find things on that file which will make you in trouble
