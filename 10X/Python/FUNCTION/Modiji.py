'''
Modiji
Modiji wants to estimate the fund that can be gathered in a month, if he applies a special rule for the funding of covid patients treatments. As per the rule, everyone should pay ceil(7% of their monthly salary) to this scheme.

Given a positive integer n. And the monthly salary of these n people. Help modiji find the fund that can be gathered in a month, through this scheme.

Write a function to do this calculation.

Input
First line contains one integer, denoting n. The next line contains n space seperated integers, denoting the monthly salary of the n people.

Output
One Integer, denoting the result.

Example
Input1:

5
100 200 300 400 555
Output1:

113

'''
import math
n=int(input())
incom=list(input().split())
su=0
for i  in range(n):
    su+=math.ceil((int(incom[i])*.07))
print(su)
