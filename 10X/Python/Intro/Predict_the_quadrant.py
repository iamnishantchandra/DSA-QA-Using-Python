count=int(input())
for i in range(0,count):
    x,y=input().split()
    x=int(x)
    y=int(y)
    #y=int(input())
    if (x > 0 and y > 0):
        print("Q1")
    elif (x < 0 and y > 0):
        print("Q2")
    elif (x < 0 and y < 0):
        print("Q3")
    else :
        print("Q4")