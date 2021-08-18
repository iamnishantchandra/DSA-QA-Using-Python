"""
Monotonic Array
Given as array containing n integers, verify if the array is Monotonic.

An array is called monotonic if it is either monotone increasing or monotone decreasing. An array A is 
monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, 
A[i] >= A[j].

Input
First line contains n, number of elements in the array.

Next n lines contains an integer in each line.

Output
Print True if given integers are Monotonic

Print False if given integers are not Monotonic

Example
Input:

5

3

12

34

34

56

Output:

True

"""
n=int(input())
a=[]
incr=True
flag=True
for i in range(n):
    a.append(int(input()))
for i in range(1,n):
    if(a[i-1]<=a[i]):
        incr=True
    else:
        incr=False
if incr:
    flag=True
else:
    for i in range(1,n):
        if(a[i-1]>=a[i]):
            flag=True
        else:
            flag=False
print(flag)