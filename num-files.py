import os
print('''Enter the number corresponding to the function:
1. Count number of files given a parameter
2. Delete files in a directory
0. Exit''')
choice=int(input('Enter your choice: '))
dir=input("Enter directory path: ")
    
def num_files(sub):
    ctr=0

    for filename in os.listdir(dir):
        f= os.path.join(dir,filename)
        if os.path.isfile(f):
            if f.endswith(sub):
                ctr+=1

    print(f"Number of {sub} files:",ctr)

def del_files():
    print('''1. Delete based on file-type(Eg:".py", ".jpg")
0.Exit \n''')
    c=int(input("Enter your choice: "))
    if c==1:
        ctr=0
        sub=input('Enter file-type(Eg:".py", ".jpg): ')
        for filename in os.listdir(dir):
            f= os.path.join(dir,filename)
            if os.path.isfile(f):
                if f.endswith(sub):
                    os.remove(f)
                    ctr+=1
        print(ctr, "files have been deleted.")

if choice==0:
    exit()

elif choice==1:
    sub=input('Enter file type: (Eg: "py","jpg")')
    num_files(sub)

elif choice==2:
    del_files()