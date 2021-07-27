n=int(input())

for i in range(n):
    a=int(input())
    f=True
    for i in range(2,(int(a/2)+1)):
        
        if(a%i==0 and a>2):
            f=False
            break
    if f:
           print("Yes")
    else:
          print("No")