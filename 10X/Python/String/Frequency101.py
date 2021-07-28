n,k=map(int,input().split())
a=input().split()
s=0
for i in range(n):
    if int(a[i])==k:
        s+=1
print(s)
