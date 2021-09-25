# def getdate():
#     import datetime
#     return datetime.datetime.now()

import datetime
def gettime():
    return datetime.datetime.now()

def take(k):
    if k==1:
        c=input("Enter 1 for exercise and 2 for food : \n")
        if(c==1):
            value=input("Type here for exercise:\n")
            with open("Manish-exercise.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("Query Enetred Succesfully")
        elif (c==2):
            value=input("Type here for Food:\n")
            with open("Manish-Food.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("Query Enetred Succesfully")
    elif (k==2):
        c=input("Enter 1 foor exercise and 2 for food : \n")
        if c==1:
            value=input("Type here for exercise:\n")
            with open("Rahul-exercise.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("Query Enetred Succesfully")
        elif (c==2):
            value=input("Type here for Food:\n")
            with open("Rahul-Food.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("Query Enetred Succesfully")
    elif (k==3):
        c=input("Enter 1 foor exercise and 2 for food : \n")
        if (c==1):
            value=input("Type here for exercise:\n")
            with open("Kamal-exercise.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("Query Enetred Succesfully")
        elif (c==2):
            value=input("Type here for Food:\n")
            with open("Kamal-Food.txt","a") as op:
                op.write(str([str(gettime())])+":"+value+"\n")
            print("Query Enetred Succesfully")
    else:
        print("Enter the Valid detail")

def retrive(k):
    if k==1:
        c=int(input("Enter 1 for Execise and 2 for food"))
        if c==1:
            with open("Manish-exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("Manish-Food") as op:
                for i in op:
                    print(i,end="")
    elif k==2:
        c=int(input("Enter 1 for Execise and 2 for food"))
        if c==1:
            with open("Rahul-exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("Rahul-Food") as op:
                for i in op:
                    print(i,end="")
    elif k==3:
        c=int(input("Enter 1 for Execise and 2 for food"))
        if c==1:
            with open("Kamal-exercise.txt") as op:
                for i in op:
                    print(i,end="")
        elif c==2:
            with open("Kamal-Food") as op:
                for i in op:
                    print(i,end="")
    else:
        print("Enter Valid Information\n")

print("Project of Health Management System\n")
a=int(input("Enter 1 for log and 2 for Retrive : \n"))

if a==1:
    b=int(input("Enter the 1 for Manish 2 for Rohan and 3 for kamal"))
    take(b)
else:
    b=(int(input("Enter the 1 for Manish 2 for Rohan and 3 for kamal")))
    retrive(b)



