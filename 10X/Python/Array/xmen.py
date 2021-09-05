'''
X-Man
Description
You have been given the scores of n people. You need to find the number of x-mans amongst those n people.

A given person is said to be x-man, if his/her score is greater than the average score amongst those n people.

Note: Scores can be negative as well, since there was negative marking as well.

Input format
First line contains t, the no of test cases. First line of each test case contains N, the length of the given array (number of people). The next N line contain space separated integers, denoting the elements of the array (each element is the score of a person).

Output format
One line for each test, a integer denoting the result (number of x-man).

Sample input
3
6
12 35 1 10 34 1
3
10 5 12
1
10
Sample output
2
2
0
Explanation
For the array [12 35 1 10 34 1], avg = 15.5, so 35 and 34 are greater than average.
Similarly for second testcase, avg = 9.0, so 10 and 12 are greater than result.
And for the 3rd testcase, average is 10.0 , so no elements are greater than 10.0

'''

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    avg=sum(arr)/len(arr)
    for i in range(len(arr)):
        if arr[i]>avg:
            count+=1
    print(count)
         



for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    count=0
    for i in range(len(arr)):
        if arr[i]>0:
            count+=arr[i]
    print(count)
         