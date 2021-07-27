n,k=map(int,input().split())
temp=0
if(n>=k):
    a=(input().split())

    temp=a[k-1]
    a[k-1]=a[n-k]
    a[n-k]=temp

for i in range(0,len(a)):
    print(a[i],end=" ")
