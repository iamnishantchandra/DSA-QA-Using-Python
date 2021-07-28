n,k=map(int,input().split())
a=input().split()
s=0
for i in range(n):
    if int(a[i])==0:
        pass
    elif (int(a[i])%k==0):
        s+=1
print(s)
