'''
maximum number of submissions: 10
Max distance
You are given an array of integers. The distance between any two elements in the array, lets say ordered pair (index i,index j) is defined as

Distance(arr[i],arr[j]) = (i x arr[i]-j x arr[j]) - (arr[i]+arr[j])

for 0< i,j< len(arr)

find the value of maximum distance possible among all the possible pairs.

Note- a pair can contain any two elements of the array. for ex- [1,2,3] has following pairs (1,1),(1,2),(1,3),(2,1),(2,2),(2,3),(3,1),(3,2),(3,3)

Input
first line of the input contains N(number of elements of the array). the next line contains N space separated integers representing the elements of the array.

Output
print the maximum distance possible from all the possible pairs.

Example
Input:

3

4 1 5

Output:

3

Explanation:

(4,4) -> distance is: 0X4-0X4-4-4=-8

(4,1) -> distance is: 0X4-1X1-4-1=-6

(4,5) -> distance is: 0X4-2X5-4-5=-19

(1,4) -> distance is: 1X1-0X4-1-4=-4

(1,1) -> distance is: 1X1-1X1-1-1=-2

(1,5) -> distance is: 1X1-2X5-1-5=-15

(5,4) -> distance is: 2X5-0X4-5-4=1

(5,1) -> distance is: 2X5-1X1-5-1=3(maxima)

(5,5) -> distance is: 2X5-2X5-5-5=-10

'''
n=int(input())
arr=[int(x) for x in input().split()]
i=0
j=0