"""
K-sum MinMax
Given a sequence of integers, a subarray of length K is defned as a sequence of K consecutive elements 
of the array.

i.e- for a sequence starting at ai-> [a(i),a(i+1),a(i+2),.....a(i+K-1)]

Find out the minimum and and maximum value of sum of all subarray of length K.( where K is provided as 
an input)

Constraints
1<= length of list<= 100000

1<= K<= length is list

Input
first line of the input contains 2 space separated integers representing the value of N(number of 
elements of the sequence) and K respectively. Second line contains the N space separated integers 
denoting the N elements of the sequence.

Output
print the maximum sum of all subarrays of length K followed by minimum sum of all subarrays of length 
K.(space separated)

Example
Input:

6 3

3 4 -2 8 -1 7

Output:

14 5

Explanation:

1st subarray: 3 4 -2-> sum = 5(minima)

2nd subarray: 4 -2 8-> sum= 10

3rd subarray: -2 8 -1 -> sum= 5

4th subarray: 8 -1 7-> sum= 14(maxima)
"""
n,k=map(int,input().split())
lis=list(map(int,input().split()))

a=[]
ma=0
mi=100**100
sum0=0
for j in range(n-k+1):
    sum0=0
    for i in range(k):
        sum0+=lis[j+i]
    print(sum0)
    if mi>sum0:
        mi=sum0
    elif ma<sum0:
        ma=sum0 
print(str(ma)+" " +str(mi))