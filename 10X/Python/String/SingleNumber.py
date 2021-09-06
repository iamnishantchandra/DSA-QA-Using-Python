'''
Single Number
Given a list of N integers, every element appears twice except for one. Find that single one.

Input
First number is N (the number of integers given) Followed by the N numbers

Output
One line containing the output integer

Example
Input: 3

2

2

1

Output: 1

Input: 5

2

2

1

1

3

Output: 3
'''
# Single Number
'''
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
only-50%
'''
n=int(input())
a=[]
Count=2

for j in range(n):
   a.append(int(input()))
a=sorted(a)
p=a[0]
f=False
for i in range(n-1):
    if a[i]!=a[i-1] and a[i]!=a[i+1]:
        p=a[i]
        f=True
        break
if f:
    print(p)
else:
    print(a[n-1])
