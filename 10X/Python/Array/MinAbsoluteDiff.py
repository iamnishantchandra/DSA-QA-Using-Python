'''
Min Absolute Diff
Given a list find the minimum absolute difference between any to elements.

Input
First line is N Then follows a line consisting of N numbers. (N >= 2)

Output
Print a single number the min difference.

Example
Input:

4

5 2 1 3

Output: 1
'''
'''

n=int(input())
b=list(map(int,input().split()))
mi=abs(b[0]-b[1])
for i in range(n):
    for j in range(n):
        if i!=j:
            su=abs(b[i]-b[j])
            if mi>su:
                mi=su
print(mi)
problem- more time complexity
'''
'''
n=int(input())
b=list(map(int,input().split()))
b=sorted(b)
mi=abs(b[0]-b[1])
for i in range(1,n):
    temp=b[i-1]
    j=i
    while (temp<=(b[j]+mi)) and j<(n-1):
        su=abs(temp-b[i])
        if mi>su:
            mi=su
        j=j+1
print(mi)
problem- more time complexity
'''
n=int(input())
b=list(map(int,input().split()))
b=sorted(b)
mi=abs(b[0]-b[1])
for i in range(1,n):
    sub=abs(b[i]-b[i-1])
    if mi>sub:
        mi=sub
print(mi)
