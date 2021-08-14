"""
Good Pairs
Given an array of integers nums (length of nums > 1).

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs.

Input
Single line containing a list of numbers separated by spaces

Output
Single integer representing total number of good pairs

Example
Input:

1 2 3 1 1 3

Output:

4

Explanation:
(0,3), (0,4), (3,4), (2,5) index position elements

"""
from typing import Counter


a=list(map(int,input().split()))
count=0
for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j] and i < j:
            count+=1
print(count)
