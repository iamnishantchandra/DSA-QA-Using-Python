'''
Array Rotation
Given an array of integers and a set of queries, perform all the queries in sequential fashion from first to last. A query can be of two types-

1) L N -> rotate the array left by N units.

2) R N -> rotate the array Right by N units.

Finally print the array after performing all the queries.

ex- for given arr= a1,a2,a3,a4,a5,a6,a7,a8, a query (L 2) will change the array into arr= a3,a4,a5,a6,a7,a8,a1,a2

ex- for given arr= a1,a2,a3,a4,a5,a6,a7,a8, a query (R 4) will change the array into arr= a5,a6,a7,a8,a1,a2,a3,a4

Constraints
1<= length of array<= 1000000

1<= number of queries<= 1000000

Input
First line of the input contains N, Q representing the size of the array and number of queries respectively. second line contains the space separated elements of the array. corresponding 'Q' lines contains each query. every query contains two entries, first one being the type of query L/R and the second one is the amount by which the array is to be rotated.

Output
Print the elements of the array after performing all the queries in a single line space separated.

Example
Input:

5 3

1 2 3 4 5

L 2

R 4

L 3

Output:

2 3 4 5 1

Explanation:

initially-

1 2 3 4 5

after 1st query-

3 4 5 1 2

after 2nd query-

4 5 1 2 3

after 3rd query-

2 3 4 5 1


'''
x,y=map(int,input.split())
arr=list(map(int,input().split()))
for i in range(y):
    x,y=input.split()


