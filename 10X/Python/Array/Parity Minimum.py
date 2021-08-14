'''
Parity Minimum
Description
Given an array of length n which contains only positive integers, let S be the sum of the digits of the 
minimal element of the array.
Return 0 if S is odd, otherwise return 1.

Input format
First line contains a positive integer n, which denotes the number of elements in the array. This is 
followed by n lines each containing one integer denoting one element of the array.

Output format
One line which is 0 or 1.

Sample input
4
34
23
1
24
Sample output
0
Explanation
First line is 4, i.e. 4 elements in the array. Minimum element of the array is 1. Sum of digits of 1 is 
1 and as it is odd, the output is 0

Sample input
2
33
44
Sample output
1
Explanation
First line is 2, i.e. 2 elements in the array. Minimum element of the array is 33. Sum of digits of 33 
is 6 and as it is even, the output is 1
'''
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
mi=min(a)
su=0
for i in str(mi):
    su+=int(i)
if su%2==0:
    print(1)
else:
    print(0)