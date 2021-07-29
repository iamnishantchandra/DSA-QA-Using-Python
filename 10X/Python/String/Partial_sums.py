# Partial sums
n,k=map(int,input().split())
a=input().split()
s=0
f=False
for i in range(n):
    s+=int(a[i])
for i in range(n):
    if (s-int(a[i]))==k:
        f=True
        break
if f:
    print(1)
else:
    print(0)


'''
if int(a[i])==0:
        pass
    elif (int(a[i])%k==0):
        s+=int(a[i])
'''