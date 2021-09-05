'''
Round
Description
Given an array of n integers, You need to find the round array (this will be of size n-1).

Here, round array is defined as:

round[i] = round(arr[i+1]/arr[i]) , where 0 <= i < length of array-1
If any element of round doesn't exist, (due to any boundary case or any other reason) , print -1 only, as the output of that particular testcase.

Note: round() function rounds off the float number to the nearest integer.

More examples about round() function:

round(1)   = 1
round(1.3) = 1
round(7.8) = 8
round(0.5) = 0
round(4.5) = 4
Input format
First line contains t, the no of test cases.

First line of each test case contains N, the length of the given array.
The next line contain N space separated integers, denoting the elements of the array.
Output format
One line for each test, containing space seperated values from the result.

Sample input
4
6
12 35 1 10 34 1
3
10 5 12
1
10
5
1 2 3 4 0
Sample output
3 0 10 3 0
0 2
-1
-1
'''
def round():
    if

tc=int(input())

for i in range(tc):
    n=int(input())
    ar=[int(x) for x in input().split()]
    for i in range(n):
