'''
Noble Integer
Given a list of integers A, find if an integer P exists in the list such that the number of integers greater than P in the list equals P.

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
def nobel(arr):
    if len(arr)<2:
        return -1

    j=len(arr)-2
    count=1
    while j>=0:
        if arr[j]==count and arr[j]!=arr[j+1]:
            return 1
        j-=1
        count+=1
    return -1

arr=[int(input()) for _ in range(int(input()))]
arr.sort()
print(nobel(arr))