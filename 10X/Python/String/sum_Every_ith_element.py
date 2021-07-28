n=int(input())
a=[]
sum=0
for i in range(n):
    a.append(int(input()))
k=int(input())
for j in range(0,n,k):
    sum+=a[j]

print(sum)