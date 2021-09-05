'''
Noble Integer
Given a list of integers A, find if an integer P exists in the list such that the number of integers 
greater than P in the list equals P.

Input
N number of elements in the list (N >= 2).

N lines each line representing a single interger in the list

Output
1 if such integer exists

-1 if no such integer exists

Example
Input:

4

3

2

1

3

Output:

1

Here number of elements greater than 2 is 2.
'''
n=int(input())
lis=[]
for i in range(n):
    lis.append(int(input()))
pre=lis[0]
count=0
for i in range(n):
    if pre<lis[i]:
        count+=1
        if



