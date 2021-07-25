"""
n=int(input())
sum=0
for i in range(n+1):
    sum=sum+(i*((-1)**i))
print(sum)



n=int(input())
sum=0
a=1
while(a<(n+1)):
    sum=sum+(a*((-1)**a))
    a=a+1
print(sum)

"""
n=int(input())
if(n%2==0):
    print(n//2)
else:
    print(-((n//2)+1))


A,B=map(int,input().split())
if (A*B)%2==0:
    print("No")
else:
    print("Yes")
