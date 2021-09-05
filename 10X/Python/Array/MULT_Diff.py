'''
Diff Prod
Description
Given an array of integers, your task is to write a program that finds the product of maximum and minimum
 difference between any two numbers in the given array. Print NA if it does not exist.

Note: This is a functional problem. Try to complete the functions, so that the task can be completed.

Input format
First line contains t, the no of test cases.

First line of each test case contains N, the length of the given array.
The next line contain N space separated integers, denoting the elements of the array.
Output format
One line for each test, a integer denoting the result.

Sample input
3
6
12 35 1 10 34 1
3
10 5 12
1
10
Sample output
0
14
NA
Explanation
For the array [12 35 1 10 34 1], max_diff = 35-1 = 34; min_diff = 1-1=0; Hence the product is 34x0 = 0
Similarly, For the array [10 5 12], max_diff = 12-5 = 7; min_diff = 2=0; Hence the product is 7x2 = 0
And for the last array, it does't exist.
'''
def minDiff(arr, arr_size):
    mi=max(arr)
    for i in range(0,arr_size):
        for j in range(0,arr_size):
          if (i!=j)and (abs(arr[i]-arr[j])<mi):
                mi=abs(arr[i]-arr[j])
    return mi
def maxDiff(arr, arr_size):
	return max(arr)-min(arr)

def prodDiff(arr, arr_size):
	### Complete this and the above functions!
    if (arr_size==1):
        return "NA"
    else:
        return minDiff(arr, arr_size)*maxDiff(arr, arr_size)

for _ in range(int(input())):
    length = int(input())
    arr = [int(x) for x in input().split()]
    print(prodDiff(arr, length))
# 60% getting..
# link=---   https://6793fdf6.widgets.sphere-engine.com/lp?hash=cdRZFGs6Rq