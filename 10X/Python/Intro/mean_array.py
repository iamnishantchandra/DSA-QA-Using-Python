import array
sum=0
mean=0
count=int(input())
arr = list(input().split())
for i in range(0,count):
    arr[i]=int(arr[i])
    sum=sum+arr[i]
mean=sum/count
print(mean)
    