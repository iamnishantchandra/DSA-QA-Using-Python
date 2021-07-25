n=int(input())
while(n>0):
    if(n%3==0 and n>=3):
        n//3
    elif(n % 3!=0):
        print(False)
    else:
        print(True)
