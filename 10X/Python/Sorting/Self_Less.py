'''
Self-Less
Given an array nums of n integers where n > 0, print an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

If the array has only 1 element, print 1 as result.

Note:
Please solve it without division and in O(n).
Elements of the array can be zero 0 as well.
Input Format
First line denotes the number of testcases.

First line of each testcase denotes the size of the array nums.
The next line contains the n elements as space seperated integers.
Output Format
One line for each testcase, denoting the result array as space-seperated integers.

Sample Input
1
4
1 2 3 4
Sample Output
24 12 8 6
'''

for _ in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    la=[1]*n
    ra=[1]*n
    for i in range(1,len(arr)):
        la[i]=(arr[i-1]*la[i-1])
    for i in range(len(arr)-2,-1,-1):
        ra[i]=(ra[i+1]*arr[i+1])
    for i in range(len(arr)):
        arr[i]=int(ra[i]*la[i])
    print(*arr)