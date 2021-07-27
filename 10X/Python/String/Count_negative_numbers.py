n=int(input())
count=0
a=input().split()
for i in range(n):
    if(int(a[i])<0):
        count+=1
    else:
        pass
print(count)