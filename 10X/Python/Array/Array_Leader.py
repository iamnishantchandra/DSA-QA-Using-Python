'''
Array_Leader
Given an integer array A containing N distinct integers, you have to find all the leaders in the array A.

An element is leader if it is strictly greater than all the elements to its right side.

NOTE:
The rightmost element is always a leader.

Problem Constraints:
1 <= N <= 10^5
1 <= A[i] <= 10^8
Input
First line denotes n, the size of the array. The next n lines contains the elements of the array.

Output
Return an integer array denoting all the leader elements of the array. (You need to print one element in one line & The sequence of the resultant array should be in the reverse order, in which they appear in the given array.)

Example
Input: 6

16

17

4

3

5

2

Output:

2

5

17

Explanation:
Element 17 is strictly greater than all the elements on the right side to it.

Element 2 is strictly greater than all the elements on the right side to it.

Element 5 is strictly greater than all the elements on the right side to it.

So we will return this three elements i.e [2, 5, 17] as the required ordering.
'''
arr=[int(input()) for _ in range(int(input()))]
j=len(arr)
ma=arr[len(arr)-1]
a=[]
a.append(ma)
while j>0 and len(arr)>1:
    j-=1
    if arr[j]>ma:
        ma=arr[j]
        a.append(ma)
[print(i) for i in a]