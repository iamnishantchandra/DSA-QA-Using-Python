'''
Ranger Product
Power Rangers S.P.D. is the thirteenth season of the American television series, Power Rangers. The Red ranger defines the ranger product as:

An array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Red ranger asks blue ranger:

Given an array nums of n integers where n > 0, print the ranger product array as space seperated values.

If the array has only 1 element, print 1 as result.

Being the friend of Blue ranger, can you help him to solve this?

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
1 2 3 4
Sample Output
24 12 8 6

'''
def RangerProduct(arr):
    rp=[1]*len(arr)
    lp=[1]*len(arr)
    rs=[]
    for i in range(1,len(arr)):
        lp[i]=lp[i-1]*arr[i-1]

    for i in range(len(arr)-2,-1,-1):
        rp[i]=rp[i+1]*arr[i+1]
    
    for i in range(len(arr)):
        rs.append(rp[i]*lp[i])
    return rs


for _ in range(int(input())):
    n=int(input())
    arr=[int(x) for x in input().split()]
    print(*RangerProduct(arr))