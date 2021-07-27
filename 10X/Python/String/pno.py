n=int(input())
f=True
for i in range(n):
    a=int(input())
    for i in range(2,int(a//2)+1):
        if(a<2):
          print("No")
        elif (a%i==0):
        	print("No")
        	break
        else:
          print("Yes")