import os
dir=input("Enter directory path: ")
ctr=0

for filename in os.listdir(dir):
    f= os.path.join(dir,filename)
    if os.path.isfile(f):
        if f[-3:len(f)+1]==".py":
            ctr+=1

print("Number of python files:",ctr)
