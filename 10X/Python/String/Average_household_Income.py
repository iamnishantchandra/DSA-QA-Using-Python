n=int(input())
a=[]
sum=0
count=0
for i in range(2*n):
    a.append(int(input()))
for j in range(n):
    if (a[j+n]>2):
        count+=1
        sum+=a[j]
if(count==0):
    print(-1)
else:
    print(int(sum/count))