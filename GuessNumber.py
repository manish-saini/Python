Win=45
num=10
for i in range(1,num):
    n=int(input("Enter the number : "))
    if(n==Win):
        print("Win Bro")
        break
    elif n>42 and n<46:
        print("u are to close")
    elif n>Win:
        print("Choose Smaller Number")
    elif n<Win:
        print("Choose Greater number")
    else:
        print("U Loss the Game")
    num=num-1
    print("Number of Count Left : ",num)
