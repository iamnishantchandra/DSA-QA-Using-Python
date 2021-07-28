"""

n=int(input())
count=0
a=input().split()
for i in range(n):
    count=count+(int(a[i]))
    i+=1
    
print(count)
"""

"""
n=int(input())
count=0
a=input().split()
i=0
while(i<n):
    count=count+(int(a[i]))
    i+=2
    
print(count)

"""
n=int(input())
a=input().split()
s=0
for i in range(n):
    if i%2==0:
        s=s+int(a[i])
print(s)