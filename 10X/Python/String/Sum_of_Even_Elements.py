n=int(input())
count=0
a=input().split()
for i in range(n):
    if(int(a[i])%2==0):
        count+=int(a[i])
    else:
        pass
print(count)