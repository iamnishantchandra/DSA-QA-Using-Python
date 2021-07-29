# Matrix 101
n,m=map(int,input().split())
a=[]
s=0
for i in range(n):
    a=list(map(int,input().split()))
    for j in range(m):
        if(a[j]%2!=0):
            s+=a[j]
print(s)      

