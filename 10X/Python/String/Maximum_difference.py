n=int(input())
a=input().split()
temp=0
min=int(a[1])
max=int(a[1])
for i in range(n):
    temp=int(a[i])
    if temp>=max:
        max=temp
    elif temp<=min:
        min=temp
print(max-min)
