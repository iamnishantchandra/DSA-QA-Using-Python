'''
Rotate Array Clockwise
Write a function which takes a list L and a postive integer M and returns a list which is rotated clockwise M times.

Input
L List of numbers separated by spaces

M in a single line

Output
A list which is a representation of L rotated M times.

Example
Input:

2 1 3 4 5 10

1

Output:

1

3

4

5

10

2


'''
lis=list(map(int,input().split()))
n=int(input())
for i in range(n):
    temp=lis[0]
    del lis[0]
    lis.append(temp)
for j in lis:
    print(j)