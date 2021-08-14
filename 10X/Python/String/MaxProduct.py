'''
Maximum Product
link https://6793fdf6.widgets.sphere-engine.com/lp?hash=atbecI0dwg
You are given a list of integers. Find the maximum product that can be obtained from multiplying adjacent integers in the list.

Input
First line contains n, indicating the number of elements in the list, 2 <= n <= 10

This is followed by n lines each containing an integer

Output
One integer indicating the maximum product achievable from adjacent elements of the list

Example
Input:

4

1

3

4

10

Output:

40

Explination:

First line of input contains 4 indicating there are 4 elements in the list

The next four lines contain the elements of the list: 1,3,4,10

The possible products we can obtains is 1x3=3, 3x4=12, 4x10=40 where 40 is the maximum


'''
n=int(input())
a=[]

for i in range(n):
    a.append(int(input()))
ma=a[0]
if n>1:
    for j in range(1,n):
        if ma<int(a[j-1]*a[j]):
            ma=int(a[j-1]*a[j])
    print(ma)
elif n==0:
    print(0)
else:
    print(ma)