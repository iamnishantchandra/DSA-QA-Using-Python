# Single Number
n=int(input())
a=[]
Count=2
p=0
for i in range(n):
   a.append(int(input()))
for k in a:
    for j in a:
        temp=a[k]
        if a[k]==a[j]:
            Count-=1
            if Count==0:
                p=a[k]
                break

print(p)   
