'''
Sorted_Square
Given an array of integers A, return an array of the squares of each number, in sorted non-decreasing order.

Input
First Line contains an integer n, denoting the size of array A. The next n lines contains n elements of the array A.

Output
n lines, Each line containing 1 element of the array A in the above mentioned order.

Example
Input:

5

-4

-1

0

3

10

Output:

0

1

9

16

100

Note:
1 <= A.length <= 10000
-10000 <= A[i] <= 10000
'''
"""
n=int(input())
d=[(int(x)**2) for x in input().split()]
for i in range(len(d)):
    for j in range(len(d)):
        if d[i]<d[j]:
            d[j],d[i]=d[i],d[j]
print(d)

"""
"""
n=int(input())
d=[(int(input())**2) for i in range(n)]
for i in range(len(d)):
    for j in range(len(d)):
        if d[i]<d[j]:
            d[j],d[i]=d[i],d[j]
[print(x) for x in d]
"""
n=int(input())
d=[(int(input())**2) for i in range(n)]
d.sort()
[print(x) for x in d]