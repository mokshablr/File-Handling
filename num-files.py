import os
print('''Enter the number corresponding to the function:
1. Count number of files given a parameter
0. Exit''')
choice=int(input('Enter your choice:'))
    
def num_files(dir, sub):
    ctr=0

    for filename in os.listdir(dir):
        f= os.path.join(dir,filename)
        if os.path.isfile(f):
            if f.endswith(sub):
                ctr+=1

    print(f"Number of {sub} files:",ctr)

if choice==1:
    dir=input("Enter directory path: ")
    sub=input('Enter file type: (Eg: "py","jpg")')
    num_files(dir, sub)    
    