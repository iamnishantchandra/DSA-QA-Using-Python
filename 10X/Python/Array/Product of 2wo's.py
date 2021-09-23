'''
Product of 2wo's
Given an array of integers. Find the sum of absolute values of product of twos of the array. More specifically, 
for an array a1,a2,a3.....an, the sum of absolute values of all the pairs in an array is defined as

SUM(| ai * aj |), for all 1<=i,j<=n such that i != j

ex- for arr= a1,a2,a3 -> | a1 x a2 | + | a1 x a3 | + | a2 x a3 |

Note- |x| stands for absolute value of x.

Contraints
1<= length of array<= 1000000

Input
first line of the input contains N, representing the size of the array. the second line contains the N 
space separated elements of the array.

Output
finally print the sum of absolute values of all the pairs in the array.

Example
Input:

3

1 2 -3

Output:

11

Explanation:

|1 x 2| + |1 x -3| + |2 x -3|

= 2 + 3 + 6

=11
'''
# def mult():
#     if 
# n=int(input())
# a=list(map(int,input().split()))
# print(mult(a))
####################################################
n=int(input())
a=list(map(int,input().split()))
su=0

for i in range(len(a)):
    for j in range(i):
        # if i!=j:
            su+=abs((a[i]*a[j]))
print(su)
###################################################
# n=int(input())
# a=list(map(int,input().split()))
# su=0
# i=0
# j=1
# while i<(len(a)) and j<(len(a)):
#     if j==len(a)-1:
#         i+=1
#         j+=i
#     su=abs((a[i]*a[j]))
#     j+=1
