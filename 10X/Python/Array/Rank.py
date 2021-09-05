'''
Rank
Description
You have been given the scores of n people. You need to find the rank of the given array.

Here, the rank of the given array is defined as: sum of the elements of the subarray, having the maximum sum.

Input format
First line contains t, the no of test cases. First line of each test case contains N, the length of the given array (number of people). The next N line contain space separated integers, denoting the elements of the array (each element is the score of a person).

Output format
One line for each test, a integer denoting the result (rank).

Sample input
3
6
12 35 1 10 34 -1
3
10 5 12
1
10
Sample output
92
27
10
Explanation
For the array [12 35 1 10 34 -1], subarray having maximum sum is [12 35 1 10 34].

For rest of them, the whole array, is the desired subarray. 

'''
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in range(len(arr)):
        if arr[i]>0:
            count+=arr[i]
    print(count)

#####  wrong Answer  #####