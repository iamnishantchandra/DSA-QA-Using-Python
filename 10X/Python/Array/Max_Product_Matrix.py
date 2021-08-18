'''
MAX product
You are given two array A and B. You have to select two integers, one from A and one from B. Let them me A[i] (0<=i< length of array A) and B[j] (0<=j< length of array B). you have to find the maximum value of |A[i]XB[j]|.

note:- |x| is absolute value of x.

Input
first line contains the size of the array A which is followed by size of array B in line two. Next two lines contain the two arrays A,B.

1<=length of A,B<=10^5

-10^9< A[i],B[j]< 10^9

Output
Print the maximum value of |A[i]XB[j]|

Example
Input:

5

8

-3 4 5 2 1

7 4 2 4 5 3 -10 6

Output:

50

explanation

choose 5 from first A and -10 from B, the product is -50 whose absolute value is 50(max)
'''
'''
for i in range(n):
    nar[i]=abs(nar[i])
for j in range(m):
    mar[i]=abs(mar[i])
'''
'''
n=int(input())
m=int(input())
nar=[abs(int(x)) for x in input().split()]
mar=[abs(int(x)) for x in input().split()]
print(int(max(nar)*max(mar)))
'''
n=int(input())
m=int(input())
print(int(max([abs(int(x)) for x in input().split()])*max([abs(int(x)) for x in input().split()])))