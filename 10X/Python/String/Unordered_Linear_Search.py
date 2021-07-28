

k=int(input())
n=int(input())
a=[]
for i in range(n):
    b=int(input())
    a.append(b)
for j in range(n):
    if a[j]==k:
        s=j
        break
    else:
        s=-1
print(s)
